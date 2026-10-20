# 上架指南（发布者完整流程）

本指南面向想把 BGM 方案分享给其他人的发布者。使用者不需要本指南，
在 QxBgmManager 方案市场页把索引源设为本仓库即可。

## 0. 前置

- 安装 QxBgmManager（完成环境检查全部通过）。
- 有 GitHub 账号（或 Gitee，链路相同）。

## 1. 制作方案

方式 A（推荐，导出）：
1. 在 QxBgmManager 替换中心完成曲目替换（编码+打入补丁）。
2. 方案管理页「导出方案」，填 id/名称/作者/描述，得到 `<id>.qxbgmzip`。

方式 B（手写 manifest）：
- 按 `docs/QXBGM_SCHEME.md`（qxbgm/v1）写 `.qxbgm.json`；
  音频 `kind=raw`（接收方编码）或 `kind=wem`（你预先编码好，推荐）。

## 2. 托管 manifest 与音频

1. 建一个自己的公开仓库（如 `qxbgm-schemes-<你的名字>`）。
2. 提交 `schemes/<id>.qxbgm.json`；音频文件两种放法：
   - 小文件直接入库（`audio/…`，manifest 里 `uri` 写相对路径 `audio/xx.wem`）；
   - 大文件/整包放 **Releases** 附件，`uri` 或索引条目的 `package.url` 写附件 https 地址。
3. 建议为 manifest 与大文件计算 sha256 填入（`certutil -hashfile <文件> SHA256` 或 `sha256sum`）。

## 3. 向索引仓库 PR

1. Fork `crt106/qxbgm-registry`。
2. 在 `index/` 新增或更新 `<scheme-id>.json`（模板见 README 或既有条目）。
3. 本地跑 `python ci/validate.py`（联网校验 URL 与 sha256），0 错误再提交。
4. 提 PR，按模板填自检清单。维护者过目后合并即上架。

## 4. 迭代与下架

- 改曲子/修 bug：更新自己仓库 → 更新索引条目 `version`/`updatedAt` → PR。
  使用者刷新市场页会看到「可升级」。
- 下架：PR 删除对应 `index/<id>.json`（已安装的使用者不受影响，可手动卸载）。

## 5. 内容规范

- 只分享你**有权分享**的音频（原创、CC 授权、官方明确允许的二创）。
- 方案必须是纯数据：不得包含脚本、可执行文件或指向可执行内容的链接。
- 单个方案建议 ≤ 20 轨；音频总量建议 ≤ 200MB（超出请拆包）。
