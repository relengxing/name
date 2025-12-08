# GitHub Pages 部署指南

本文档介绍如何将名字生成器部署到 GitHub Pages。

## 前提条件

- 有一个 GitHub 账号
- 已安装 Git

## 部署步骤

### 1. 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库名称（例如：`name-generator`）
4. 选择 "Public"（公开仓库才能免费使用 GitHub Pages）
5. 点击 "Create repository"

### 2. 推送代码到 GitHub

在项目根目录打开终端，执行以下命令：

```bash
# 初始化 Git 仓库（如果还没有初始化）
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit: 名字生成器"

# 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送代码到 main 分支
git push -u origin main
```

### 3. 配置 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击 "Settings"（设置）
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分，选择 "GitHub Actions"
5. 保存设置

### 4. 等待部署完成

1. 点击仓库顶部的 "Actions" 标签
2. 你会看到一个正在运行的工作流 "Deploy to GitHub Pages"
3. 等待工作流完成（通常需要 1-2 分钟）
4. 完成后，返回 Settings → Pages，你会看到你的网站地址

### 5. 访问你的网站

你的网站地址将是：
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

## 自动部署

配置完成后，每次你推送代码到 `main` 分支，GitHub Actions 都会自动构建和部署你的网站。

```bash
# 修改代码后
git add .
git commit -m "更新描述"
git push
```

## 自定义域名（可选）

如果你有自己的域名，可以配置自定义域名：

1. 在仓库根目录创建一个名为 `CNAME` 的文件
2. 在文件中写入你的域名（例如：`name.yourdomain.com`）
3. 在你的域名提供商处添加 CNAME 记录，指向 `YOUR_USERNAME.github.io`
4. 推送代码到 GitHub
5. 在 GitHub Pages 设置中输入你的自定义域名

## 故障排查

### 部署失败

- 检查 Actions 标签页中的错误信息
- 确保 Pages 设置中选择了 "GitHub Actions"
- 确保仓库是公开的

### 页面显示 404

- 等待几分钟让 DNS 传播
- 检查访问的 URL 是否正确
- 确保 index.html 文件在仓库根目录

### 名字库文件加载失败

这是正常的，因为浏览器的跨域安全策略。有两种解决方案：

1. **使用在线编辑**：直接在 GitHub 上编辑 `names/` 文件夹中的文件
2. **本地开发**：使用本地服务器（如 Live Server 扩展）

## 更新 SEO 信息

部署后，记得更新 `index.html` 中的 SEO 信息：

1. 将所有的 `https://yourdomain.com/` 替换为你的实际 GitHub Pages 地址
2. 如果需要，添加网站预览图片 `preview.png`
3. 提交并推送更改

## 支持

如有问题，请在 GitHub 仓库中创建 Issue。

---

祝你部署顺利！🚀

