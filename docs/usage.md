# 订阅使用指南

本文说明客户端配置。新版仍在本地、尚未部署；远端目前是旧直发流程。候选机制部署后，试用固定提交及配套 mihomo.pinned.yaml，通过审核和设备验收后才晋升稳定版。

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
