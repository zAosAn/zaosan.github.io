---
title: '主题指南'
pubDate: '2025-07-10'
tags: ['指南', 'Astro']
---

Chiri 是一个使用 [Astro](https://astro.build) 构建的极简博客主题，在保持简洁美学的同时提供多种自定义选项。

---

## 基本命令

- `pnpm new <title>` - 创建一篇新文章（标题前加 `_` 可创建草稿）
- `pnpm update-theme` - 将主题更新到最新版本

## 主要文件与目录

- `src/content/about/about.md` - 编辑首页的“关于”部分。若不想显示任何内容，请将其留空。
- `src/content/posts/` - 所有博客文章都存放在这里
- `src/config.ts` - 配置站点主要信息与设置

```ts
// Site Info
site: {
  website: 'https://chiri.the3ash.com/', // Site domain
  title: 'CHIRI', // Site title
  author: '3ASH', // Author name
  description: 'Minimal blog built by Astro', // Site description
  language: 'en-US' // Default language
},
```

```ts
// General Settings
general: {
  contentWidth: '35rem', // Content area width
  centeredLayout: true, // Use centered layout (false for left-aligned)
  themeToggle: false, // Show theme toggle button (uses system theme by default)
  postListDottedDivider: false, // Show dotted divider in post list
  footer: true, // Show footer
  fadeAnimation: true // Enable fade animations
},
```

```ts
// Date Settings
date: {
  dateFormat: 'YYYY-MM-DD', // Date format: YYYY-MM-DD, MM-DD-YYYY, DD-MM-YYYY, MONTH DAY YYYY, DAY MONTH YYYY
  dateSeparator: '.', // Date separator: . - / (except for MONTH DAY YYYY and DAY MONTH YYYY)
  dateOnRight: true // Date position in post list (true for right, false for left)
},
```

```ts
// Post Settings
post: {
  readingTime: false, // Show reading time in posts
  toc: true, // Show table of contents (when there is enough page width)
  imageViewer: true, // Enable image viewer
  copyCode: true, // Enable copy button in code blocks
  linkCard: true, // Enable link card
  katex: true // Enable KaTeX math rendering
}
```

## 文章 Frontmatter

只有 `title` 和 `pubDate` 是必填字段

```ts
---
title: 'Post Title'
pubDate: '2025-07-10'
---
```

## 语法高亮

你可以在 `astro.config.ts` 中通过 `shikiConfig` 配置主题。

更多详情：[语法高亮 | Astro 文档](https://docs.astro.build/en/guides/syntax-highlighting/)

```ts
import { defineConfig } from 'astro/config'

export default defineConfig({
  markdown: {
    shikiConfig: {
      light: 'github-light',
      dark: 'github-dark',
      wrap: false
    }
  }
})
```

---

## 部分功能预览

![主题切换](./_assets/theme-toggle.webp)

![点状分隔线](./_assets/dotted-divider.webp)

![左侧日期](./_assets/date-on-left.webp)

![目录](./_assets/toc.webp)

![阅读时长](./_assets/reading-time.webp)

![复制代码](./_assets/copy-code.webp)
