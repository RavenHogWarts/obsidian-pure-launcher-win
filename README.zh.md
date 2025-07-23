> 中文 | [English](README.md)

# Obsidian Pure Launcher

一个用于优化 Obsidian 启动体验的小工具，自动修正配置并启动 Obsidian。

> **注意：本项目及生成的 EXE 仅适用于 Windows 系统。**

## 功能简介

- 自动修正 `%APPDATA%\obsidian\obsidian.json` 文件中的冗余字符串（去除 `,"open":true`）。
- 自动检测并启动本地已安装的 Obsidian 客户端。
- 支持 Windows 下一键打包为单文件 EXE。

## 依赖环境

- Windows 操作系统
- Python 3.7 及以上
- pip
- pyinstaller（首次打包时自动安装）

## 目录结构

```
obsidian-pure-launch-win/
├── assets/                # 资源文件目录
│   └── app-icon.ico       # 应用图标
├── build/                 # 打包临时目录（自动生成，打包后会自动清理）
├── dist/                  # 打包后输出目录（自动生成）
├── src/
│   ├── main.py            # 主程序入口
│   └── build.bat          # 一键打包脚本
├── README.md              # 项目说明
```

## 打包方法

1. 确保已安装 Python 3 和 pip（可在命令行输入 `python --version` 和 `pip --version` 检查）。
2. 进入 `src` 目录，双击或在命令行运行 `.\build.bat`。
3. 首次打包会自动安装 pyinstaller，安装完成后脚本会自动重启并继续打包，无需手动分步操作。
4. 打包完成后，EXE 文件会输出到 `dist` 目录。

## 使用说明

1. 运行打包生成的 `obsidian-pure-launcher.exe`（仅限 Windows）。
2. 程序会自动修正 Obsidian 配置文件并尝试启动 Obsidian 客户端。
3. 若未检测到 Obsidian，请检查其安装路径是否为：
   - `C:\Users\你的用户名\AppData\Local\Obsidian\Obsidian.exe`
   - `C:\Program Files\Obsidian\Obsidian.exe`

## 贡献

欢迎提交 issue 和 PR 改进本项目。
