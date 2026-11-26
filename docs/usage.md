# 订阅使用指南

以下是 `dist` 稳定通道的订阅地址。它们是规则集，不含代理节点。

## Mihomo / Clash Meta 用法

| 文件 | 地址 |
| --- | --- |
| 拦截规则 | https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash.yaml |
| 放行例外（白名单） | https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/clash-allow.yaml |

`clash-allow.yaml` 保存上游要求放行的域名，本来就不含拦截规则。当前输出将黑名单和白名单分开；不是让客户端同时加载两套拦截规则，也不能把白名单设为 REJECT。

将 [Mihomo 配置片段](https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/mihomo.example.yaml) 合并到现有配置。两个提供者都用 `behavior: classical`、`format: yaml`，通过片段中的逻辑规则拦截“命中黑名单且不在白名单”的连接。已有 `rule-providers:` 或 `rules:` 时合并其中的条目，不要重复顶层键；将广告逻辑规则放在广泛匹配规则和 `MATCH` 前面。

白名单继续走后面的正常分流。只添加拦截集会丢失上游的例外保护。

推荐使用 Mihomo 内核（Clash Meta）。不支持 `AND` / `NOT` / `RULE-SET` 组合的旧 Clash 内核需要升级；本项目没有对旧 Clash 内核完成兼容验证。

## AdGuard Home 用法

进入“过滤器 → DNS 封锁清单 → 添加拦截列表 → 添加自定义列表”，填写：

https://raw.githubusercontent.com/MaoLikeQvQ/Home-Adblock-Rules/dist/adguard.txt

AdGuard DNS 或支持 DNS 过滤语法的 AdGuard 客户端也可以使用该文件。`@@` 放行规则已经合并在同一订阅中，不需要再单独添加白名单订阅。浏览器元素隐藏与脚本过滤不在这份 DNS 规则的范围内。

## 本机临时试用

在项目目录生成规则后运行：

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory dist
```

同机客户端可以使用 `http://127.0.0.1:8080/adguard.txt`，Mihomo 则替换两个提供者的对应 URL。回环地址仅供本机使用，关闭终端后服务停止。

## 误拦排查

1. 记录订阅版本、客户端、App、触发动作和异常表现。
2. 从 Mihomo 连接记录或 AdGuard Home 查询日志查找命中的规则。
3. 针对命中的具体域名临时放行，对照异常是否恢复。
4. 将复现步骤、命中规则、来源和恢复情况交给维护者；删除账号、Token、带身份参数的 URL 等隐私信息。

DNS 本来无法解析、代理节点故障、缓存广告等情况不能仅凭现象归因于规则。查看 [维护指南](maintenance.md) 了解如何补规则；候选试用、晋升与回滚见 [维护指南](maintenance.md)。
