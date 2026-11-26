# 规则来源核对

每个文件固定到构建时的上游提交。SHA-256 对原始字节计算，可自行下载复核。新增与独有数量按完全相同的规范化规则统计，不代表新增域名覆盖范围。

## AWAvenue 秋风广告规则（Clash Classical）

- 项目：https://github.com/TG-Twilight/AWAvenue-Ads-Rule
- 实际下载：https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/8965815bf3978bdaccdd7a18ec694db67e14d5c1/Filters/AWAvenue-Ads-Rule-Clash-Classical.yaml
- 原始快照：[sources/awa-clash.txt](sources/awa-clash.txt)
- 上游提交：`8965815bf3978bdaccdd7a18ec694db67e14d5c1`
- SHA-256：`58a85bfdfccb48f7038bb520df4f5c67ffa44a79c0e14aa962777847a3614845`
- Git Blob SHA-1：`10dc8e692d84abea01320632a5bc2a992d689007`
- 解析结果：拦截 998 条，放行 0 条。
- clash：按来源顺序新增 998 条；与之前来源重复 0 条；最终保留 997 条；该来源独有 985 条。

独有规则示例：

```text
DOMAIN,1500020991.vodplayer.wxamedia.com
DOMAIN,1500022744.vodplayer.wxamedia.com
DOMAIN,1500026601.vodplayer.wxamedia.com
DOMAIN,8le8le.com
DOMAIN,8rn1y79f02-1.algolianet.com
DOMAIN,a0.app.xiaomi.com
DOMAIN,aaid.umeng.com
DOMAIN,abtest-ch.snssdk.com
DOMAIN,ad-api.4pyun.com
DOMAIN,ad-cdn.qingting.fm
```


## AWAvenue 秋风广告规则（AdGuard DNS）

- 项目：https://github.com/TG-Twilight/AWAvenue-Ads-Rule
- 实际下载：https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/8965815bf3978bdaccdd7a18ec694db67e14d5c1/AWAvenue-Ads-Rule.txt
- 原始快照：[sources/awa-dns.txt](sources/awa-dns.txt)
- 上游提交：`8965815bf3978bdaccdd7a18ec694db67e14d5c1`
- SHA-256：`9c7204be5180e33ed97d2f7b8dc9fc1b61e6aabdaafa149ed9165636294f7f7b`
- Git Blob SHA-1：`f1b2b2feff996920c151119252eb1197e550e248`
- 解析结果：拦截 982 条，放行 0 条。
- adguard：按来源顺序新增 982 条；与之前来源重复 0 条；最终保留 981 条；该来源独有 5 条。

独有规则示例：

```text
*-ad.sm.cn*
*-ad.video.yximgs.com*
*-ad.wtzw.com*
*-be-pack-sign.pglstatp-toutiao.com*
||proxy.advp.apple.com^
```


## 217heidai AdBlock DNS Filters

- 项目：https://github.com/217heidai/adblockfilters
- 实际下载：https://raw.githubusercontent.com/217heidai/adblockfilters/08c72d35e0b25c259d83aac5e55eb38bea2f0d3d/adblockdns.txt
- 原始快照：[sources/heidai-dns.txt](sources/heidai-dns.txt)
- 上游提交：`08c72d35e0b25c259d83aac5e55eb38bea2f0d3d`
- SHA-256：`d9505657be49bb3f24fc96991a8796a4c1815d41b99630bd0d4b400f870d8b76`
- Git Blob SHA-1：`bab4a38cd381d7e70244346334ba56c7bd620f1a`
- 解析结果：拦截 252252 条，放行 194 条。
- clash：按来源顺序新增 252243 条；与之前来源重复 9 条；最终保留 252218 条；该来源独有 251619 条。

独有规则示例：

```text
DOMAIN-SUFFIX,0--d.com
DOMAIN-SUFFIX,0-0.fr
DOMAIN-SUFFIX,0-02.net
DOMAIN-SUFFIX,0-btc.com
DOMAIN-SUFFIX,0-energy.com
DOMAIN-SUFFIX,0-tox.com
DOMAIN-SUFFIX,0.avmarket.rs
DOMAIN-SUFFIX,0.myikas.com
DOMAIN-SUFFIX,0.net.easyjet.com
DOMAIN-SUFFIX,0.nextyourcontent.com
```

- adguard：按来源顺序新增 251666 条；与之前来源重复 586 条；最终保留 252219 条；该来源独有 251604 条。

独有规则示例：

```text
||0--d.com^
||0-0.fr^
||0-02.net^
||0-btc.com^
||0-energy.com^
||0-tox.com^
||0.avmarket.rs^
||0.myikas.com^
||0.net.easyjet.com^
||0.nextyourcontent.com^
```


## abclq Home DNS Adblock（精确规则 + 上游全量）

- 项目：https://github.com/abclq/home-dns-adblock
- 实际下载：https://raw.githubusercontent.com/abclq/home-dns-adblock/d8e8f5b47e89b1ec3b3923917159861cc3173678/dist/adguard-dns-full.txt
- 原始快照：[sources/home-dns.txt](sources/home-dns.txt)
- 上游提交：`d8e8f5b47e89b1ec3b3923917159861cc3173678`
- SHA-256：`2de281f86a2c977dec3169d59ae2c2764311f184426038d10a4941d0b0d823f3`
- Git Blob SHA-1：`98bde2862bf79d75b69e3a52b302b923940f9363`
- 解析结果：拦截 1019 条，放行 0 条。
- clash：按来源顺序新增 417 条；与之前来源重复 602 条；最终保留 1019 条；该来源独有 417 条。

独有规则示例：

```text
DOMAIN-SUFFIX,a0.app.xiaomi.com
DOMAIN-SUFFIX,aaid.umeng.com
DOMAIN-SUFFIX,activity-ag.awemeughun.com
DOMAIN-SUFFIX,ad.doubleclick.net
DOMAIN-SUFFIX,ad.hpplay.cn
DOMAIN-SUFFIX,ad.player.baidu.com
DOMAIN-SUFFIX,ad.shenshiads.com
DOMAIN-SUFFIX,ad4.sina.com.cn
DOMAIN-SUFFIX,adc.hpplay.cn
DOMAIN-SUFFIX,adcdn.hpplay.cn
```

- adguard：按来源顺序新增 29 条；与之前来源重复 990 条；最终保留 1019 条；该来源独有 29 条。

独有规则示例：

```text
||activity-ag.awemeughun.com^
||aeventlog.beacon.qq.com^
||api.iegadp.qq.com^
||comfylink.com^
||dig.bdurl.net^
||dns.alidns.com^
||doh.pub^
||jomoxc.com^
||l2-toutiao-quic-ipv6-ml.gslb.ksyuncdn.com^
||log5-applog-lf.fqnovel.com^
```


