# 🚀 快速部署到 GitHub Pages

## 一键部署步骤

### 1️⃣ 创建 GitHub 仓库
```bash
# 在 GitHub 网站上创建一个新的公开仓库
# 仓库名称例如：name-generator
```

### 2️⃣ 推送代码
```bash
# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "feat: 名字生成器首次提交"

# 添加远程仓库（替换 YOUR_USERNAME 和 REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 重命名分支为 main（如果需要）
git branch -M main

# 推送
git push -u origin main
```

### 3️⃣ 启用 GitHub Pages
1. 进入仓库 → **Settings** → **Pages**
2. 在 **Source** 下选择 **GitHub Actions**
3. 保存

### 4️⃣ 完成！
- 等待 1-2 分钟自动部署完成
- 访问：`https://YOUR_USERNAME.github.io/REPO_NAME/`

## 📝 后续更新

每次修改代码后：
```bash
git add .
git commit -m "你的更新说明"
git push
```

GitHub Actions 会自动重新部署！

## 🔧 项目特点

✅ **已配置好的文件：**
- `.github/workflows/deploy.yml` - 自动部署工作流
- `.nojekyll` - 禁用 Jekyll 处理
- `.gitignore` - Git 忽略规则

✅ **无需构建：**
- 纯静态 HTML/CSS/JS
- 所有依赖通过 CDN 加载
- 直接推送即可部署

✅ **自动化部署：**
- 推送到 main 分支自动触发
- 也支持手动触发部署

## 🌐 访问地址

部署成功后，你的网站地址为：
```
https://YOUR_USERNAME.github.io/REPO_NAME/
```

例如：
- 用户名：`zhangsan`
- 仓库名：`name-generator`
- 访问地址：`https://zhangsan.github.io/name-generator/`

## 💡 提示

1. 仓库必须是**公开的**才能免费使用 GitHub Pages
2. 首次部署可能需要等待几分钟
3. 可以在 Actions 标签页查看部署进度
4. 名字库文件 (`names/*.txt`) 会正常加载

## 📚 相关文档

- 详细部署指南：[DEPLOYMENT.md](DEPLOYMENT.md)
- 使用说明：[USAGE.md](USAGE.md)
- 主文档：[README.md](README.md)

