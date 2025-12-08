@echo off
REM 名字生成器 GitHub Pages 部署脚本（Windows 版本）
REM 使用方法：deploy.bat "提交信息"

if "%~1"=="" (
    echo ❌ 请提供提交信息
    echo 使用方法: deploy.bat "你的提交信息"
    exit /b 1
)

echo 🚀 开始部署到 GitHub Pages...

REM 添加所有更改
echo 📦 添加文件...
git add .

REM 提交更改
echo 💾 提交更改...
git commit -m "%~1"

REM 推送到远程仓库
echo ⬆️ 推送到 GitHub...
git push

echo.
echo ✅ 部署完成！GitHub Actions 将自动构建和部署你的网站。
echo 📊 在浏览器中查看部署进度
echo.
echo ⏳ 请等待 1-2 分钟后访问你的网站
pause

