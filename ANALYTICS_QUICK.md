# 📊 统计配置 - 快速指南

本页面提供最简洁的统计配置步骤。详细说明请查看 [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md)。

---

## 🎯 为什么需要配置统计？

配置统计后，你可以了解：
- 📈 网站访问量
- 👥 访客来源
- 🌍 访客地理位置
- 📱 使用设备类型
- ⏱️ 访问时长

---

## ⚡ 快速配置

### 步骤 1：获取统计 ID

#### Google Analytics
1. 访问 https://analytics.google.com/
2. 创建账号 → 创建媒体资源 → 创建数据流
3. 获取 `G-XXXXXXXXXX` 格式的 ID

#### 百度统计
1. 访问 https://tongji.baidu.com/
2. 管理 → 新增网站
3. 代码获取 → 复制 `hm.js?` 后面的 ID

### 步骤 2：修改 index.html

找到 `index.html` 的第 39-60 行左右：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');  ← 替换这里
</script>

<!-- 百度统计 -->
<script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?YOUR_BAIDU_TONGJI_ID";  ← 替换这里
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(hm, s);
    })();
</script>
```

**替换为你自己的 ID！**

### 步骤 3：推送更新

```bash
git add index.html
git commit -m "feat: 配置统计代码"
git push
```

### 步骤 4：验证

1. 等待 1-2 分钟部署完成
2. 访问你的网站
3. 查看统计后台是否有数据（可能需要等待 20-30 分钟）

---

## 📝 配置示例

### 替换前
```html
gtag('config', 'G-XXXXXXXXXX');
hm.src = "https://hm.baidu.com/hm.js?YOUR_BAIDU_TONGJI_ID";
```

### 替换后（示例）
```html
gtag('config', 'G-ABC123XYZ');
hm.src = "https://hm.baidu.com/hm.js?1234567890abcdef1234567890abcdef";
```

---

## ❓ 常见问题

**Q：必须两个都配置吗？**  
A：不是，可以只配置一个，或者都不配置。

**Q：不配置会影响网站功能吗？**  
A：不会，网站功能完全正常，只是看不到访问统计数据。

**Q：看不到数据怎么办？**  
A：等待 20-30 分钟，确保 ID 正确，检查是否有广告拦截插件。

---

## 📚 详细文档

需要更详细的说明？查看完整的配置指南：

👉 [ANALYTICS_SETUP.md](ANALYTICS_SETUP.md)

包含：
- 详细注册步骤（带截图说明）
- 统计后台使用指南
- 数据查看方法
- 完整的故障排查

---

## ✅ 配置完成

配置完成后，你就可以：
- 📊 查看实时访问数据
- 📈 分析用户行为
- 🎯 优化网站内容
- 📱 了解用户设备

**祝你网站访问量节节高升！** 🚀

