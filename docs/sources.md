# 上游规则管理

来源选择以 [sources.json](../config/sources.json) 为当前真源。本页不固定最新规则数量，具体数量以相应版本的 `report.json` 为准。

## 当前来源

| 项目 | 源文件与分支 | 目标 | 定位与注意事项 |
| --- | --- | --- | --- |
| [秋风 AWAvenue](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) | `main/Filters/AWAvenue-Ads-Rule-Clash-Classical.yaml` | Mihomo | 保留精确域名、后缀、关键字、IP 规则 |
| 同一秋风项目 | `main/AWAvenue-Ads-Rule.txt` | AdGuard | 保留 DNS 原生域名及模式 |
| [217heidai](https://github.com/217heidai/adblockfilters) | `dist/adblockdns.txt` | 两种格式 | 广覆盖的合并源，含原生放行规则；不同版本可能有规则进出 |
| [Home DNS](https://github.com/abclq/home-dns-adblock) | `main/dist/adguard-dns-full.txt` | 两种格式 | 完整公开订阅，含手工与社区规则；不等于继承其服务端保护策略 |

这是三个独立项目、四个输入文件。[秋风订阅网页](https://awavenue.top/Sub.html?tool=clashClassical) 与秋风仓库是同一来源。217heidai 和 Home DNS 自身还收录秋风等规则，不能把来源条数相加当作独立覆盖增量。

2026-11-26 保存的 Home DNS 全量文件为 1,019 条去重规则，单独 Clash 文件为 75 条。选择全量文件是为了接入完整订阅；这些数量是历史快照，不保证上游一直相同。

## 来源证明的范围

当前构建先把 GitHub 分支固定至提交，再下载不可变地址，保存输入 SHA-256、Git Blob SHA-1、原始快照以及各格式的贡献统计。[历史独立核验](source-verification-2026-11-26.json) 另经 GitHub Contents API 对照源文件 Blob 哈希。

这些信息证明输入身份、内容和构建可追溯性。它们不能证明某域名一定只用于广告，不能证明作者的环境与我们的家庭设备相同，也不能保证不同来源合并后的业务兼容性。

`added_after_previous_sources` 与配置顺序有关；独有规则数按完全相同的规范化规则计算。精确规则与后缀规则分别保留，规则文本独有不代表网络覆盖独有。白名单覆盖的子域可能仍以拦截项出现在文件中，真正生效结果要由内核回归确认。

## Home DNS 的保护策略为何需要单独处理

Home DNS 的 [同步脚本](https://github.com/abclq/home-dns-adblock/blob/27a0a29c9941759662f48b78c985d0273caaa023/scripts/sync_upstream.py) 对受保护域、部分主域和广告例外进行筛选；公开全量拦截文件不是这套策略的完整序列化。

在此前保存的合并输入中，`gecko.snssdk.com`、`is.snssdk.com`、`tz.sec.xiaomi.com` 存在与它的保护名单相冲突的拦截项。这是策略冲突线索，不是已经在本项目设备上证实的故障。直接将 Home DNS 规则与其他源取并集，其他源可能重新引入它剔除的项。

因此保护策略属于本项目维护的配置。上游保护名单作为候选依据，先审查原因、适用 App 和例外，再建立本项目场景与证据。尤其不能为了保护视频主域而全域放行，又期待其中的广告子域仍被拦截。具体处理见 [验证设计](validation.md)。

## 新增或调整来源的流程

1. 确认原生格式、原始分发地址、分支迁移、许可和署名要求。
2. 用固定快照验证解析器；检查例外、条件修饰符、IP、关键字与通配符。
3. 生成与现有来源的重叠、独有规则及变化报告，明确接入价值。
4. 检查保护策略冲突；将关键规则及历史误拦纳入场景回归。
5. 待候选通道实现后，仅先进入候选，固定版本试用后再晋升。当前直发阶段，不能把新增来源视作已经获得业务验证。

停用或替换来源也需要展示删除与白名单变化，保留历史快照。首阶段不增加来源数量、Lite/纯广告等新产品变体；先把现有三家的验证和发布闭环完成。

## 许可边界

本项目源码使用 [MIT](../LICENSE)；秋风、217heidai 的规则遵循其 GPLv3 要求；Home DNS 原始规则携带 MIT 版权声明。合并分发保留三份上游原始许可及 [署名说明](../NOTICE.md)，不能用根目录 MIT 覆盖合并规则的 GPLv3 要求。
