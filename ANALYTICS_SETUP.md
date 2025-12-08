# 📊 网站统计配置指南

本文档说明如何配置百度统计和谷歌分析（Google Analytics）。

---

## 🎯 统计代码位置

统计代码已经添加到 `index.html` 的 `<head>` 部分，**但需要替换为你自己的统计 ID**。

---

## 📈 Google Analytics（谷歌分析）

### 1. 获取 Google Analytics ID

#### 步骤 1：创建 Google Analytics 账号
1. 访问 [Google Analytics](https://analytics.google.com/)
2. 使用 Google 账号登录
3. 点击"开始测量"

#### 步骤 2：创建媒体资源
1. 输入**账号名称**（例如：我的网站统计）
2. 点击"下一步"
3. 输入**媒体资源名称**（例如：名字生成器）
4. 选择**报告时区**：中国（GMT+8）
5. 选择**币种**：人民币 CNY
6. 点击"下一步"

#### 步骤 3：配置数据流
1. 选择平台：**网站**
2. 输入**网站网址**：`https://YOUR_USERNAME.github.io/YOUR_REPO/`
3. 输入**数据流名称**（例如：名字生成器网站）
4. 点击"创建数据流"

#### 步骤 4：获取 Measurement ID
创建完成后，你会看到类似 `G-XXXXXXXXXX` 的 ID。

### 2. 配置到网站

在 `index.html` 中找到以下代码（约第 39-45 行）：

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
</script>
```

**将两处 `G-XXXXXXXXXX` 替换为你的实际 Measurement ID**

例如：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123XYZ"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-ABC123XYZ');
</script>
```

### 3. 验证配置

1. 部署网站后，访问你的网站
2. 返回 Google Analytics
3. 在左侧菜单选择"报告" → "实时"
4. 如果看到当前访问者（你自己），说明配置成功！

---

## 📊 百度统计

### 1. 获取百度统计 ID

#### 步骤 1：注册百度统计
1. 访问 [百度统计](https://tongji.baidu.com/)
2. 使用百度账号登录（没有的话需要先注册）
3. 点击"管理" → "新增网站"

#### 步骤 2：添加网站
1. 输入**网站域名**：`YOUR_USERNAME.github.io`
2. 输入**网站首页**：`https://YOUR_USERNAME.github.io/YOUR_REPO/`
3. 选择**网站行业分类**：工具软件
4. 点击"确定"

#### 步骤 3：获取统计代码
1. 点击"代码获取"
2. 复制代码中的 **ID 部分**

代码类似：
```html
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?1234567890abcdef1234567890abcdef";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
```

**需要的是 `hm.js?` 后面的 ID：** `1234567890abcdef1234567890abcdef`

### 2. 配置到网站

在 `index.html` 中找到以下代码（约第 47-55 行）：

```html
<!-- 百度统计 -->
<script>
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?YOUR_BAIDU_TONGJI_ID";
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(hm, s);
    })();
</script>
```

**将 `YOUR_BAIDU_TONGJI_ID` 替换为你的实际统计 ID**

例如：
```html
hm.src = "https://hm.baidu.com/hm.js?1234567890abcdef1234567890abcdef";
```

### 3. 验证配置

1. 部署网站后，访问你的网站
2. 返回百度统计
3. 在左侧菜单选择"报告" → "实时访客"
4. 如果看到当前访问（你自己），说明配置成功！

通常需要等待 **20 分钟左右** 才能看到数据。

---

## ✅ 配置步骤总结

### 快速配置流程

1. **获取 Google Analytics ID**
   - 访问 https://analytics.google.com/
   - 创建媒体资源
   - 获取 `G-XXXXXXXXXX` ID

2. **获取百度统计 ID**
   - 访问 https://tongji.baidu.com/
   - 添加网站
   - 获取统计代码中的 ID

3. **修改 index.html**
   ```html
   <!-- 替换 Google Analytics ID -->
   gtag('config', 'G-YOUR-ACTUAL-ID');
   
   <!-- 替换百度统计 ID -->
   hm.src = "https://hm.baidu.com/hm.js?YOUR-ACTUAL-ID";
   ```

4. **推送代码**
   ```bash
   git add index.html
   git commit -m "feat: 添加统计代码"
   git push
   ```

5. **等待部署完成**（1-2 分钟）

6. **验证配置**
   - 访问你的网站
   - 检查统计后台是否有数据

---

## 📋 完整配置示例

### 配置前（默认）
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    gtag('config', 'G-XXXXXXXXXX');
</script>

<!-- 百度统计 -->
<script>
    hm.src = "https://hm.baidu.com/hm.js?YOUR_BAIDU_TONGJI_ID";
</script>
```

### 配置后（示例）
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123XYZ"></script>
<script>
    gtag('config', 'G-ABC123XYZ');
</script>

<!-- 百度统计 -->
<script>
    hm.src = "https://hm.baidu.com/hm.js?1234567890abcdef1234567890abcdef";
</script>
```

---

## 🔍 数据查看

### Google Analytics
- 实时数据：报告 → 实时
- 访问量：报告 → 流量获取
- 用户地理位置：报告 → 用户 → 用户属性 → 地理位置

### 百度统计
- 实时访客：报告 → 实时访客
- 今日数据：报告 → 趋势分析
- 来源分析：报告 → 来源分析
- 访问明细：报告 → 访问明细

---

## 💡 提示

### 隐私保护
- 统计代码只收集匿名访问数据
- 不会收集个人隐私信息
- 符合网站统计的常规做法

### 两个统计都要配置吗？
- **Google Analytics**：适合国际用户，功能强大
- **百度统计**：适合国内用户，更准确反映国内访问情况
- 建议**两个都配置**，获得更全面的数据

### 不配置会怎样？
- 网站功能完全正常
- 只是无法看到访问统计数据
- 如果不需要统计，可以删除相关代码

### 删除统计代码
如果不需要统计，可以删除 `index.html` 中的以下部分：
- 第 35-45 行：Google Analytics 代码
- 第 47-55 行：百度统计代码

---

## 🆘 常见问题

### Q1：为什么看不到数据？
**A：** 
1. 检查统计 ID 是否正确替换
2. 等待 20-30 分钟让数据同步
3. 确保访问的是部署后的线上网站（不是本地）
4. 检查浏览器是否安装了广告拦截插件

### Q2：本地开发时统计代码会工作吗？
**A：** 会，但建议在本地开发时先不配置统计 ID，避免测试数据污染真实数据。

### Q3：可以只配置一个统计吗？
**A：** 可以，配置哪个都行。不配置的那个可以删除或保留默认代码。

### Q4：统计代码会影响网站速度吗？
**A：** 影响很小，统计脚本都是异步加载的，不会阻塞页面渲染。

---

## 📚 相关链接

- [Google Analytics 官方文档](https://support.google.com/analytics)
- [百度统计官方文档](https://tongji.baidu.com/web/help/article?id=93)
- [Google Analytics 设置指南](https://support.google.com/analytics/answer/1008015)
- [百度统计安装步骤](https://tongji.baidu.com/web/help/article?id=174)

---

## ✅ 配置完成检查

- [ ] 已注册 Google Analytics 账号
- [ ] 已获取 Google Analytics Measurement ID（G-XXXXXXXXXX）
- [ ] 已在 index.html 中替换 Google Analytics ID
- [ ] 已注册百度统计账号
- [ ] 已获取百度统计 ID
- [ ] 已在 index.html 中替换百度统计 ID
- [ ] 已推送代码到 GitHub
- [ ] 已访问网站测试
- [ ] 已在统计后台看到数据（等待 20-30 分钟）

---

**配置完成后，你就可以看到网站的访问数据了！** 📊✨

祝你统计数据节节高升！🚀

