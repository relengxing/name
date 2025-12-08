# GitHub Pages 部署指南

本文档介绍如何将名字生成器部署到 GitHub Pages。

---

## ✨ 本项目特点

本项目是**纯静态网站**，无需构建、无需 Node.js，部署非常简单！

---

## 📋 前提条件

- 有一个 GitHub 账号
- 已安装 Git

---

## 🚀 部署步骤

### 步骤 1：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库名称（例如：`name-generator`）
4. 选择 "Public"（公开仓库才能免费使用 GitHub Pages）
5. **不要**勾选 "Add a README file"
6. 点击 "Create repository"

### 步骤 2：推送代码到 GitHub

在项目根目录打开终端，执行以下命令：

```bash
# 初始化 Git 仓库（如果还没有初始化）
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "feat: 名字生成器首次部署"

# 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 重命名分支为 main
git branch -M main

# 推送代码到 main 分支
git push -u origin main
```

### 步骤 3：启用 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击 "Settings"（设置）
3. 在左侧菜单中找到 "Pages"
4. 在 "Source" 部分：
   - 选择 **"Deploy from a branch"**
   - Branch 选择 **"main"**
   - 文件夹选择 **"/ (root)"**
5. 点击 "Save"

### 步骤 4：等待部署完成

1. 在 Pages 设置页面，你会看到一个提示："Your site is live at ..."
2. 等待 1-2 分钟让 GitHub 部署你的网站
3. 页面刷新后，绿色框会显示你的网站地址

### 步骤 5：访问你的网站

你的网站地址将是：
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

例如：
- 用户名：`zhangsan`
- 仓库名：`name-generator`
- 访问地址：`https://zhangsan.github.io/name-generator/`

---

## 🔄 更新网站

每次修改代码后，只需推送到 GitHub 即可：

```bash
# 修改代码后
git add .
git commit -m "更新描述"
git push
```

等待 1-2 分钟，GitHub Pages 会自动更新。

---

## 🌐 自定义域名（可选）

如果你有自己的域名，可以配置自定义域名：

### 方法 1：使用 CNAME 记录（推荐）

1. 在仓库根目录创建一个名为 `CNAME` 的文件（无扩展名）
2. 在文件中写入你的域名（例如：`name.yourdomain.com`）
3. 推送到 GitHub

```bash
echo "name.yourdomain.com" > CNAME
git add CNAME
git commit -m "feat: 添加自定义域名"
git push
```

### 方法 2：在 DNS 配置

在你的域名提供商处添加 DNS 记录：

**使用子域名（推荐）：**
- 类型：CNAME
- 名称：name（或其他子域名）
- 值：YOUR_USERNAME.github.io

**使用根域名：**
- 类型：A
- 名称：@
- 值：添加以下 4 个 IP 地址
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```

### 方法 3：在 GitHub 配置

1. 在 GitHub Pages 设置中输入你的自定义域名
2. 等待 DNS 验证完成
3. 建议勾选 "Enforce HTTPS"

---

## 🛠️ 故障排查

### 问题 1：页面显示 404

**原因：**
- 部署还没完成
- 分支或路径选择错误
- 文件名大小写问题

**解决方案：**
1. 等待 5-10 分钟
2. 确认 Pages 设置中选择了正确的分支（main）和路径（/ root）
3. 确保 `index.html` 在仓库根目录
4. 清除浏览器缓存

### 问题 2：样式或图片加载失败

**原因：**
- 使用了绝对路径

**解决方案：**
本项目已使用相对路径，应该不会出现此问题。如果出现，检查 HTML 中的路径。

### 问题 3：名字库文件加载失败

**原因：**
- CORS 跨域问题（本地开发时）
- 文件路径错误

**解决方案：**
1. GitHub Pages 部署后不会有 CORS 问题
2. 本地开发时使用 Live Server 等工具
3. 确保 `names/` 文件夹已推送到 GitHub

### 问题 4：推送失败

**原因：**
- 没有权限
- 远程仓库地址错误

**解决方案：**
```bash
# 检查远程仓库地址
git remote -v

# 如果错误，删除并重新添加
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 确保使用 HTTPS 或 SSH 认证
git push -u origin main
```

---

## 📊 配置网站统计（可选）

部署完成后，建议配置网站统计来了解访问情况：

👉 详细配置方法请查看：[ANALYTICS_SETUP.md](ANALYTICS_SETUP.md)

需要配置：
1. **Google Analytics**：适合国际用户
2. **百度统计**：适合国内用户

---

## 🔧 更新 SEO 信息（可选）

部署后，建议更新 `index.html` 中的 meta 标签：

找到以下内容（约 15-27 行）：
```html
<meta property="og:url" content="https://yourdomain.com/">
```

替换为你的实际网址：
```html
<meta property="og:url" content="https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/">
```

这样在社交媒体分享时会显示正确的链接。

---

## 📱 测试清单

部署完成后，建议测试以下功能：

- [ ] 网站能正常访问
- [ ] 点击"开始生成"能生成名字
- [ ] 名字库能正常加载（查看浏览器控制台）
- [ ] 排序功能正常
- [ ] 复制功能正常
- [ ] 多语言切换正常
- [ ] 手机端显示正常

---

## 💡 提示

1. ✅ 本项目是纯静态网站，无需构建步骤
2. ✅ 所有依赖通过 CDN 加载，无需安装
3. ✅ 修改代码后只需 `git push` 即可更新
4. ✅ GitHub Pages 免费且稳定
5. ✅ 支持自定义域名

---

## 🆘 需要帮助？

如果遇到问题：
1. 查看本文档的故障排查部分
2. 查看 [GitHub Pages 官方文档](https://docs.github.com/pages)
3. 在项目仓库创建 Issue

---

## 🎉 部署完成！

恭喜你成功部署了名字生成器！

现在你可以：
- 🌐 访问你的网站
- 📊 配置统计（可选）
- 🎨 自定义样式
- 📚 添加更多名字到名字库
- 🔗 分享给朋友

---

**祝你的网站访问量节节高升！** 🚀✨
