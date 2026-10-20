# 多仓库组织与协同

千星BGM替换体系由三个（类）仓库组成，职责单一、单向依赖：

```
┌──────────────────────────────┐
│ crt106/QxBgmManager          │  App 源码（WPF 桌面应用）
│  - 应用代码、编码器、自测      │
│  - 不含任何共享配置/曲库数据    │
└──────────────┬───────────────┘
               │ 启动/刷新时拉取（克隆或浅读）
               ▼
┌──────────────────────────────┐
│ crt106/qxbgm-registry        │  中心化枢纽
│  index/   方案注册条目（PR 上架）│
│  config/  共享配置             │
│    ├─ track-map.json  曲名映射 │
│    └─ app-config.json 预设/书签 │
└──────────────┬───────────────┘
               │ index 条目指向 manifest/包
               ▼
┌──────────────────────────────┐
│ 发布者仓库（各自维护）          │
│  crt106/qxbgm-schemes-touhou8bit … │
│  schemes/*.qxbgm.json + 音频   │
└──────────────────────────────┘
```

## 配置流向（哪些东西住在 registry）

| 配置 | registry 位置 | App 消费点 | 本地回退 |
|---|---|---|---|
| 曲名映射（188轨） | `config/track-map.json` | 曲库页/替换中心/环境检查 | 研究目录副本 → 内置种子 |
| 编码预设（normal/chiptune-6k…） | `config/app-config.json` presets | 替换中心/编码转换页 | 内置两条 |
| 默认书签 | `config/app-config.json` bookmarks | 奇域浏览页 | 内置五条 |
| 已知游戏安装路径 | `config/app-config.json` knownGameRoots | 设置页自动探测 | 注册表探测 |
| 编码器参数（采样率/束宽） | `config/app-config.json` encoder | 编码服务默认值 | 内置常量 |
| 最低 App 版本 | `config/app-config.json` + 条目 minAppVersion | 市场页安装门槛 | — |

原则：**所有"会随生态演进、与代码无关"的数据都放 registry**；App 源码仓库不携带任何曲库数据。

## 版本契约

- 索引条目格式：`qxbgm-registry/v1`（破坏性变更升版本号，App 拒绝未知版本并提示升级 App）。
- 方案格式：`qxbgm/v1`（见 QxBgmManager 仓库 docs/QXBGM_SCHEME.md）。
- 条目 `minAppVersion`：App 版本低于要求时安装被拦截并提示。
- App 对未知字段一律忽略（前向兼容），registry 可自由加字段。

## 发布者仓库自治

- 结构自由（推荐 `schemes/` + `audio/` + Releases），registry 只登记 manifest/package URL。
- 发布者用 git 管理自己的方案迭代与奇域关联；上架/更新/下架都通过对 registry 的 PR。
- 想自己跑一个平行索引？fork 本仓库改远端即可，App 索引源是可配置项。
