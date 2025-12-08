# ✅ GitHub Pages 部署检查清单

部署前请确认以下事项：

## 📋 部署前检查

### 必须完成
- [ ] 已创建 GitHub 账号
- [ ] 已安装 Git
- [ ] 已在 GitHub 创建公开仓库
- [ ] 项目文件完整（index.html、names 文件夹等）

### 推荐完成
- [ ] 更新 `index.html` 中的 meta 标签 URL（将 yourdomain.com 替换为你的 GitHub Pages 地址）
- [ ] 检查 `names/chinese_names.txt` 和 `names/english_names.txt` 文件存在
- [ ] 确认 `.github/workflows/deploy.yml` 文件存在
- [ ] 确认 `.nojekyll` 文件存在

### 可选配置
- [ ] 配置 Google Analytics 统计 ID（参考 [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md)）
- [ ] 配置百度统计 ID（参考 [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md)）
- [ ] 添加自定义域名（如果有）

## 🚀 部署步骤

### 1. 初始化 Git 仓库（如果还没有）
```bash
git init
git branch -M main
```

### 2. 添加和提交文件
```bash
git add .
git commit -m "feat: 名字生成器首次部署"
```

### 3. 添加远程仓库
```bash
# 替换 YOUR_USERNAME 和 YOUR_REPO
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### 4. 推送代码
```bash
git push -u origin main
```

### 5. 启用 GitHub Pages
1. 访问仓库 → Settings → Pages
2. Source 选择：**GitHub Actions**
3. 保存

### 6. 等待部署完成
- 查看 Actions 标签页
- 等待工作流完成（约 1-2 分钟）

## 🔍 部署后检查

### 功能测试
- [ ] 网站能正常访问
- [ ] 点击"开始生成"按钮能生成名字
- [ ] 名字库文件能正常加载（检查控制台）
- [ ] cnchar.js 能正常计算笔画数
- [ ] 排序功能正常工作
- [ ] 复制功能正常工作
- [ ] 多语言切换正常

### 性能检查
- [ ] 页面加载速度正常
- [ ] CDN 资源加载正常（Faker.js、cnchar.js、Tailwind CSS）
- [ ] 控制台无错误信息

### SEO 检查
- [ ] 页面标题正确显示
- [ ] Meta 描述正确
- [ ] Open Graph 标签正确（用于分享预览）

## 🛠️ 故障排查

### 问题：部署失败
**解决方案：**
1. 检查 Actions 标签页中的错误日志
2. 确保仓库是公开的
3. 确认 Pages 设置中选择了 "GitHub Actions"

### 问题：页面 404
**解决方案：**
1. 等待 5-10 分钟让部署完全完成
2. 清除浏览器缓存
3. 检查 URL 是否正确（注意仓库名大小写）

### 问题：名字库加载失败
**解决方案：**
1. 检查 `names/` 文件夹是否被正确推送
2. 检查控制台是否有 CORS 错误
3. GitHub Pages 应该不会有 CORS 问题，如果有，检查文件路径

### 问题：cnchar.js 加载失败
**解决方案：**
1. 检查控制台错误信息
2. CDN 可能暂时不可用，稍后重试
3. 项目会自动降级使用备用方案

## 📱 部署完成后的 URL

你的网站地址格式：
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

例如：
- 用户名：`zhangsan`
- 仓库名：`name-generator`
- 访问地址：`https://zhangsan.github.io/name-generator/`

## 🎉 完成！

部署成功后，你可以：
- 分享你的网站链接
- 继续改进功能
- 每次 push 代码都会自动重新部署

## 📚 相关文档

- [快速部署指南](QUICK_DEPLOY.md)
- [详细部署文档](DEPLOYMENT.md)
- [使用说明](USAGE.md)
- [README](README.md)

## 💡 提示

- 使用 `deploy.bat`（Windows）或 `deploy.sh`（Linux/Mac）脚本可以快速部署
- 每次更新代码后只需 `git push` 即可自动重新部署
- 建议定期备份代码

