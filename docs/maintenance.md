# 维护说明

订阅地址与使用说明统一放在 [README](../README.md)。

## 配置

| 文件 | 用途 |
| --- | --- |
| `config/sources.json` | 上游地址、原生格式、目标格式及最低条数 |
| `config/blocklist.txt` | 本地 Classical 拦截规则 |
| `config/allowlist.txt` | 明确放行的 DOMAIN 或 DOMAIN-SUFFIX |
| `config/protection.json` | 全来源合并后的统一保护 |
| `config/validation.json` | 审核阈值、测试内核版本及包哈希 |
| `tests/scenarios.json` | 内核匹配场景 |

本地精确域名和后缀规则分别转换为 AdGuard 的 `|domain^` 和 `||domain^`；本地 IP 和关键字规则只进入 Mihomo。上游使用各自原生格式，未知语法停止构建。放行与保护的边界见 [保护策略](protection.md)。

## 构建与验证

需要 Python 3.10+，仅使用标准库。在仓库根目录执行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build.py --repository MaoLikeQvQ/Home-Adblock-Rules --output work/candidate
```

默认输出目录为 `dist/`。已有完整快照可通过 `--source-dir dist/sources` 离线重建，邻接 `report.json` 用于恢复版本并检查输入哈希。固定快照可复现，不代表上游最新状态。

验证前将稳定提交的完整文件导出到 `work/stable/`，包含规则、`report.json` 与 `sources/`，并记录完整提交 SHA：

```bash
python3 scripts/validate.py --candidate work/candidate --baseline work/stable
python3 scripts/smoke_engines.py --candidate work/candidate
python3 scripts/validate.py --candidate work/candidate --seal --baseline-commit STABLE_FULL_SHA
```

将 `STABLE_FULL_SHA` 换成实际基准提交。validate 返回 2 表示待审核，内核工具返回 3 表示环境未配置，1 表示失败。内核测试在临时目录和回环网络运行，不修改系统 DNS。修改规则、配置或源码后重新生成并验证，不复用旧报告。

## 发布

[Update subscriptions](https://github.com/MaoLikeQvQ/Home-Adblock-Rules/actions/workflows/update.yml) 每 8 小时运行，只有必要检查成功才更新 `candidate`；PR 只验证。`dist` 稳定版通过 **Promote or rollback stable rules** 手动晋升或回滚。

试用候选时使用完整提交 SHA；Mihomo 选择该提交的 `mihomo.pinned.yaml`，只加载一个规则提供者。新候选的 `clash.yaml` 已处理放行例外；`clash-allow.yaml` 仅保留作审计及旧配置兼容，无需单独订阅。旧稳定版在晋升前仍沿用双提供者配置。

当前晋升工具要求将候选审核记录提交到 `docs/acceptance/名称.json`。记录字段如下：

| 字段 | 要求 |
| --- | --- |
| `candidate_id` | 与候选 manifest 完全一致 |
| `reviewer`、`reviewed_on` | 实际审核者、ISO 日期 |
| `approved_findings` | 精确覆盖 validation 中全部 finding ID |
| `device` | 现有字段名，记录实际测试环境和内核版本，不影响规则生成 |
| `scenarios` | login、images、video、advertising 四项，每项有 `status: passed` 及真实 `evidence` |

不得用模板、模拟或内核受控测试冒充实际使用结果。记录只允许上述字段；格式以 `scripts/promote.py` 的 `verify_acceptance` 为准。

```bash
python3 scripts/promote.py promote --candidate-commit FULL_SHA --acceptance docs/acceptance/名称.json --dry-run
python3 scripts/promote.py rollback --release-commit PRIOR_RELEASE_SHA --reason '已确认的故障原因' --dry-run
```

实际发布需显式 `--apply` 和操作授权。晋升核对审核记录、内核结果、源码及配置指纹、稳定基准和产物哈希，只发布同一批产物，不重新拉取上游。基准变化时重新分析。

回滚追加提交，不强推；目标需为带完整发布记录的历史稳定版，迁移前的旧 dist 不满足该结构。发布后用 `scripts/check_remote.py` 核对固定提交的公开规则哈希，客户端另行刷新。

## 产物与存储

main 只保留源码、配置、测试、必要文档和正式审核记录。candidate/dist 保存生成规则及随版证据：

- `SOURCES.md`、`report.json`、`sources/`：固定版本、原始输入、构建源码及许可。
- `rules.jsonl.gz`、`decisions.json`：原文位置、来源归属和保护处理。
- `validation.json`、`VALIDATION.md`、`engines.json`、`manifest.json`：差异、审核项、内核结果和封存指纹。

日志与临时报告放在忽略的 `work/`、`artifacts/` 或 Actions 附件；附件保留 7 天，不作为唯一长期存档。
