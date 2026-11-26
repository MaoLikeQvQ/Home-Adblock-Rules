# 维护与本地构建

本文只描述当前已实现的命令和工作流。目标架构见 [工程架构](architecture.md)，待实施任务见 [实施计划](roadmap.md)。

## 自己维护规则

编辑 `config/blocklist.txt`，每行一条：

```text
DOMAIN,ads.example.com
DOMAIN-SUFFIX,tracker.example.net
IP-CIDR,192.0.2.1/32,no-resolve
DOMAIN-KEYWORD,example-ad
```

- `DOMAIN` 只匹配该域名；输出到 AdGuard 时使用 `|domain^`，保留精确语义。
- `DOMAIN-SUFFIX` 匹配域名及其子域名；输出到 AdGuard 时使用 `||domain^`。
- IP 和关键字规则只进入 Clash 输出，并记录在 `report.json` 的 `local_clash_only_rules`，不会直接改写成 DNS 后缀规则。

遇到误拦，编辑 `config/allowlist.txt`：

```text
DOMAIN,api.example.com
DOMAIN-SUFFIX,example.org
```

白名单只接受精确域名与域名后缀。它与 217heidai 的原生放行规则合并，对所有合并来源生效，并优先于本地黑名单。填写后重新构建或提交到 `main`，让 Actions 更新订阅。

`config/sources.json` 中可以替换、增加或删除来源。当前支持 `classical` 与 `adguard` 两种格式，后者转换到 Clash 时只接受可保留匹配语义的域名规则；不支持的输入会中止构建。`min_rules` 是最低拦截规则数；`max_drop_ratio` 默认为 `0.35`，表示与上次同地址来源相比减少超过 35% 时停止发布。上游有意精简规则时，先核对变化，再调整阈值。

秋风默认使用完整方案，包含广告、隐私与不受欢迎类规则。若改用秋风的纯广告版本，也需要考虑 217heidai 与 Home DNS 仍可能包含同类拦截；仅更换秋风文件不会把整个合并订阅变成纯广告版。

## 本地构建

需要 Python 3.10 或更高版本：

在检出的项目根目录执行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules
```

输出在本地 `dist/`。该目录被 `.gitignore` 排除，由 Actions 单独发布，不需要提交到源码分支。

从已经保存的原始来源离线复现：

```bash
python3 scripts/build.py \
  --repository MaoLikeQvQ/Home-Adblock-Rules \
  --source-dir dist/sources
```

`--source-dir` 中的文件名采用 `<source-id>.txt`。生成器保留本轮原始输入，所有输出采用稳定排序，相同输入与项目配置重复构建会得到相同文件。

## 发布到自己的 GitHub

1. 在自己的账号创建公开仓库（本项目为 `Home-Adblock-Rules`），以 `main` 为默认分支。
2. 提交并推送本项目源码。第一次推送包含工作流时会触发构建。
3. 在仓库的 Actions 中查看 **Update subscriptions**；也可以手动点击 **Run workflow**。
4. 构建和发布都成功后，会出现 `dist` 分支；[项目首页](../README.md) 的 Raw 链接即可作为订阅。

无需 GitHub Pages、服务器或自定义 Token。发布任务使用 GitHub 提供的 `GITHUB_TOKEN`，仅发布任务需要 `contents: write`。如果组织策略或分支保护禁止工作流写入 `dist`，应针对该发布方式配置权限，再重新运行。公开订阅地址需要规则文件能被客户端无认证访问。

定时任务约在北京时间 **00:23、08:23、16:23** 运行，GitHub 调度可能有延迟。修改 `config/`、生成脚本或工作流也会触发更新。拉取请求只验证和构建，不发布订阅。

任何必需来源下载失败、出现未知格式、低于最低条数或相对上次明显骤减，都不会发布半份规则。完整生成后才替换本地输出；在线 `dist` 也只在构建成功后更新。全部发布文件均未变化时不创建空提交。

## 当前验证命令

```bash
python3 -m unittest discover -s tests -v
```

它运行解析、构建、来源固定和快照复现等回归测试。当前仓库没有持续运行两种内核的测试命令，也没有候选晋升或自动回滚命令。历史内核试验记录见 [验证记录](../VERIFICATION.md)。

## 当前更新失败的处理

从 Actions 的失败步骤与错误信息定位来源、格式或数量变化。先对照固定输入和上一版报告，再修正配置或解析器；不以关闭检查作为常规恢复手段。更改源码、配置和工作流会触发重新构建。线上已有 `dist` 在构建失败时保持原样，但客户端可能仍有旧缓存。

本地从 `dist/sources` 离线复现的是已保存输入；它用于确认构建一致性，不能证明上游最新分支或真实 App 当前行为。
