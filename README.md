> English | [中文](README.zh.md)

# Obsidian Pure Launcher

A small tool to optimize the Obsidian launch experience by automatically fixing configuration and launching Obsidian.

> **Note: This project and the generated EXE are for Windows only.**

## Features

- Automatically fixes redundant strings (removes `,"open":true`) in `%APPDATA%\obsidian\obsidian.json`.
- Automatically detects and launches the locally installed Obsidian client.
- Supports one-click packaging into a single EXE file for Windows.

## Requirements

- Windows OS
- Python 3.7 or above
- pip
- pyinstaller (will be installed automatically on first build)

## Project Structure

```
obsidian-pure-launch-win/
├── assets/                # Resource files
│   └── app-icon.ico       # Application icon
├── build/                 # Temporary build directory (auto-generated, auto-cleaned after build)
├── dist/                  # Output directory for packaged EXE (auto-generated)
├── src/
│   ├── main.py            # Main program entry
│   └── build.bat          # One-click build script
├── README.md              # Project documentation
```

## Build Instructions

1. Make sure Python 3 and pip are installed (check with `python --version` and `pip --version`).
2. Go to the `src` directory and run `.\build.bat` by double-clicking or from the command line.
3. On first build, pyinstaller will be installed automatically. The script will then restart and continue building, no manual steps required.
4. After building, the EXE file will be output to the `dist` directory.

## Usage

1. Run the generated `obsidian-pure-launcher.exe` (Windows only).
2. The program will automatically fix the Obsidian configuration file and attempt to launch the Obsidian client.
3. If Obsidian is not detected, please check if it is installed at one of the following paths:
   - `C:\Users\YourUsername\AppData\Local\Obsidian\Obsidian.exe`
   - `C:\Program Files\Obsidian\Obsidian.exe`

## Contributing

Contributions are welcome! Please submit issues and pull requests to help improve this project.
