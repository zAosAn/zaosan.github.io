---
title: '嵌入内容'
pubDate: '2025-06-06'
tags: ['指南']
---

使用以下指令嵌入媒体：

```
::link{url="https://xxxxx.xxx"}

::spotify{url="https://open.spotify.com/type/xxxxx"}

::youtube{url="https://www.youtube.com/watch?v=xxxxx"}

::bilibili{url="https://www.bilibili.com/video/xxxxx"}

::github{repo="username/repo"}

::x{url="https://x.com/username/status/xxxxx"}

::neodb{url="https://neodb.social/category/xxxxx"}
```

```
🟡

When embedded content is still loading,
the table of contents positioning may be inaccurate.
```

## 链接卡片

::link{url="https://pitchfork.com/reviews/albums/ichiko-aoba-luminescent-creatures/"}

```
🟡

Link Card metadata is fetched automatically during `pnpm dev` and `pnpm build`.
Run `pnpm update-link-metadata --force` to refresh existing entries.

-

To disable Link Card, set `linkCard: false` in `src/config.ts`.
Restart `pnpm dev` for the change to take effect.
```

## Spotify

::spotify{url="https://open.spotify.com/track/41Y0ch6R3jzpJOZv6nhf9Z?si=6c82dbed65ab4853"}

::spotify{url="https://open.spotify.com/album/1kBPEN3NIVwjdmIjjNk9vB?si=Lz29MvjwRnKX9y3dhxlbaQ"}

## YouTube

::youtube{url="https://www.youtube.com/embed/GlhV-OKHecI?si=KdB4rRPLAMEK-ozf"}

## BiliBili

::bilibili{url="https://www.bilibili.com/video/BV1Vm421W7pX/?vd_source=c0bc2746a6d2b23de50d26376498b2ff"}

## GitHub

::github{repo="the3ash/astro-chiri"}

## X 帖子

::x{url="https://x.com/DAVID_LYNCH/status/1174367510893752321"}

## NeoDB（仅限中国）

::neodb{url="https://neodb.social/album/5nD3R8gmnVlsoOBdyO8PA3"}

::neodb{url="https://neodb.social/movie/1bhogjXkNnlWWM0bf6aj8P"}

::neodb{url="https://neodb.social/book/4BqQ5mhfKMHPND3L6hf0Qh"}

::neodb{url="https://neodb.social/game/1hl18l0qD5UN93k8ZkCZ7Q"}
