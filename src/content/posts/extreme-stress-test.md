---
title: '极端测试：超长标题、海量目录、复杂排版与性能压力'
pubDate: '2026-10-29'
---

这是一篇专门用来压测博客模板边界情况的文章：它同时包含超长标题、几十个层级的目录项、重复标题、超长中文与英文标题、超长无空格字符串、宽表格、深层嵌套列表、嵌套引用、超长代码行、数学公式、脚注、折叠块以及大段中英文混排正文。它的存在不是为了阅读，而是为了让目录、遮罩、滚动高亮、排版和构建流程在极端输入下暴露问题。

文章会故意制造一些在真实写作中很少出现、但一旦出现就很容易破坏布局的组合。例如：连续多个没有正文的标题、名称完全相同的多个章节、长度接近侧栏宽度的标题、需要横向滚动的表格，以及一行几百个字符的代码。所有这些内容都应该保持可渲染、可折叠、可定位，并且不会让目录的悬浮展开层失去可读性。

## 目录压力测试：一个非常非常长的中文标题用于验证侧栏在极端长度下的截断、悬浮展开与行距表现

这一节用于观察超长标题在 26rem 展开面板中的截断行为。标题越长，省略号越早出现；如果目录项超过两行，不应该撑破面板，也不应该覆盖相邻行。

### 第三级标题：用于验证 h3 是否会正确进入目录

正文只放一句话，用来确认 h3 的行高、横线与高亮状态是否与 h2 一致。

## 重复标题

第一次出现，用于验证重复标题的 slug 去重。

## 重复标题

第二次出现，预期 id 会带上 `-1` 后缀。

## 重复标题

第三次出现，预期 id 会带上 `-2` 后缀。

## 2026

纯数字标题，用于验证数字 slug。

## A/B 测试：斜杠、括号（全角）、引号“测试”、省略号……

标点符号密集的标题，用于验证 slug 过滤后仍然能得到稳定的 id。

## 🚀 Emoji 与符号测试：→ ★ ♥ ① ② ③

包含 emoji 与特殊符号的标题，预期 slug 只保留中文、英文和数字。

## Supercalifragilisticexpialidocious-And-Then-Some-More-Words-To-Make-This-Heading-Absurdly-Long

一个很长的英文标题，用于验证不换行时的省略与展开态宽度。

## 连续标题测试一

## 连续标题测试二

## 连续标题测试三

连续三个没有正文的标题，用于验证目录高度与滚动高亮在空章节之间的表现。

## 超长正文段落

下面是一段刻意拉长的中文正文，用于观察行高、段落间距、标点悬挂以及阅读宽度。这里的文字会重复一些结构，但每句话都尽量保持语义完整，避免变成无意义的占位符。长段落的主要风险不是渲染失败，而是排版节奏变得松散，读者很难在密集的文字中定位段落边界。为了模拟真实的长文，这一段会持续较长时间，并在中途插入英文、数字、行内代码与链接。

当文章变得很长时，目录的当前位置高亮会不断变化。滚动时的 `requestAnimationFrame` 节流、标题位置的 `getBoundingClientRect()` 计算、以及 `activeOffset` 的判定都会受到影响。如果标题数量过多，滚动事件仍然应该保持流畅；如果某个标题恰好位于视口顶部附近，高亮不应该在相邻两项之间反复跳动。为了测试这一点，后面的章节会安排得比较密集。

这一段还会包含一个很长的链接：<https://example.com/a/very/long/path/that/keeps/going/with/many/segments/and-query-parameters?utm_source=stress-test&utm_medium=article&utm_campaign=extreme-layout&ref=zaosan.github.io>，以及一个超长无空格字符串：`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`。

## 超长英文段落

This paragraph exists to stress the typographic rhythm of a very long English block inside a Chinese-first layout. It mixes several sentence lengths, parenthetical remarks (like this one), em dashes — which are common in translated text — and inline code such as `getBoundingClientRect()` and `astro:before-swap`. The paragraph should wrap cleanly, keep a comfortable measure, and never overflow the content column even when a single token is unusually long.

It also contains a deliberately unbroken token: `abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz` to verify `overflow-wrap: break-word` behavior. In a narrow window this token should break instead of forcing horizontal scrolling. The rest of the paragraph continues with ordinary prose so that the line-breaking algorithm has to handle both extreme and normal cases in the same block.

## 列表压力测试

### 无序列表与嵌套

- 第一层项目
  - 第二层项目
    - 第三层项目
      - 第四层项目
        - 第五层项目
- 另一个第一层项目，后面跟着一段较长的说明文字，用来观察项目符号与文本之间的间距是否会因为长文本而失衡。
- 含行内代码的项目：`npm run build`
- 含链接的项目：[主题指南](/theme-guide/)
- 含强调的项目：**粗体**、_斜体_、~~删除线~~

### 有序列表

1. 第一步：准备依赖
2. 第二步：启动开发服务器
3. 第三步：打开浏览器
4. 第四步：悬停目录横线
5. 第五步：检查展开态
6. 第六步：滚动页面
7. 第七步：刷新页面
8. 第八步：观察状态是否保持

### 任务列表

- [x] 目录能正常生成
- [x] 重复标题能去重
- [ ] 超长标题在展开态完整可读
- [ ] 触屏设备也能展开目录

## 引用与嵌套引用

> 这是一段普通引用，用于观察左边框、内边距和文本颜色。
>
> 第二段引用继续占用多行，测试引用块内部的段落间距。

> > 这是嵌套引用。
> >
> > > 这是第三层嵌套引用，理论上仍然应该保持可读。

## 宽表格测试

| 序号 | 标题                                                   | 类型     | 长度 | 语言     | 备注                                   | 链接                        | 状态 |
| ---- | ------------------------------------------------------ | -------- | ---- | -------- | -------------------------------------- | --------------------------- | ---- |
| 1    | 一个非常长的表格单元格内容，用于测试横向溢出与换行策略 | 压力测试 | 1024 | 中文     | 这一段备注同样很长，目的是让表格尽量宽 | [示例](https://example.com) | 正常 |
| 2    | Short                                                  | Test     | 12   | EN       | normal                                 | [link](https://example.com) | OK   |
| 3    | 中等长度的标题                                         | 测试     | 256  | 中英混排 | 含 `inline code` 与 **粗体**           | —                           | 正常 |
| 4    | 第四行                                                 | 边界     | 0    | —        | 空值测试                               | —                           | 待定 |

## 代码块压力测试

```ts
// 这是一行刻意拉长的代码，用于测试横向滚动、行号、复制按钮以及代码块背景在极宽内容下的表现。
const extremelyLongVariableName = someFunction(
  withAnExtremelyLongArgumentName,
  anotherExtremelyLongArgumentName,
  yetAnotherExtremelyLongArgumentName,
  andOneMoreForGoodMeasure
)
```

```js
function stressTest(input) {
  const values = Array.from({ length: 100 }, (_, index) => ({
    index,
    label: `item-${index}`,
    nested: { a: index * 2, b: index * 3, c: { deep: index * 4 } }
  }))

  return values.filter((value) => value.index % 2 === 0).map((value) => value.nested.c.deep)
}
```

```css
.extremely-long-selector-name-that-keeps-going-and-going .another-very-long-class-name .yet-another-long-class-name {
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.8) 0%,
    rgba(255, 255, 255, 0.8) calc(100% - 1.6rem),
    transparent 100%
  );
}
```

## 数学公式

行内公式：$E = mc^2$，以及更复杂一点的 $\displaystyle \int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}$。

$$
\begin{aligned}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
$$

## 脚注与引用标记

这里有一个脚注引用[^stress-note]，用于测试脚注跳转与回跳。

这里还有一个更长的脚注引用[^long-note]，其内容包含链接与行内代码。

[^stress-note]: 这是一个用于压力测试的脚注，内容很短。

[^long-note]: 这是一个更长的脚注，包含 `inline code`、一个[链接](https://example.com)、以及足够多的文字来测试脚注区域在窄屏下的换行。脚注的返回按钮应该仍然可用，并且不会因为页面过长而失效。

## 折叠内容

<details>
<summary>点击展开一段被折叠的长文本</summary>

折叠区域内部同样可以有标题、列表和代码。这里的标题不会进入目录，因为目录是在构建时从 Markdown AST 生成的，而折叠块内部的结构仍然属于正文。

- 折叠列表项一
- 折叠列表项二

```text
folded code block
```

</details>

## 超长无空格字符串

下面这一行没有任何空格，用于验证强制换行：

`0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789`

再重复一次，但放在正文里：012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789。

## 图片与媒体占位

本节故意不放图片，避免测试文章依赖不存在的资源。正式文章里如果出现图片，图片查看器、懒加载与 `fetchpriority` 逻辑应该在长页面中仍然正常工作。

## 多级标题混合

### 三级标题 A

#### 四级标题 A-1（不应进入目录）

四级标题只影响正文层级，不应该出现在 TOC 中。如果它出现了，说明 `remark-toc` 的层级过滤失效。

### 三级标题 B

#### 四级标题 B-1（不应进入目录）

继续填充一点正文，确保目录项的纵向位置不会因为空章节而挤在一起。

### 三级标题 C

#### 四级标题 C-1（不应进入目录）

再填充一句。

## 大量短章节

### 短章节 01

内容 01。

### 短章节 02

内容 02。

### 短章节 03

内容 03。

### 短章节 04

内容 04。

### 短章节 05

内容 05。

### 短章节 06

内容 06。

### 短章节 07

内容 07。

### 短章节 08

内容 08。

### 短章节 09

内容 09。

### 短章节 10

内容 10。

## 结语

如果这篇测试文章能够正常构建、目录能够完整生成、悬浮展开层不会因为标题过多而崩坏、滚动高亮仍然准确，那么这套目录实现就通过了第一轮极端输入测试。接下来值得继续观察的是：标题数量超过视口高度时的目录溢出、触屏设备上的展开方式，以及超长标题在展开面板中的截断策略。
