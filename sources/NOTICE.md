# 上游署名与许可

本项目的生成脚本为新编写的实现，沿用仓库初始化时的 MIT 许可（见根目录 `LICENSE`）。合并后的规则以 GPL-3.0-only 发布，不能用源码的 MIT 许可替代规则的 GPLv3 要求。规则来自以下项目，原作者及贡献者保留各自版权：

| 项目 | 用途 | 许可及原文 |
| --- | --- | --- |
| [TG-Twilight/AWAvenue-Ads-Rule](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) | Clash Classical 与 AdGuard DNS 两种原生规则 | [GPLv3](licenses/AWAvenue-LICENSE) |
| [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) | AdBlock DNS 规则及放行规则 | [GPLv3](licenses/217heidai-LICENSE) |
| [abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock) | 精确规则与上游合并后的完整 AdGuard DNS 订阅；同时转换成 Clash 域名后缀规则 | [MIT，Copyright (c) 2026 abclq](licenses/home-dns-adblock-LICENSE) |

生成文件为以上规则的合并、规范化、去重及格式转换版本，加入可选本地规则与白名单，并非上游官方发布。规则文件头保留来源与许可链接；`sources/` 随订阅发布构建时的原始规则快照、原许可、配置及生成脚本；`report.json` 记录每个输入的 SHA-256 与规则数量。上游可能进一步汇集其他作者规则，完整贡献与来源以各上游仓库、原始规则头及其许可声明为准。

[abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock) 既是项目思路参考，也是真实的规则上游。本项目读取其 `dist/adguard-dns-full.txt`，覆盖其公开全量订阅；没有复制其脚本、文档或系统部署方案，也不继承其效果与“零误伤”声明。其单独的 `clash-surge-rules.txt` 当前只含 75 条手工规则，因此采用完整 AdGuard 订阅转换，避免漏掉它的社区规则。

秋风官网订阅生成器与秋风仓库是同一项目；本项目按输出格式读取两个原生文件，每个订阅只合并一次秋风。217heidai 本身也包含秋风；本项目去除完全相同的规则，保留不同的匹配范围，不做将子域合并成父域之类的扩大拦截转换。

项目按现状提供，不保证所有广告都可拦截或没有误拦。源码许可见 [LICENSE](LICENSE)，规则的完整 GPLv3 许可与 MIT 上游版权见上述原始许可文件。
