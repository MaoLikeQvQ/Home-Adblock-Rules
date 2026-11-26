# Home-Adblock-Rules

把秋风广告规则、217heidai AdBlock DNS Filters 与 abclq Home DNS Adblock 合并成自己的去广告规则订阅，同时支持 **Mihomo / Clash Meta** 和 **AdGuard Home / AdGuard DNS**。

使用 Python 标准库构建，无需安装第三方 Python 依赖。GitHub Actions 每 8 小时同步上游，规则发布到独立的 `dist` 分支，源码保留在 `main` 分支。

项目仓库：[MaoLikeQvQ/Home-Adblock-Rules](https://github.com/MaoLikeQvQ/Home-Adblock-Rules)。在线规则已由本仓库的 GitHub Actions 生成并发布，可以直接订阅下列地址。

## 规则来源

| 上游 | 读取内容 | 输出 |
| --- | --- | --- |
| [AWAvenue 秋风广告规则](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) | 官方 Clash Classical 规则 | Mihomo |
| 同一秋风项目 | 官方 AdGuard DNS 规则 | AdGuard Home |
| [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) | `dist/adblockdns.txt`，含拦截与放行规则 | 两种格式 |
| [abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock) | `dist/adguard-dns-full.txt`，精确规则与社区上游规则的完整订阅 | 两种格式 |

[秋风订阅生成器](https://awavenue.top/Sub.html?tool=clashClassical) 与秋风 GitHub 仓库属于同一个上游，不作为第三个独立规则源。217heidai 本身也收录了秋风；合并时会对相同匹配类型与相同内容去重。

`home-dns-adblock` 同时是参考项目与规则上游。它的完整 AdGuard 文件当前包含 1,019 条去重规则，而单独的 Clash 文件只有 75 条手工规则，所以这里选用完整订阅转换到两种输出。它的系统服务、Tailscale 部署以及 `config/whitelist.txt` 中含特殊穿透例外的服务端策略没有直接搬入；本项目保留完整订阅自身的匹配语义，使用自己的白名单及订阅中的原生例外。

## 订阅文件

发布成功后，订阅地址如下。修改仓库名或所有者时，将地址中的 `MaoLikeQvQ/Home-Adblock-Rules` 一并替换。

| 文件 | 用途 | 地址 |
| --- | --- | --- |
| `clash.yaml` | Classical 拦截规则集 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml` |
| `clash-allow.yaml` | Classical 白名单规则集，须与上项配套 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml` |
| `adguard.txt` | AdGuard DNS 订阅，已包含白名单 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt` |
| `mihomo.example.yaml` | 自动生成的配置片段 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/mihomo.example.yaml` |
| `report.json` | 每个来源的规则数、SHA-256、生成统计 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/report.json` |
| `SOURCES.md` | 固定上游版本、文件哈希、重复与实际新增规则的可读核对表 | `https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/SOURCES.md` |
| `sources/` | 构建用原始规则、配置、脚本与许可 | `dist` 分支同名目录 |

`clash.yaml` 是规则集，需要通过 `rule-providers` 使用；它不包含代理节点，不能作为完整代理配置订阅直接导入。

## 如何核对规则来源

每次在线构建先通过 GitHub API 把上游分支固定到具体提交，再从该提交下载文件，避免只记录一个会继续变化的分支地址。打开 `dist` 分支的 `SOURCES.md`，可以看到每个输入的不可变下载地址、上游提交、原始快照、SHA-256、Git Blob SHA-1，以及合并去重后的实际新增和独有规则示例。完整机器可读证据在 `report.json`。首次发布时另行通过 GitHub Contents API 核对了四个输入文件，返回的上游 Git Blob SHA-1 全部匹配原始快照；记录见 [2026-11-26 来源独立核验](docs/source-verification-2026-11-26.json)。

可将 `report.json` 中某个来源的 `resolved_url` 文件下载后计算 SHA-256，与它的 `sha256` 比较。比如在本地查看 Home DNS 的证据：

```bash
python3 -c 'import json; r=json.load(open("dist/report.json")); print(next(s for s in r["sources"] if s["id"]=="home-dns"))'
shasum -a 256 dist/sources/home-dns.txt
```

来源之间会互相收录，不能把上游条数直接相加。报告中的“新增”“独有”按完全相同的规范化规则计算；精确域名与后缀规则不视作同一条，也不把这些数字等同于新增覆盖的域名数量。上游自身更新也可能让总条数下降，应结合每个固定版本核对。

## Mihomo / Clash Meta 用法

把下面片段合并进现有配置；已有 `rule-providers:` 或 `rules:` 时，合并其中的条目，不要重复顶层键。把广告逻辑规则放在广泛匹配规则和 `MATCH` 前面。

```yaml
rule-providers:
  home-adblock:
    type: http
    behavior: classical
    format: yaml
    url: https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml
    path: ./ruleset/home-adblock.yaml
    interval: 28800
  home-adblock-allow:
    type: http
    behavior: classical
    format: yaml
    url: https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml
    path: ./ruleset/home-adblock-allow.yaml
    interval: 28800

rules:
  - AND,((RULE-SET,home-adblock),(NOT,((RULE-SET,home-adblock-allow)))),REJECT
  # 接着保留你现有的分流规则与 MATCH。
```

这条逻辑规则只拒绝“命中广告规则且不在白名单”的连接。白名单继续走后面的正常分流，不会被强制改成直连。**两个规则提供者必须一起配置。** 只添加拦截集会丢失上游的例外保护。

推荐使用 Mihomo 内核（Clash Meta）。不支持 `AND` / `NOT` / `RULE-SET` 组合的旧 Clash 内核需要升级；本项目没有对旧 Clash 内核完成兼容验证。

## AdGuard Home 用法

进入“过滤器 → DNS 封锁清单 → 添加拦截列表 → 添加自定义列表”，填写：

```text
https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt
```

AdGuard DNS 或支持 DNS 过滤语法的 AdGuard 客户端也可以使用该文件。`@@` 放行规则已经合并在同一订阅中，不需要再单独添加白名单订阅。浏览器元素隐藏与脚本过滤不在这份 DNS 规则的范围内。

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

秋风默认使用完整方案，包含广告、隐私与不受欢迎类规则。若改用秋风的纯广告版本，也需要考虑另一个合并来源 217heidai 仍可能包含同类拦截；仅更换秋风文件不会把整个合并订阅变成纯广告版。

## 本地构建

需要 Python 3.10 或更高版本：

```bash
cd /Users/maolike/Desktop/Mike/home-adblock-rules
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

本地试用可以在项目目录运行：

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory dist
```

然后在同一台电脑上的客户端使用 `http://127.0.0.1:8080/adguard.txt`，或把 Mihomo 两个提供者的 URL 分别改成该服务的对应文件地址。此地址仅供本机临时测试，终端关闭后服务停止。

## 发布到自己的 GitHub

1. 在自己的账号创建公开仓库（本项目为 `Home-Adblock-Rules`），以 `main` 为默认分支。
2. 提交并推送本项目源码。第一次推送包含工作流时会触发构建。
3. 在仓库的 Actions 中查看 **Update subscriptions**；也可以手动点击 **Run workflow**。
4. 构建和发布都成功后，会出现 `dist` 分支；上面的 Raw 链接即可作为订阅。

无需 GitHub Pages、服务器或自定义 Token。发布任务使用 GitHub 提供的 `GITHUB_TOKEN`，仅发布任务需要 `contents: write`。如果组织策略或分支保护禁止工作流写入 `dist`，应针对该发布方式配置权限，再重新运行。公开订阅地址需要规则文件能被客户端无认证访问。

定时任务约在北京时间 **00:23、08:23、16:23** 运行，GitHub 调度可能有延迟。修改 `config/`、生成脚本或工作流也会触发更新。拉取请求只验证和构建，不发布订阅。

任何必需来源下载失败、出现未知格式、低于最低条数或相对上次明显骤减，都不会发布半份规则。完整生成后才替换本地输出；在线 `dist` 也只在构建成功后更新。规则和来源未变化时不创建空提交。

## 验证与效果范围

自动测试覆盖原生格式解析、精确/后缀匹配范围、白名单、本地补充规则、未知语法拒绝、规则骤减、失败保留旧文件以及重复构建一致性。

已完成的实际内核与工作流验证见 [VERIFICATION.md](VERIFICATION.md)。

真实 App 广告、视频与正片共用域名、已经缓存的广告、客户端绕过所配置 DNS 或代理的请求，不能仅凭构建成功判断效果。使用时可以通过 Mihomo 连接记录或 AdGuard Home 查询日志核对命中的规则；发现误拦先加白名单，再向具体上游反馈。

该合并规则体积由 217heidai 的完整列表主导，适合需要广覆盖的场景。若设备资源有限，可自行评估其 Lite 来源并调整配置与阈值；本项目没有对所有路由器型号完成性能验证。

## 许可

项目源码沿用仓库的 [MIT 许可](LICENSE)；合并规则继承上游的 **GPLv3** 要求，不能按 MIT 再授权。原作者保留各自版权，来源与完整规则许可见 [NOTICE.md](NOTICE.md) 和 `licenses/`。`dist/sources/` 随规则公开构建输入与生成脚本，便于追溯和复现。
