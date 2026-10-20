name: 方案上架 / 更新
about: 提交或更新 qxbgm/v1 方案的注册条目
title: "[方案] <方案名> v<版本>"
labels: scheme
body:
  - type: input
    id: scheme-id
    attributes:
      label: 方案 ID
      description: 与 index/ 下文件名一致（字母数字连字符）
      placeholder: touhou-8bit-youkai-komachi
    validations:
      required: true
  - type: input
    id: repo
    attributes:
      label: 发布者仓库地址
      description: 存放 manifest 与音频的仓库
    validations:
      required: true
  - type: textarea
    id: notes
    attributes:
      label: 方案说明
      description: 内容、适用奇域、曲目清单、授权说明
    validations:
      required: true
  - type: checkboxes
    id: checklist
    attributes:
      label: 提交前自检
      options:
        - label: index/<id>.json 通过 ci/validate.py 本地校验（含联网检查）
          required: true
        - label: 音频 URL 为 https 且可公开下载
          required: true
        - label: 大文件均填写了 sha256
          required: true
        - label: 方案为纯数据（不含可执行内容），音频为本人有权分享的内容
          required: true
