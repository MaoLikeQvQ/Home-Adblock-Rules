# Home-Adblock-Rules

合并秋风、217heidai 与 Home DNS 三个上游项目，生成 **Mihomo / Clash Meta** 和 **AdGuard Home / AdGuard DNS** 去广告规则订阅，保留来源版本、原始快照与内容哈希。

项目仓库：[MaoLikeQvQ/Home-Adblock-Rules](https://github.com/MaoLikeQvQ/Home-Adblock-Rules)。使用 Python 标准库和 GitHub Actions，无需自建服务器。

## 当前状态与建设方向

**当前已经可以订阅，工作流每 8 小时构建成功后直接更新 `dist`。业务保护策略、持续内核回归、候选版晋升和受控回滚仍待实施。** 来源真实性和历史测试通过，不代表全部规则、App 或设备已经完成误拦验证。

项目下一阶段按“合并后统一保护 → 差异与风险检查 → 两种内核回归 → 固定候选试用 → 稳定晋升”建设。2026-11-26 本轮只更新工程规划和文档，不切换现有发布流程。

| 能力 | 状态 |
| --- | --- |
| 三家上游、四个输入，固定提交并保存原始文件和哈希 | 已实现 |
| 语义保留、合并去重、本地拦截与白名单、异常输入和条数检查 | 已实现 |
| 构建与来源测试 | 当前有 20 项；不包含全套业务场景 |
| Mihomo 与 AdGuard Home 加载、拦截、放行及 DNS 查询 | 在历史指定版本本地验证，尚未持续运行于 CI |
| 业务保护、变更风险报告、候选/稳定隔离、自动化回滚工具 | 待实施 |

具体任务和验收条件见 [实施计划](docs/roadmap.md)，历史证据见 [验证记录](VERIFICATION.md)。

## 订阅入口

| 文件 | 用途 | 地址 |
| --- | --- | --- |
| `clash.yaml` | Mihomo Classical 拦截集 | [订阅](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml) |
| `clash-allow.yaml` | 配套放行集 | [订阅](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml) |
| `mihomo.example.yaml` | 合并进现有配置的示例 | [配置片段](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/mihomo.example.yaml) |
| `adguard.txt` | AdGuard DNS 规则，含放行例外 | [订阅](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt) |
| `SOURCES.md` | 来源版本、哈希与合并贡献 | [核对表](https://github.com/MaoLikeQvQ/Home-Adblock-Rules/blob/dist/SOURCES.md) |
| `report.json` | 机器可读来源与输出统计 | [报告](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/report.json) |

Mihomo 必须配套使用两个规则集，通过逻辑排除保留白名单原有分流。规则集不包含代理节点，不能当完整代理配置订阅导入；旧 Clash 内核没有完成兼容验证。两文件可变 URL 的客户端刷新不保证同时完成，固定版本方案见 [发布设计](docs/release.md)。

AdGuard Home 在“过滤器 → DNS 封锁清单 → 添加自定义列表”填写上表 `adguard.txt` 地址。完整配置和误拦排查见 [使用指南](docs/usage.md)。

## 规则来源

| 项目 | 当前输入 | 输出 |
| --- | --- | --- |
| [AWAvenue 秋风](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) | 官方 Clash Classical、AdGuard DNS 两种原生文件 | 分别用于 Mihomo、AdGuard |
| [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) | `dist` 分支的 `adblockdns.txt`，含放行规则 | 两种格式 |
| [abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock) | `main/dist/adguard-dns-full.txt` 全量订阅 | 两种格式 |

[秋风订阅网页](https://awavenue.top/Sub.html?tool=clashClassical) 与其 GitHub 仓库是同一项目；三个来源互有收录，去重贡献不等同于独立覆盖增量。Home DNS 规则已纳入，但它的服务端业务保护策略没有自动继承；其他来源可能重新带入它剔除的规则。

来源选择、许可与证据边界见 [上游规则管理](docs/sources.md)。

## 本地构建

需要 Python 3.10+，无需第三方 Python 依赖。在项目目录执行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules
```

当前来源在 `config/sources.json`，自定义拦截和放行分别在 `config/blocklist.txt`、`config/allowlist.txt`。输出写入被 Git 忽略的本地 `dist/`，源码不混入生成规则。修改配置可能触发在线直发，维护前先核对 [当前维护流程](docs/maintenance.md)。

## 工程文档

完整入口见 [文档索引](docs/README.md)。

| 文档 | 内容 |
| --- | --- |
| [工程架构](docs/architecture.md) | 项目范围、现状、目标模块与依赖 |
| [验证与保护设计](docs/validation.md) | 全来源保护、业务例外、风险审核、内核和设备验收 |
| [发布设计](docs/release.md) | 候选、稳定晋升、配套版本一致性、回滚与迁移 |
| [实施计划](docs/roadmap.md) | P0 盘点和 P1–P4 的任务、依赖及验收条件 |
| [维护指南](docs/maintenance.md) | 现有规则编辑、构建、离线复现和 Actions |

规则无法保证消除与正片同域名、已缓存或绕过过滤路径的广告，也没有完成全型号路由器性能验证。本项目首先完成现有两种格式的验证与发布机制，再评估更多来源、格式或轻量变体。

## 许可

源码使用 [MIT](LICENSE)。合并规则保留上游 GPLv3 要求和 Home DNS 的 MIT 版权声明；根目录 MIT 不能替代规则许可。完整说明见 [NOTICE.md](NOTICE.md) 和 `licenses/`。
