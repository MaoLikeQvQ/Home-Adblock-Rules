# 候选验证报告

状态：review-required

设备验收：未完成。实际内核结果见 engines.json。

## 审核项

### impact-a9185f2d4867f333

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.sm.cn`
- 来源：awa-clash，sources/awa-clash.txt:1007
- gecko-service：`probe-ad.sm.cn.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.sm.cn.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.sm.cn.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-0082db7e5e882fb3

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.video.yximgs.com`
- 来源：awa-clash，sources/awa-clash.txt:1008
- gecko-service：`probe-ad.video.yximgs.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.video.yximgs.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.video.yximgs.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-dbd8efd29647f375

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-ad.wtzw.com`
- 来源：awa-clash，sources/awa-clash.txt:1009
- gecko-service：`probe-ad.wtzw.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.wtzw.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.wtzw.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-b153447f90355ff4

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：clash
- 规则：`DOMAIN-KEYWORD,-be-pack-sign.pglstatp-toutiao.com`
- 来源：awa-clash，sources/awa-clash.txt:1010
- gecko-service：`probe-be-pack-sign.pglstatp-toutiao.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-be-pack-sign.pglstatp-toutiao.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-be-pack-sign.pglstatp-toutiao.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-5d5d95388b56e77a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,111.20.26.186/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:13
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-d124d4898fd8e189

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,112.84.130.73/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:14
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-dfd3b325acb20d08

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,116.142.251.100/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:15
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-378df5d643363f35

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,116.177.251.215/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:16
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-0ccd30ef7d5ace26

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,120.77.173.114/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:17
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-212ab678a2830d83

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,123.56.23.22/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:18
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-6e875846585264aa

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.160/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:19
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-1b9db71a2b48199a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.168/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:20
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-5e66fb371ad71cc3

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,14.29.101.169/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:21
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-1a79e533d8631f04

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,182.254.116.116/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:22
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-f56141b995daac45

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,203.205.137.89/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:23
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-a51869ec69d8467a

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,218.77.192.51/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:24
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-06589875c3f1fab0

Destination IP can affect protected traffic; domain policy alone cannot prove separation

- 目标：clash
- 规则：`IP-CIDR,38.190.225.166/32,no-resolve`
- 来源：awa-clash，sources/awa-clash.txt:25
- 待核对：路由器连接目标 IP 与实际命中规则；no-resolve 不代表绝不会影响域名连接。

### impact-4ced1257045e303a

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.sm.cn*`
- 来源：awa-dns，sources/awa-dns.txt:993
- gecko-service：`probe-ad.sm.cn.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.sm.cn.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.sm.cn.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-7499d33337faa518

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.video.yximgs.com*`
- 来源：awa-dns，sources/awa-dns.txt:994
- gecko-service：`probe-ad.video.yximgs.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.video.yximgs.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.video.yximgs.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-863c64916b43c713

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-ad.wtzw.com*`
- 来源：awa-dns，sources/awa-dns.txt:995
- gecko-service：`probe-ad.wtzw.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-ad.wtzw.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-ad.wtzw.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）

### impact-078083ab522df9cb

Pattern can intersect protected suffixes; synthetic witnesses are not real app evidence

- 目标：adguard
- 规则：`*-be-pack-sign.pglstatp-toutiao.com*`
- 来源：awa-dns，sources/awa-dns.txt:996
- gecko-service：`probe-be-pack-sign.pglstatp-toutiao.com.gecko.snssdk.com`（合成样例，不是实机请求）
- risk-control：`probe-be-pack-sign.pglstatp-toutiao.com.is.snssdk.com`（合成样例，不是实机请求）
- xiaomi-service：`probe-be-pack-sign.pglstatp-toutiao.com.tz.sec.xiaomi.com`（合成样例，不是实机请求）


完整变更见 validation.json，处理与原文位置见 decisions.json、rules.jsonl.gz。
