# 构建、验证与发布

定时任务只更新 candidate 候选，稳定版 dist 由人工验收后晋升。源码推送不代表构建成功或稳定规则已更新；运行结果以 [GitHub Actions](https://github.com/MaoLikeQvQ/Home-Adblock-Rules/actions/workflows/update.yml) 和实际发布提交为准。

## 修改规则

| 文件 | 用途 |
| --- | --- |
| `config/sources.json` | 必需来源、原生格式、目标客户端和最低条数 |
| `config/blocklist.txt` | 本地 Classical 拦截规则 |
| `config/allowlist.txt` | 明确放行的 DOMAIN 或 DOMAIN-SUFFIX |
| `config/protection.json` | 合并后统一保护及例外 |
| `config/validation.json` | 审核阈值、固定内核和 SHA-256 |
| `tests/scenarios.json` | 各客户端的匹配预期与必测场景 |

拦截可以写 `DOMAIN,ads.example.com`、`DOMAIN-SUFFIX,tracker.example.net` 或支持的 IP/关键字规则。IP 和关键字只进入 Mihomo；精确/后缀分别转换为 AdGuard 的 `|domain^` 和 `||domain^`。

放行与原生例外合并，对所有来源生效。保护范围与广告例外须按 [保护规则](protection.md) 维护，不用父域全局白名单替代复杂例外。修改秋风为纯广告版本，并不能保证另外两家来源也移除了隐私或不受欢迎规则。

## 本地构建与离线复现

在项目根目录运行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules --output work/candidate
```

不指定 `--output` 时写入本地 `dist/`。生成文件、测试结果和内核缓存不提交到 main。

已有快照可以离线重建：

```bash
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules --source-dir dist/sources --output work/candidate
```

`--source-dir` 的文件名为 `<source-id>.txt`，邻接 `report.json` 用于恢复版本和校验输入哈希。发布快照的 `sources/` 中同时保存全部必要代码、配置和场景，可在该目录运行保存的构建入口，并选择独立输出。离线复现不代表验证了上游最新版本。

## 验证候选

准备完整稳定基准到 `work/stable/`，包括规则、`report.json` 和 `sources/`；记录对应的稳定提交，不能只复制旧统计或用另一轮候选替代。分别执行：

```bash
python3 scripts/validate.py --candidate work/candidate --baseline work/stable
python3 scripts/smoke_engines.py --candidate work/candidate
python3 scripts/validate.py --candidate work/candidate --seal --baseline-commit STABLE_FULL_SHA
```

将 `STABLE_FULL_SHA` 换成基准的完整提交。封存必须在本轮报告和内核检查完成后进行；规则、代码或配置变化后重新构建和验证，不给旧结果重新贴标签。

validate 返回 2 表示待审核，内核工具返回 3 表示平台或必要环境未配置；1 为失败，0 为相应自动检查通过。设备验收独立完成，不能用退出码 0 代替。

检查生成的文件：

| 文件 | 内容 |
| --- | --- |
| `SOURCES.md`、`report.json`、`sources/` | 固定来源、哈希、原始输入与源码 |
| `rules.jsonl.gz`、`decisions.json` | 完整原文位置及保护决定 |
| `validation.json`、`VALIDATION.md` | 稳定差异、审核项和未完成项 |
| `engines.json` | 固定内核及真实匹配结果 |
| `manifest.json` | 文件、源码、配置指纹与候选 ID |

内核测试使用临时目录和回环网络。官方包哈希不符、输出被修改、配置与快照不一致、必要场景缺失或执行失败均不通过。已配置 Linux amd64、macOS arm64；其他架构不能推断为兼容。

## 候选与稳定通道

新版 update 工作流在北京时间约 00:23、08:23、16:23 运行；调度可能延迟。PR 只验证，main 的构建通过必要检查后才发布 candidate。待审核候选可供明确标记的试用，失败或未完成的必要检查不更新可用候选。

每个候选用不可变提交定位，试用优先使用同版 `mihomo.pinned.yaml`；不要在测试期间一直跟随可变 candidate 分支。Mihomo 两个提供者独立刷新，可变 URL 不保证客户端同时更新。

## 手动晋升与回滚

按 [设备验收](acceptance/README.md) 完成真实场景，提交 `docs/acceptance/名称.json`。维护者手动运行 **Promote or rollback stable rules**，填写完整候选提交与验收路径。

本地预检默认不写远端：

```bash
python3 scripts/promote.py promote --candidate-commit FULL_SHA --acceptance docs/acceptance/名称.json --dry-run
python3 scripts/promote.py rollback --release-commit PRIOR_RELEASE_SHA --reason '已确认的故障原因' --dry-run
```

实际发布需显式 `--apply` 和操作授权。晋升核对逐项审核、设备证据、内核结果、源码/配置、稳定基准及产物哈希，只拷贝已测规则，不重新拉取上游。稳定基准已变化时拒绝晋升，需重新分析累计变化。

回滚用追加提交恢复旧字节，不强推。工具要求目标是带完整清单、发布及验收记录的历史稳定版；迁移前的 legacy dist 不满足此结构，需要另行保留其固定提交作为人工恢复依据。

发布后检查固定提交 Raw 文件哈希。缓存或网络导致无法确认时如实报告，不自动声称已生效或已回滚；客户端仍需刷新。失败、审核和回滚记录不能补写成完整测试通过。

## 存储约定

main 保留代码、配置、测试、必要文档及正式验收记录。规则与随版证据由 candidate/dist 分支保存；一次性日志、历史 JSON、调试产物写本地 `work/`、`artifacts/` 或 Actions 附件。Actions 附件保留 7 天，不能作为唯一长期版本存档。
