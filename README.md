# Home-Adblock-Rules

> **自用声明与免责说明**
>
> 本项目为个人自用的去广告规则合集，按现状提供，不承诺持续维护、拦截效果或兼容所有软件。规则可能漏拦、误拦或影响正常服务，请自行判断、备份配置并承担使用风险。维护者在适用法律允许的范围内不对使用本项目造成的损失负责。
>
> 本项目不是上游官方订阅，合并规则的来源、版权及许可归原作者所有，使用和再分发须遵守对应许可。

合并秋风、217heidai 和 Home DNS 的规则，生成 Mihomo 与 AdGuard DNS 格式。**按内核选择订阅，同一内核不区分设备型号。**

## 订阅地址

| 内核 / 过滤引擎 | 内容 | 地址 |
| --- | --- | --- |
| Mihomo / Clash Meta | 拦截规则，Classical YAML | https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml |
| Mihomo / Clash Meta | 配套放行白名单，Classical YAML | https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml |
| AdGuard Home / AdGuard DNS 过滤引擎 | DNS 过滤规则，已含放行例外 | https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt |

**Mihomo / Clash Meta：**拦截规则和白名单配套使用，均选择 `behavior: classical`、`format: yaml`。白名单不设为拦截或强制直连，通过 [配置片段](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/mihomo.example.yaml) 中的逻辑规则保留原有分流。

**AdGuard：**将 `adguard.txt` 地址添加到自定义 DNS 封锁清单，只需这一条订阅。

这些是规则订阅，不含代理节点。未验证其他内核的兼容性。以上 `dist` 为稳定地址；每 8 小时自动构建的新版先进入 `candidate`，审核后再更新稳定版，构建状态见 [GitHub Actions](https://github.com/MaoLikeQvQ/Home-Adblock-Rules/actions/workflows/update.yml)。

## 规则来源

- [AWAvenue 秋风](https://github.com/TG-Twilight/AWAvenue-Ads-Rule)：Clash Classical 与 AdGuard DNS 原生文件。[官网订阅页](https://awavenue.top/Sub.html?tool=clashClassical) 属于同一来源。
- [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters)：`dist` 分支的 `adblockdns.txt`。
- [abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock)：`main` 分支的 `dist/adguard-dns-full.txt`。

构建固定上游版本、保留放行例外、按原有匹配范围合并去重，并保存来源快照及哈希。完整配置见 `config/sources.json`。

## 项目维护

[维护说明](docs/maintenance.md) · [开发说明](docs/development.md) · [保护策略](docs/protection.md)

源码采用 [MIT](LICENSE)；合并规则按 GPL-3.0-only 发布，并保留 Home DNS 的 MIT 版权声明。详见 [NOTICE.md](NOTICE.md) 和 `licenses/`。
