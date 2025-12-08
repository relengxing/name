# 🚀 快速部署到 GitHub Pages

## 最简 3 步部署

### 1️⃣ 推送代码到 GitHub

```bash
git init
git add .
git commit -m "feat: 名字生成器"
git remote add origin https://github.com/你的用户名/你的仓库名.git
git branch -M main
git push -u origin main
```

### 2️⃣ 启用 GitHub Pages

1. 进入仓库 → **Settings** → **Pages**
2. Source 选择：**Deploy from a branch**
3. Branch 选择：**main** 分支，**/ (root)** 目录
4. 点击 **Save**

### 3️⃣ 完成！

等待 1-2 分钟，访问：
```
https://你的用户名.github.io/你的仓库名/
```

---

## 📝 后续更新

每次修改代码后：

```bash
git add .
git commit -m "你的更新说明"
git push
```

等待 1-2 分钟自动生效！

---

## 🔧 项目特点

✅ **纯静态网站** - 无需构建  
✅ **零配置** - 推送即部署  
✅ **CDN 加载** - 所有依赖自动加载  
✅ **自动更新** - 推送后自动生效  

---

## 🌐 访问地址格式

```
https://用户名.github.io/仓库名/
```

**示例：**
- 用户名：`zhangsan`
- 仓库名：`name-generator`
- 访问地址：`https://zhangsan.github.io/name-generator/`

---

## 💡 提示

1. 仓库必须是**公开的**（Public）
2. 首次部署需要等待 1-2 分钟
3. 后续更新自动生效（无需手动操作）
4. 如有问题，查看详细文档：[DEPLOYMENT.md](DEPLOYMENT.md)

---

## 📚 相关文档

- [详细部署指南](DEPLOYMENT.md) - 完整步骤和故障排查
- [使用说明](USAGE.md) - 功能使用指南
- [统计配置](ANALYTICS_SETUP.md) - 网站统计设置

---

**就这么简单！开始部署吧！** 🎉
