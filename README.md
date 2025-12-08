# 名字生成器 ✨

这是一个精美的名字生成器网页应用，具有现代化的玻璃拟态设计风格。集成 **Faker.js** 库，支持15+种语言/地区的真实名字生成。

**在线演示：** [https://name.relengxing.tech/](https://name.relengxing.tech/)

---

## 🚀 快速部署到 GitHub Pages

本项目是纯静态网站，部署非常简单！

### 3 步部署：

1️⃣ **推送代码到 GitHub**
```bash
git init
git add .
git commit -m "feat: 名字生成器"
git remote add origin https://github.com/你的用户名/你的仓库名.git
git branch -M main
git push -u origin main
```

2️⃣ **启用 GitHub Pages**
- 进入仓库 → Settings → Pages
- Source 选择：**Deploy from a branch**
- Branch 选择：**main** 分支，**/ (root)** 目录
- 点击 Save

3️⃣ **完成！**
- 等待 1-2 分钟
- 访问：`https://你的用户名.github.io/你的仓库名/`

📖 **详细部署指南：** [doc/DEPLOYMENT.md](doc/DEPLOYMENT.md)

---

## ✨ 功能特点

- 🎨 **现代化设计**: 使用 Tailwind CSS 和 Glassmorphism 玻璃拟态效果
- 🌍 **多语言支持**: 支持 15+ 种语言/地区（中文、英文、日文、韩文、法语、德语等）
- 🚀 **Faker.js 集成**: 使用专业的 Faker.js 库生成真实、多样化的名字
- 📚 **大型名字库**: 内置近 7000 个中文名字，避免重复
- 🖌️ **精准笔画计算**: 集成 cnchar.js 库，准确计算中文笔画数
- 📊 **多级排序**: 支持字母、笔画、长度等多种排序方式（最多 3 级组合）
- 🎲 **灵活生成**: 自定义生成数量（1-100）
- ✍️ **智能识别**: 支持粘贴名字列表，自动识别多种分隔符
- 📋 **便捷复制**: 一键复制单个或全部名字
- 📱 **响应式设计**: 完美适配手机、平板、电脑

---

## 🌍 支持的语言/地区

🇨🇳 中文 | 🇺🇸 英文(美) | 🇬🇧 英文(英) | 🇯🇵 日文 | 🇰🇷 韩文 | 🇫🇷 法文 | 🇩🇪 德文 | 🇪🇸 西班牙文 | 🇮🇹 意大利文 | 🇧🇷 葡萄牙文 | 🇷🇺 俄文 | 🇸🇦 阿拉伯文 | 🇹🇷 土耳其文 | 🇻🇳 越南文 | 🇹🇭 泰文

---

## 📖 使用方法

### 基本使用
1. 选择语言/地区
2. 设置生成数量（1-100）
3. 点击"🚀 开始生成"
4. 点击任意名字复制

### 高级功能
- **多级排序**：最多可组合 3 种排序方式
- **粘贴名字**：从 Excel/网页等复制名字列表，自动识别分隔符
- **批量复制**：选择分隔符后一键复制全部

📚 **详细使用说明：** [doc/USAGE.md](doc/USAGE.md)

---

## 🗂️ 项目结构

```
名字生成器/
├── index.html              # 主页面
├── favicon.svg             # 网站图标
├── names/                  # 名字库文件夹
│   ├── chinese_names.txt   # 7000+ 中文名字
│   └── english_names.txt   # 英文名字
├── doc/                    # 文档文件夹
│   ├── DEPLOYMENT.md       # 部署指南
│   ├── USAGE.md            # 使用说明
│   ├── ANALYTICS_SETUP.md  # 统计配置
│   └── ...                 # 其他文档
├── .gitignore              # Git 忽略配置
└── README.md               # 本文件
```

---

## 🛠️ 技术栈

- **前端框架**: 无（纯 HTML/CSS/JavaScript）
- **CSS 框架**: Tailwind CSS (CDN)
- **名字生成**: Faker.js v10
- **笔画计算**: cnchar.js
- **部署**: GitHub Pages
- **特色**: 玻璃拟态设计 (Glassmorphism)

---

## 📊 配置网站统计（可选）

部署后可以配置百度统计和 Google Analytics 来了解访问情况：

📊 **统计配置指南：** [doc/ANALYTICS_SETUP.md](doc/ANALYTICS_SETUP.md)

---

## 📚 文档导航

| 文档 | 说明 |
|------|------|
| [部署指南](doc/DEPLOYMENT.md) | GitHub Pages 部署详细步骤 |
| [快速部署](doc/QUICK_DEPLOY.md) | 最简洁的部署流程 |
| [使用说明](doc/USAGE.md) | 功能详细使用指南 |
| [统计配置](doc/ANALYTICS_SETUP.md) | 百度统计和 Google Analytics 配置 |
| [分隔符识别](doc/SEPARATOR_GUIDE.md) | 智能分隔符识别规则 |
| [Faker.js 集成](doc/FAKER_INTEGRATION.md) | Faker.js 技术细节 |

---

## 💡 自定义名字库

可以编辑 `names/` 文件夹中的文件来自定义名字库：

- `chinese_names.txt` - 每行一个中文名字
- `english_names.txt` - 每行一个英文名字

保存后刷新页面即可生效。

---

## 🌟 特色功能

### 智能分隔符识别
自动识别输入文本的分隔符：
- 中文：逗号、顿号、空格、换行等
- 英文：逗号、分号、换行等（保留名字中的空格）

### 多级排序组合
支持最多 3 种排序方式组合：
- 字母顺序 (A-Z / Z-A)
- 笔画顺序 (少→多 / 多→少)
- 长度顺序 (短→长 / 长→短)

### Faker.js 强力驱动
- 15+ 种语言/地区支持
- 数万个真实名字数据
- 自动适配文化命名习惯

---

## 🔗 友情链接

- [工具集合站](https://tool.relengxing.tech/)
- [手写文本生成器](https://handwrite.relengxing.tech/)

---

## 📝 Slogan

**用正确打开方式使用人名大全**

---

## 📄 开源协议

本项目采用 MIT 协议开源。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**享受使用！如有任何问题或建议，欢迎反馈。** ✨
