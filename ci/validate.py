# qxbgm-registry 注册条目 CI 校验脚本
# 用法: python ci/validate.py            # 校验 index/ 全部条目
#       python ci/validate.py --no-net   # 只校验 schema，不做网络可达性检查
import hashlib
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_DIR = os.path.join(ROOT, "index")
REQUIRED = ["registry", "id", "name", "author", "version", "updatedAt", "tracks"]
ERRORS = []
WARNINGS = []


def err(f, msg):
    ERRORS.append(f"{os.path.basename(f)}: {msg}")


def warn(f, msg):
    WARNINGS.append(f"{os.path.basename(f)}: {msg}")


def head_ok(url, expect_sha256=None):
    try:
        req = urllib.request.Request(url, method="GET",
                                     headers={"User-Agent": "qxbgm-ci"})
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
        if expect_sha256:
            digest = hashlib.sha256(body).hexdigest()
            if digest != expect_sha256.lower():
                return f"sha256 不符 (期望 {expect_sha256[:12]}… 实际 {digest[:12]}…)"
        return None
    except Exception as e:
        return f"不可达: {e}"


def validate_entry(path, check_net):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        err(path, f"JSON 解析失败: {e}")
        return
    for k in REQUIRED:
        if k not in d:
            err(path, f"缺少必填字段 {k}")
    if d.get("registry") != "qxbgm-registry/v1":
        err(path, f"registry 版本未知: {d.get('registry')}")
    if d.get("id") != os.path.splitext(os.path.basename(path))[0]:
        err(path, f"id {d.get('id')} 与文件名不一致")
    if not isinstance(d.get("tracks"), int) or d["tracks"] < 1:
        err(path, "tracks 必须为正整数")
    for part in ("manifest", "package"):
        if part not in d:
            continue
        u = d[part].get("url", "")
        if not u.startswith("https://"):
            if os.path.exists(u):
                warn(path, f"{part}.url 为本地路径（P0 模式，上架前须改为 https）: {u[:60]}")
            else:
                err(path, f"{part}.url 必须是 https 或存在的本地路径: {u[:60]}")
            continue
        if check_net:
            r = head_ok(u, d[part].get("sha256"))
            if r:
                err(path, f"{part}.url {r}")
    if "manifest" not in d and "package" not in d:
        err(path, "manifest 与 package 至少提供一个")
    if not isinstance(d.get("tags", []), list):
        warn(path, "tags 应为数组")
    wid = (d.get("wonderland") or {}).get("id")
    if wid is not None and not str(wid).isdigit():
        warn(path, f"wonderland.id 非纯数字: {wid}")


def main():
    check_net = "--no-net" not in sys.argv
    files = sorted(
        os.path.join(INDEX_DIR, f) for f in os.listdir(INDEX_DIR) if f.endswith(".json")
    )
    if not files:
        print("index/ 为空，无条目可校验")
        sys.exit(1)
    for f in files:
        validate_entry(f, check_net)
    for w in WARNINGS:
        print(f"WARN  {w}")
    for e in ERRORS:
        print(f"ERROR {e}")
    print(f"\n{len(files)} 条目, {len(ERRORS)} 错误, {len(WARNINGS)} 警告")
    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
