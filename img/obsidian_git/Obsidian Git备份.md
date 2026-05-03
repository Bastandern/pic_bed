---
title: Obsidian Git备份
tags:
    - Tools
categories: tools
cover: https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/cover.png
date: 2026-05-03 11:03
top_img: https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/cover.png
copyright_author: Bastandern
---

# 附件分离

**这一步是将所有图片与笔记分离开，将图片整理到一个目录下，并给图片重命名。**

> **为什么需要附件分离？**
> Github 建议大小：单文件 < 50MB，单仓库 < 1GB。
> Obsidian仓库的大小几乎都源于图片。
> 即使之后 Obsidian 仓库内容逐渐增加，分离附件之后一般也不会超过1GB，而图片随随便便就会到1GB以上。



> 什么情况下 **可以不做** 附件整理？
> 最开始选择附件位置的时候设置像下面这样：
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_004655.png)
> 这样的结果是，所有图片已经与笔记分离了。
> **但图片名称为原始的、语义不清的。如果按接下来的步骤整理附件，可以*重命名图片***



> 什么情况下 **建议进行** 附件整理？
> 如果你的附件位置设置成这样：
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_005026.png)
> 或者这样：
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_005032.png)
> 那么你的图片是保存在**笔记目录及其子目录下**的，目录类似：
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_005149.png)



## 整理附件

**插件**：*Attachment Management*

配置该插件后会自动拦截，“文件与链接”下无论配置的附件位置是哪里，都会优先按 Attachment Management 里面的来。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_003206.png)

**保存根路径**：*在下方指定的文件夹中*
**根文件夹**：attachment
**附件路径**：

- 空着：所有图片在 attachment 下
- `${notepath}/${notename}`：在 attachment 里创建该笔记对应附件的文件夹

**附件格式**：`${notename}_${date}`
**日期格式**：`YYMMDD_HHmmss`

- 该命名格式最终得到的文件名类似：`编译原理_260502_032801.png`
- 同一时间戳下如有多个文件会自动添加编号`-1`、`-2`、`-3`等

**排除扩展名模式**：`pdf|docx?|xlsx?|pptx?|zip|rar`

- 只会分离 png、jpg 等没有写在排除列表中的格式
- 如果需要把 pdf、doc 等也分离出来，就把这几项从“排除扩展名模式”中去掉

设置完成后，`ctrl+p` 打开命令面板，运行 `Attachment Management: 重新整理所有链接的附件`

**整理后**
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260502_004246.png)

*之后在任何一篇笔记下插入图片，都会自动整理且重命名，无需再进行手动配置！*

## 删除空图片文件夹

整理后如果有很多 **残留的 image 文件夹**，可以用代码来清理。
[代码链接](https://github.com/Bastandern/pic_bed/blob/main/img/obsidian_git/clean_images.py)，点击下载
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_094713.png)

下载后在代码的目录下，输入`cmd`打开终端
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_094756.png)

用编辑器打开代码（没有的话也可以用记事本打开）
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_094938.png)

1. 把仓库目录改成你的
2. 把图片文件夹名称改成你的

修改后保存。在终端输入命令：

```sh
python clean_images.py
```

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_095041.png)

# Git 备份

## 创建 github 仓库

先在仓库根目录下创建 `.gitignore`（注意没有后缀名）

```plaintext
attachment/
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache/
.trash/
.DS_Store
desktop.ini
```

- `attachment/`换成你自己的图片文件夹名称

在 github 新建仓库
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_093055.png)

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_093140.png)

直接复制命令
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_100054.png)
在仓库目录下打开`cmd`，一次性粘贴刚刚复制的命令

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_100226.png)

现在你的仓库已经变成 github 仓库了。接下来要配置 obsidian 的插件去自动管理你的仓库。

## 自动上传

**插件**：*Git*

只做 **备份** 和 **版本控制** 而不做多端同步，只需要在 **默认配置** 基础上改下面几个：
*Automatic*：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101333.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101336.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101343.png)
*Commit-and-sync*：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101348.png)
*Miscellaneous*：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101355.png)

配置好之后，在仓库有修改的情况下，每隔一定时间就会自动向 github 上传

查看上传记录：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_102853.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_102919.png)

## 手动上传

如果你有重要修改，不想等自动上传，也可以手动上传
只需要关注这几个图标：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_101921.png)

**手动上传的流程：**

1. 上传 *全部* 文件：直接按 commit + push
2. 上传 *部分* 文件：先把要上传的文件 `+` 进去，再按 commit 和 push
3. commit 的框框里可以填写内容

![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_102541.png)

上传成功了
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_102744.png)

## 版本控制

在 github 的 commit 界面点击历史的 commit 记录，就能查看之前的版本，以及当前的 commit 修改了哪些内容。

如果笔记做出了修改，但还未 push，可以查看修改。
在 Changes 下面找到要查看的笔记：
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_103727.png)
*红色删除，绿色添加。左侧原来的，右侧改后的。*
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_103751.png)

如果想返回之前的，可以 **撤销** 改动。
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_103921.png)
![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_103926.png)



> 不仅可以查看 **笔记** 的修改，还可以查看 **设置** 的修改。这对于 *回溯* 设置相当有用！
> 例如：
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_104443.png)
> ![](https://cdn.jsdelivr.net/gh/Bastandern/pic_bed@main/img/obsidian_git/Obsidian%20git%E5%A4%87%E4%BB%BD_260503_104448.png)
