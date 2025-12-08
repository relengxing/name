# 📦 GitHub Pages 部署文件说明

本文档说明项目中为 GitHub Pages 部署准备的所有文件。

## 🔧 核心配置文件

### `.github/workflows/deploy.yml`
GitHub Actions 自动部署工作流配置文件。

**功能：**
- 当代码推送到 `main` 分支时自动触发部署
- 支持手动触发部署
- 自动上传所有文件到 GitHub Pages

**无需修改**，开箱即用！

### `.nojekyll`
禁用 GitHub Pages 的 Jekyll 处理。

**作用：**
- 确保以 `.` 或 `_` 开头的文件夹不被忽略
- 加快部署速度
- 避免 Jekyll 处理导致的问题

**空文件**，只要存在即可。

### `.gitignore`
Git 忽略规则配置。

**包含：**
- 编辑器配置文件（.vscode、.idea）
- 系统文件（.DS_Store、Thumbs.db）
- 临时文件（*.log、*.tmp）
- Node modules（如果将来需要）

## 📚 文档文件

### `QUICK_DEPLOY.md` ⭐ 推荐
**最简洁的快速部署指南**

包含：
- 3 步快速部署流程
- 清晰的命令示例
- 访问地址格式说明

**适合：**第一次部署的用户

### `DEPLOYMENT.md`
**详细的部署指南**

包含：
- 完整的部署步骤
- GitHub Pages 配置说明
- 自定义域名配置
- 故障排查方案
- SEO 优化建议

**适合：**需要详细说明的用户

### `DEPLOYMENT_CHECKLIST.md`
**部署检查清单**

包含：
- 部署前检查项
- 部署步骤
- 部署后测试项
- 故障排查

**适合：**确保部署万无一失

## 🚀 部署脚本

### `deploy.bat`（Windows）
Windows 用户的一键部署脚本。

**使用方法：**
```cmd
deploy.bat "你的提交信息"
```

**功能：**
- 自动 git add、commit、push
- 显示部署进度提示

### `deploy.sh`（Linux/Mac）
Linux/Mac 用户的一键部署脚本。

**使用方法：**
```bash
bash deploy.sh "你的提交信息"
```

**功能：**
- 自动 git add、commit、push
- 显示部署进度提示

## 📄 核心文件

### `index.html`
主页面文件。

**特点：**
- 所有代码在单个 HTML 文件中
- 依赖通过 CDN 加载（Faker.js、cnchar.js、Tailwind CSS）
- 无需构建步骤，直接可用

**需要修改：**
部署后建议将 meta 标签中的 `yourdomain.com` 替换为你的实际 GitHub Pages 地址。

### `favicon.svg`
网站图标。

### `names/` 文件夹
名字库文件。

**包含：**
- `chinese_names.txt` - 7000+ 中文名字
- `english_names.txt` - 英文名字

**重要：**确保这些文件被正确推送到 GitHub。

## 📖 其他文档

### `README.md`
项目主文档，包含项目介绍、功能特点、技术栈等。

### `USAGE.md`
详细的使用说明文档。

### `SEPARATOR_GUIDE.md`
智能分隔符识别规则说明。

### `FAKER_*.md`
Faker.js 相关的技术文档和解决方案。

## 🎯 最简部署流程

对于第一次部署的用户，只需要关注：

1. **阅读：**`QUICK_DEPLOY.md`
2. **执行：**
   ```bash
   git init
   git add .
   git commit -m "feat: 首次部署"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```
3. **配置：**GitHub Settings → Pages → Source 选择 "GitHub Actions"
4. **完成！**

## 📦 推送到 GitHub 的文件

以下文件都会被推送到 GitHub：

```
.github/
  workflows/
    deploy.yml          # 自动部署配置
.gitignore             # Git 忽略规则
.nojekyll              # 禁用 Jekyll
deploy.bat             # Windows 部署脚本
deploy.sh              # Linux/Mac 部署脚本
DEPLOYMENT*.md         # 部署文档
favicon.svg            # 网站图标
index.html             # 主页面
names/                 # 名字库文件夹
  chinese_names.txt
  english_names.txt
QUICK_DEPLOY.md        # 快速部署指南
README.md              # 项目说明
*.md                   # 其他文档
```

## 🔍 部署后验证

部署成功后，访问你的网站，检查：

1. ✅ 页面能正常显示
2. ✅ 点击"开始生成"能生成名字
3. ✅ 控制台提示名字库加载成功
4. ✅ 笔画排序功能正常
5. ✅ 所有功能正常工作

## 💡 提示

- **首次部署**：推荐阅读 `QUICK_DEPLOY.md`
- **详细了解**：查看 `DEPLOYMENT.md`
- **确保无误**：使用 `DEPLOYMENT_CHECKLIST.md`
- **快速更新**：使用 `deploy.bat` 或 `deploy.sh`

## 🆘 需要帮助？

如果遇到问题：
1. 查看 `DEPLOYMENT.md` 中的故障排查章节
2. 检查 GitHub Actions 的日志
3. 在项目仓库创建 Issue

---

祝部署顺利！🎉

