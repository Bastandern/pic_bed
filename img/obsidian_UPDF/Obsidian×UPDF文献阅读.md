

本教程包含以下内容：
1. UPDF 文献阅读流程
2. 利用 UPDF 构建论文阅读元笔记
3. 利用 Obsidian *数据库* 核心插件建立论文检索库

# 整体工作流

**首先展示一下最终达到的效果**：

`paper-database/` 是论文仓库，里面的每个 BASE 都是筛选出的 *研究方向* 的 *论文列表*。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_204128.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-1.png)

在论文列表中可以查看论文信息，点击第一栏名称可跳转到对应 *论文笔记页面*。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-2.png)

点击“直接阅读”后的 <u>PDF</u>，直接打开这篇论文对应 PDF 的 UPDF 界面，里面包含我们精读论文时做的批注。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-3.png)

在 Obsidian 自带的标签页面，也可以查看论文的待办列表等。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_190517.png)

# UPDF 阅读文献

官网下载：[UPDF-新一代AI智能PDF编辑器【官网】](https://www.updf.cn/)

## 文献检索

打开 UPDF 后进入 AI 功能。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-4.png)

点击 *论文搜索与图谱* 即可进入论文检索模块，输入关键词后在左侧设置检索条件。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-5.png)

针对检索出的论文，可以通过 *PDF对话* 功能快速了解文章内容，判断是否有阅读价值。也可以用这个 [论文阅读prompt](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/%E8%AE%BA%E6%96%87%E9%98%85%E8%AF%BBprompt.md) 去粗略总结论文内容。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-6.png)

对于有价值的文章可以 *查看关联图谱* 和 *下载 PDF*。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-7.png)
- 关联图谱里面的文章也都是可以直接添加到 *PDF对话* 进行阅读的，还可以翻译摘要。

## 文献精读

用 UPDF 打开需要精读的文章。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185500-8.png)

### 翻译

点击页面右上角的 *UPDF AI* 小图标，展开右侧功能栏。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501.png)

**全文翻译**：可将原文和翻译两列对照显示。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-1.png)

**实时翻译**：直接选中文本点击 *翻译* 即可实时翻译。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-2.png)

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-3.png)

### AI 问答与思维导图

右侧功能栏第一个是 *PDF 对话*。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-4.png)

*AI 总结* 后还会给出几个预设的问题帮助理解，也可以向其提问。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-5.png)

可以选定页码生成 *思维导图*。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-6.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-7.png)

生成的思维导图可 *下载*，也可以直接 *插入到 PDF 首页*，方便下次阅读查看。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-8.png)

### 批注

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-9.png)
也可使用铅笔和矩形框对图片进行标记。

批注后点击保存。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185501-10.png)

# Obsidian 文献笔记管理库

## 创建论文笔记

根据模板创建笔记：将 [paper-prompt](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/paper-prompt.md) 喂给 AI，将结果粘贴回来。可以将 *ShortName* 字段作为笔记名称。
- 包含论文信息、**研究方向分类标签**（后续创建论文库最重要的东西）、核心摘要
- 内置从 Obsidian 跳转 UPDF **直接查看论文批注** 的功能

> paper-prompt 中的 *PDF链接* 地址需要改成你存放论文pdf的文件夹。
>![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502.png)

得到的笔记模板如下：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-1.png)

这里的直接阅读 PDF 点击会直接弹出 UPDF 中该篇论文的界面，便于之后回顾论文和精读批注内容。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-2.png)

>如果打开的不是 UPDF，只需要右键一个 pdf 格式文件，打开属性面板，将默认改为 UPDF
>![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-3.png)

精读文献后将重要观点和想法提炼后记录到笔记下方就可以了。

> **跳转失败解决方案：手动填写URL**
> 复制论文文件名，使用 [在线url网址编码、解码(ES JSON在线工具)](http://www.esjson.com/urlEncode.html) 转换成 URL 编码。
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-4.png)
> 再按 `file://<存放PDF的地址>/<PDF文件名URL编码>.pdf` 拼接后覆盖到原来位置。

## 文献库

>这一步实际上是按照 **论文方向标签** 进行分类，将同方向论文整理到一个知识库里去。都是基于我们上一步笔记模板中嵌入了论文标签：
>![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-5.png)
>![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-6.png)

### 创建数据库

先在设置里打开 *数据库* 功能。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185711.png)

ctrl+p，输入“数据库”，点击“数据库: 新建数据库”
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-7.png)


### 设置筛选条件
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-8.png)
点击筛选，设置两个条件：
1. **文件标签 contains paper**，用于筛选论文笔记。这是由于我们的论文笔记模板里已经给每一篇笔记自带了 paper 的 tag
2. **论文方向筛选**。点击 *添加筛选器*，点击右侧图标转换为高级筛选模式。

高级筛选采用 JavaScript 语句（可以让 AI 写）。也可以直接用我下面的示例，修改研究方向就行：

示例：筛选“场景/领域/细分”标签里带有“多模态”的文章。也就是 **筛选多模态方向的文章** 的意思。
```JavaScript
file.tags.filter((value.contains("场景/") || value.contains("领域/") || value.contains("细分/")) && (value.contains("多模态") )).length > 0
```

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-9.png)
可以根据自己的需要设置，一般只需改 && 后面的部分

### 展示属性

选择需要展示的属性，一般是这几个，可以按需添加。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185502-10.png)

设置完后效果如下：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185503.png)

点击 *名称* 栏，可以跳转到该文章的笔记页面。修改其他栏的内容，对应文章笔记内部属性也会同步修改。

## 论文标签

笔记模板中我们通过 AI 给论文打上了很多标签，*场景/领域/细分* 用来标记研究方向（用于数据库筛选），而 *待办/类型/评级* 则主要是给自己看的。

可根据理解修改标签二级内容（可不唯一），然后在右侧 *标签* 页面查看。这样 只读了一半/还没复现/需要引
用... 的论文，都可以记录在案。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185503-1.png)

# UPDF 其他功能

对于平时课程的学习，UPDF 也能起到帮助作用。

## OCR
如果载入一个扫描版的 PDF 电子教材，UPDF 可自动将其识别。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185503-2.png)

对其使用OCR识别功能。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185503-3.png)

识别后，文字变成可选中的。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_UPDF/Obsidian%C3%97UPDF%E6%96%87%E7%8C%AE%E9%98%85%E8%AF%BB_260821_185503-4.png)

## PDF 编辑

对课程 PPT 直接进行 AI 对话整理并原地批注，比起自己单独整理笔记要省时间，又避免了 AI 整理漏东西。这对于 **开卷考试**（覆盖全、不遗漏、时间投入相对较少）来说是再合适不过的了。