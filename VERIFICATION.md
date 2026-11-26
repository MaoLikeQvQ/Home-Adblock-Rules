# 本地验证记录

验证日期：2026-11-26。测试环境：macOS ARM64、Python 3.13.5。本次验证使用下载保存的真实上游规则快照；各输入的完整 SHA-256 见 `dist/report.json`。

## 生成结果

| 输出 | 拦截规则 | 放行规则 |
| --- | ---: | ---: |
| Mihomo / Clash Meta | 253,628 | 194 |
| AdGuard Home / AdGuard DNS | 252,647 | 194 |

上游输入：秋风 Classical 998 条去重后的拦截规则；秋风 AdGuard 982 条去重后的拦截规则；217heidai DNS 252,252 条拦截规则及 194 条放行规则；Home DNS 全量 1,019 条规则。规则文件的说明头可能使用原始行数，本项目统计实际解析、去重后的规则数。

## 自动检查

- `python3 -m unittest discover -s tests -v`：20 项通过。
- `actionlint v1.7.12`：`.github/workflows/update.yml` 检查通过。
- 临时本地裸 Git 仓库模拟工作流的真实 shell 脚本：首次发布、读取上一版统计、无变化不提交、更新时正常追加提交，均通过。
- 输出与源码检查：没有依赖第三方 Python 库；生成规则、来源快照、许可与配置齐全。

## Mihomo 内核验证

内核版本：官方 `v1.19.34`，macOS ARM64。

- 配置检查通过。
- 使用生成的 `mihomo.example.yaml` 配置片段，通过本机 HTTP 订阅服务成功下载并加载两个规则提供者。
- API 返回拦截集 `253628` 条、白名单集 `194` 条。
- 请求 `ad.12306.cn`：命中广告逻辑规则，使用 `REJECT`。
- 请求 `app.adjust.com`：命中上游白名单，跳过广告拒绝规则，继续执行后面的 `MATCH`。测试配置的 `MATCH` 为 `DIRECT`；白名单自身不指定路由策略。
- Home DNS 独有规则 `activity-ag.awemeughun.com` 已进入合并订阅，AdGuard Home 检查命中 `FilteredBlackList`。

## AdGuard Home 内核验证

内核版本：官方 `v1.0.0`，macOS ARM64。

- 隔离配置检查通过。
- 通过本机 HTTP 订阅服务成功加载 `252841` 条规则，即 `252647` 条拦截与 `194` 条放行。
- 过滤检查 `ad.12306.cn`：`FilteredBlackList`，命中 `||ad.12306.cn^`。
- 过滤检查 `app.adjust.com`：`NotFilteredWhiteList`，命中 `@@||app.adjust.com^`。
- 向测试 DNS 监听端口发送真实 UDP A 查询，`ad.12306.cn` 返回 `0.0.0.0`，符合测试配置的默认阻断模式。

测试仅使用隔离工作目录与回环地址的高位端口，没有安装系统服务或修改系统 DNS。

## 尚未覆盖

- GitHub 托管环境中的首次 Actions 执行及线上 Raw 地址，需要发布仓库后验证。
- 旧 Clash 内核兼容性、实体路由器性能、具体 App 的所有广告场景，没有完成实机验证。
- 这些检查证明规则可构建、内核可加载及所选拦截/放行场景有效，不代表所有广告都能拦截或没有误拦。

## 来源真实性与合并贡献

真实在线构建先把三个 GitHub 项目的来源固定到提交，再下载该提交上的文件；全部原始输入、SHA-256、Git Blob SHA-1 与贡献统计记录在 `dist/report.json` 和 `dist/SOURCES.md`。Home DNS 的 1,019 条输入全部保留；相对其他来源，AdGuard 有 29 条独有规范化规则，Clash 有 417 条。两者差异来自精确域名与后缀规则分别保留，这些数值不等同于新增覆盖的域名数量。
