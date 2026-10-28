---
title: 'Markdown 样式指南'
pubDate: '2025-06-28'
---

本主题没有定义更多级别的标题。如有需要，你可以在 `src/styles/post.css` 中自行定义。

---

## 段落

下面是 Markdown 段落的一个实际示例。这段文字展示了内容在博客文章中自然流动的效果。

你可以在段落中使用各种格式，例如**粗体**、_斜体_、~~删除线~~，以及 `code`。

## 引用块

> Don't communicate by sharing memory, share memory by communicating.<br>
> — <cite>Rob Pike[^1]</cite>

[^1]: 以上引文摘录自 Rob Pike 在 2015 年 11 月 18 日 Gopherfest 上的[演讲](https://www.youtube.com/watch?v=PAAkCSZUG1c)。

### 有序列表

1. 第一项
2. 第二项
3. 第三项

### 无序列表

- 项目
  - 子项目
  - 子项目

## 任务列表

- [ ] 第一项
- [ ] 第二项
- [x] 第三项

## 图片

如需隐藏图片说明，可在其开头加上下划线 `_`，或将替代文本留空。

![HIKARI](./_assets/hikari.webp)

## 表格

| 样式     | 字重     | 其他   |
| -------- | -------- | ------ |
| 常规     | 常规     | 文本   |
| _斜体_   | **粗体** | `Code` |

## 代码块

```jsx
// Button.jsx

const Button = ({ text, onClick }) => {
  const [count, setCount] = useState(0)

  const handleClick = () => {
    setCount(count + 1)
    onClick?.()
  }

  return (
    <button className="btn" onClick={handleClick}>
      {text} ({count})
    </button>
  )
}
```

## 其他元素 —— sub、sup、abbr、kbd、mark

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

<abbr title="Graphics Interchange Format">GIF</abbr> 是一种位图图像格式。

按 <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd> 结束会话。

大多数<mark>蝾螈</mark>在夜间活动，捕食昆虫、蠕虫和其他小生物。

---
