# Home-Adblock-Rules

合并秋风、217heidai 和 Home DNS 的去广告规则，生成 **Mihomo / Clash Meta** 与 **AdGuard Home / AdGuard DNS** 订阅，保留来源版本、原始文件及内容哈希。使用 Python 标准库和 GitHub Actions，无需自建服务器。

## 订阅地址

**Mihomo / Clash Meta 拦截规则：**

https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml

**Mihomo 配套白名单（放行例外，不含拦截规则）：**

https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml

当前 Mihomo 实现需要两份文件配合：拦截命中黑名单且不在白名单中的连接。白名单继续走现有分流。配置方法见 [使用指南](docs/usage.md)。

**AdGuard Home / AdGuard DNS（已含放行例外，只需一个地址）：**

https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt

以上均为 `dist` 稳定通道的规则订阅，不含代理节点。自动构建只更新 `candidate` 候选通道，完成风险审核及设备验收后才更新稳定通道，详见 [维护指南](docs/maintenance.md)。

## 上游

| 项目 | 输入 | 输出 |
| --- | --- | --- |
| [AWAvenue 秋风](https://github.com/TG-Twilight/AWAvenue-Ads-Rule) | 官方 Clash Classical 和 AdGuard DNS 文件 | 各自原生格式 |
| [217heidai/adblockfilters](https://github.com/217heidai/adblockfilters) | `dist/adblockdns.txt`，含放行规则 | 两种格式 |
| [abclq/home-dns-adblock](https://github.com/abclq/home-dns-adblock) | `main/dist/adguard-dns-full.txt` 全量订阅 | 两种格式 |

[秋风订阅网页](https://awavenue.top/Sub.html?tool=clashClassical) 与其仓库属于同一来源。上游互有收录，合并后按匹配语义去重，不把条数相加当作独立覆盖。配置以 `config/sources.json` 为准。

每轮构建固定上游提交，保存原始输入、SHA-256 和 Git Blob SHA-1，可通过生成的 `SOURCES.md`、`report.json` 与 `sources/` 复核。哈希证明文件身份，不证明规则的业务安全性。Home DNS 的服务端保护也不会因订阅合并自动继承，具体策略见 [保护规则](docs/protection.md)。

## 本地构建

需要 Python 3.10+，无需第三方 Python 依赖，在项目根目录执行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules
```

输出到本地 `dist/`，该目录不提交到源码分支。修改规则、运行内核测试及发布步骤见 [维护指南](docs/maintenance.md)。

## 文档

| 文档 | 内容 |
| --- | --- |
| [使用指南](docs/usage.md) | 客户端配置和误拦排查 |
| [维护指南](docs/maintenance.md) | 构建、验证、候选发布、晋升及回滚 |
| [开发说明](docs/development.md) | 代码职责、数据流、测试和后续工作 |
| [保护规则](docs/protection.md) | 策略语义、采纳依据及风险边界 |
| [设备验收](docs/acceptance/README.md) | Linux 路由器验收步骤和记录格式 |

源码使用 [MIT](LICENSE)；合并规则保留上游 GPLv3 要求及 Home DNS 的 MIT 版权声明。完整许可见 [NOTICE.md](NOTICE.md) 和 `licenses/`。
