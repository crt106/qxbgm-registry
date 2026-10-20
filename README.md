# qxbgm-registry — 千星BGM方案索引仓库（P0）

qxbgm/v1 方案的**中心化索引仓库**。发现与管理在这里，音频与 manifest 在各发布者自己的仓库。
设计文档见 `docs/QXBGM_REGISTRY.md`（th01_BeyondLocal 项目内）。

## 上架流程（PR）

1. 在自己的仓库维护方案（manifest + 音频/Releases 附件），确保 `audio.uri` 可公开下载（https）。
2. Fork 本仓库，在 `index/` 下添加 `<scheme-id>.json` 注册条目（格式见 `registry.schema.md` 或既有示例）。
3. 提交 PR：CI 自动校验（schema、URL 可达、sha256 一致），维护者人工过目后合并即上架。

## 条目模板

```jsonc
{
  "registry": "qxbgm-registry/v1",
  "id": "<scheme-id，与文件名一致>",
  "name": "显示名",
  "author": "gitee:<用户名>",
  "description": "……",
  "tags": ["touhou", "8bit"],
  "category": "音乐包",
  "version": "1.0.0",
  "updatedAt": "2026-10-20",
  "wonderland": { "id": "可选", "name": "可选" },
  "manifest": { "url": "https://…/scheme.qxbgm.json", "sha256": "可选" },
  "package":  { "url": "https://…/pack.qxbgmzip", "sha256": "可选", "size": 0 },
  "tracks": 1,
  "minAppVersion": "1.0.0"
}
```

`manifest` 与 `package` 至少提供一个；都提供时 App 优先整包（免编码）。
