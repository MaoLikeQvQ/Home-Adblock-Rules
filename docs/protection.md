# 保护策略

策略对全部来源合并后的规则统一生效。`config/allowlist.txt` 保存明确放行，`config/protection.json` 保存保护范围、广告例外及采纳依据。

## 处理语义

- `scope: exact` 仅保护该域；`suffix` 包含本域及标签边界内的子域。
- 拦截范围完全落入保护、又不在 `permitted_block_rules` 中时，从输出剔除并记录全部来源。例外只能保留已经存在且类型和值等价的规则，不扩大拦截。
- 父域拦截与保护仅部分重叠、策略冲突、例外越界或本地规则违反保护时失败，不按来源顺序隐式覆盖。
- 禁用策略不提供保护；`evidence_level` 标记依据类型，不代表已验证所有真实使用场景。

父域下仍有广告子域时，不能用全局放行替代黑名单筛选。例如 `@@||qznovelvod.com^` 也会放过其中的广告子域。

## 已采用的保护

依据 Home DNS [固定版本白名单](https://github.com/abclq/home-dns-adblock/blob/27a0a29c9941759662f48b78c985d0273caaa023/config/whitelist.txt) 及 [域名说明](https://github.com/abclq/home-dns-adblock/blob/27a0a29c9941759662f48b78c985d0273caaa023/docs/domain-list.md)，当前保护以下后缀：

| 域名 | 上游用途说明 |
| --- | --- |
| `gecko.snssdk.com` | 业务资源下发 |
| `is.snssdk.com` | 风控业务 |
| `tz.sec.xiaomi.com` | 小米系统服务 |

三项均为 `upstream-reference`，表示采纳上游依据，实际业务影响仍需验证。其他 CDN、视频、图片和 Apple 范围没有整表照搬。新增保护需保存明确依据及回归，实际配置以 `config/protection.json` 为准。

## 审核

关键字、通配模式可能与保护后缀产生交集，工具生成合成子域验证匹配限制。IP 规则需结合实际连接目标和命中情况判断；`no-resolve` 不保证不会影响已有目标 IP 的连接。

每轮明细由 `decisions.json`、`validation.json` 和 `VALIDATION.md` 生成，不在静态文档中保存易过期的数量或逐项报告。来源或白名单变化、模式/IP 新增、匹配范围扩大等需要审核；无稳定基准时进行 bootstrap 审查。

来源哈希、DNS 可解析或少量样例通过，均不能单独证明广告属性和业务安全。出现误拦时记录规则版本与实际命中，对具体域名或 IP 做放行对照，确认后更新策略并重新构建验证。
