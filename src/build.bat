chcp 65001
@echo off
REM 切换到当前脚本所在目录，确保相对路径正确
cd /d %~dp0

REM 设置项目根目录变量，指向src的上级目录（即项目根目录）
set ROOTDIR=%~dp0..\

REM 检查 pyinstaller 是否已安装，若未安装则自动安装并重启脚本
py -m PyInstaller --version >nul 2>nul
if %errorlevel% neq 0 (
    echo 未检测到 pyinstaller，正在安装...
    py -m pip install pyinstaller
    echo pyinstaller 安装完成，正在重启打包脚本...
    "%~f0"
    exit /b
) else (
    echo 已检测到 pyinstaller，跳过安装。
)

REM 显示当前目录，便于调试
cd
REM 显示 pyinstaller 的实际路径，便于确认环境
where pyinstaller

REM 开始打包，指定输出目录、工作目录和spec文件目录都在项目根目录
REM --onefile：生成单文件exe
REM --windowed：无控制台窗口
REM --name：指定生成的exe名称
REM --icon：指定exe图标
REM --distpath：输出目录
REM --workpath：临时工作目录
REM --specpath：spec文件目录
py -m PyInstaller --onefile --windowed --name obsidian-pure-launcher --icon %ROOTDIR%assets\app-icon.ico --distpath %ROOTDIR%dist --workpath %ROOTDIR%build --specpath %ROOTDIR%build main.py

REM 清理build中间文件夹，dist目录和exe保留
if exist %ROOTDIR%build rmdir /s /q %ROOTDIR%build
REM 清理spec文件
if exist obsidian-pure-launcher.spec del obsidian-pure-launcher.spec

echo 打包完成！EXE 已输出到 dist 目录

@REM pause