# 设备验收记录

先提交与固定候选绑定的 JSON，再由维护者手动运行稳定工作流。禁止把模板当测试结果。

```json
{
  "candidate_id": "从 manifest.json 复制完整 ID",
  "reviewer": "实际审核者",
  "reviewed_on": "2026-11-26",
  "approved_findings": [],
  "device": "设备/系统/App/内核版本",
  "scenarios": {
    "login": {
      "status": "pending",
      "evidence": "待执行真实场景"
    },
    "images": {
      "status": "pending",
      "evidence": "待执行真实场景"
    },
    "video": {
      "status": "pending",
      "evidence": "待执行真实场景"
    },
    "advertising": {
      "status": "pending",
      "evidence": "待执行真实场景"
    }
  }
}
```

approved_findings 必须精确对应 validation.json 所有 finding ID；发布授权来自维护者手动工作流，而不是 JSON 自行授予。所有必测场景需 passed 并附真实证据，否则拒绝晋升。支付、推送、更新等额外功能另附测试说明，基础四项不代表覆盖这些功能。


## Linux 路由器 Mihomo 验收

先读取环境，不安装新服务或改系统 DNS：

```sh
uname -srm
command -v mihomo
mihomo -v
```

若使用 OpenClash、ShellCrash 等管理且内核不在 PATH，先确认实际路径和配置位置。没有确认服务管理方式时，不覆盖配置或盲目重启。

1. 备份当前配置、配套规则及版本，明确恢复方式。
2. 选择固定候选，将同版提供者和逻辑规则合并进现有配置；保留原代理节点与正常分流。
3. 用现有内核检查配置，确认支持 AND/NOT/RULE-SET，再按原有管理方式加载。
4. 从控制器或日志核对配套规则、版本和命中；不输出控制器密钥或全量家庭请求。
5. 在连接路由器的设备上执行登录、图片、正常播放、广告等场景，补充实际需要的支付、推送和更新。
6. 检查 CPU/内存及加载耗时，发生异常时做窄范围放行对照；保留未执行项，不以观察时间替代测试。

不能运行隔离内核时，容器或 CI 负责受控测试，路由器负责部署兼容性、资源和真实业务，两种证据分开。恢复配置后还需确认规则刷新及缓存，不能声称回滚会立即清掉客户端缓存。
