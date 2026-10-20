<div align="center">

# 🗃️ qxbgm-registry — 千星BGM方案索引仓库

**QxBgmManager 方案的中心化发现、审核与共享配置仓库。**
零自建服务器 · git 原生 · PR 即上架

[![Validate](https://img.shields.io/badge/entries-validated-brightgreen)](ci/validate.py)
[![License](https://img.shields.io/badge/license-CC0-green)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange)](../../pulls)

</div>

---

## 这是什么

千星奇域 BGM 替换方案（[qxbgm/v1 格式](https://github.com/crt106/QxBgmManager/blob/main/docs/QXBGM_SCHEME.md)）的
**中心化索引**。本仓库不存音频，只做三件事：

1. **发现**：`index/` 下每个方案一条注册条目，App 方案市场页从这里拉取
2. **审核**：fork + PR 上架，CI 自动校验（schema / URL 可达 / sha256 一致），维护者人工过目
3. **共享配置**：`config/` 下托管 App 的公共配置（曲名映射、编码预设、书签等），全生态同步

## 🚀 使用者（不需要本仓库的任何操作）

打开 [QxBgmManager](https://github.com/crt106/QxBgmManager) → 设置页确认索引源为
`https://github.com/crt106/qxbgm-registry.git`（默认即是）→ 方案市场页浏览安装。

## 📦 发布者（上架你的方案）

完整流程见 **[docs/PUBLISHING.md](docs/PUBLISHING.md)**。速览：

```
你的仓库（manifest + 音频/Releases）
        │  fork + PR 一条 index/<id>.json
        ▼
本仓库 CI 校验 → 维护者合并 → 上架，App 用户立即可见
```

## 🗂️ 仓库结构

```
index/            # 方案注册条目（每方案一个 <id>.json，PR 入口）
config/
  track-map.json  # 官方 188 轨 ↔ fileID/曲名/分类 映射（音频指纹+时长匹配构建）
  app-config.json # App 共享配置：编码预设、书签、已知游戏路径、音频参数
ci/validate.py    # 条目校验（schema + URL 可达 + sha256 + wonderland 格式）
docs/             # 上架指南等
.github/          # PR 模板、议题表单、Actions 工作流
```

## 📋 当前收录

| 方案 | 作者 | 版本 | 曲目 | 关联奇域 |
|---|---|---|---|---|
| [東方妖怪小町 (8bit)](index/touhou-8bit-youkai-komachi.json) | crt106 | 1.0.0 | 1 | 科研存档 |
| [竹取飛翔 ～ Lunatic Princess (8bit)](index/touhou-8bit-taketori-lunatic-princess.json) | crt106 | 1.0.0 | 1 | 科研存档 |

## 🧩 仓库生态

| 仓库 | 作用 |
|---|---|
| [QxBgmManager](https://github.com/crt106/QxBgmManager) | App 源码（WPF 桌面应用） |
| **qxbgm-registry**（本仓库） | 方案索引 + 共享配置 |
| [qxbgm-schemes-touhou8bit](https://github.com/crt106/qxbgm-schemes-touhou8bit) | 发布者仓库示例 |

## ⚠️ 声明

本仓库仅包含方案元数据与配置，不含任何游戏原始资产。
使用本索引中的方案进行本地资产替换的相关风险由使用者自行承担（详见 App 仓库声明）。

## 📄 许可

[CC0](https://creativecommons.org/public-domain/cc0/)（索引与配置数据）。
