#!/bin/bash

# 名字生成器 GitHub Pages 部署脚本
# 使用方法：bash deploy.sh "提交信息"

# 检查是否提供了提交信息
if [ -z "$1" ]; then
    echo "❌ 请提供提交信息"
    echo "使用方法: bash deploy.sh \"你的提交信息\""
    exit 1
fi

echo "🚀 开始部署到 GitHub Pages..."

# 添加所有更改
echo "📦 添加文件..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "$1"

# 推送到远程仓库
echo "⬆️  推送到 GitHub..."
git push

echo "✅ 部署完成！GitHub Actions 将自动构建和部署你的网站。"
echo "📊 查看部署进度：https://github.com/YOUR_USERNAME/YOUR_REPO/actions"
echo ""
echo "⏳ 请等待 1-2 分钟后访问你的网站"

