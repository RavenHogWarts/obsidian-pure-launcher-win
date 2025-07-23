> English | [中文](README.zh.md)

# Obsidian Pure Launcher

A small tool to optimize the Obsidian launch experience by automatically fixing configuration and launching Obsidian.

> **Note: This project and the generated EXE are for Windows only.**

## Features

- Automatically fixes redundant strings (removes `,"open":true`) in `%APPDATA%\obsidian\obsidian.json`.
- Automatically detects and launches the locally installed Obsidian client.
- Supports one-click packaging into a single EXE file for Windows.

## Requirements

### For Direct Usage (Method 1)
- Windows OS
- No additional dependencies required

### For Building EXE (Method 2)
- Windows OS
- Python 3.7 or above
- pip
- pyinstaller (will be installed automatically on first build)

## Project Structure

```
obsidian-pure-launcher-win/
├── assets/                    # Resource files
│   └── app-icon.ico          # Application icon
├── build/                    # Temporary build directory (auto-generated, auto-cleaned after build)
├── dist/                     # Output directory for packaged EXE (auto-generated)
├── src/
│   ├── main.py               # Main program entry
│   ├── registry_utils.py     # Registry utilities
│   └── build.bat             # One-click build script
├── start_obsidian.bat        # Direct launcher (silent mode, no Python required)
├── start_obsidian_console.bat # Direct launcher (console mode, no Python required)
├── README.md                 # Project documentation (English)
└── README.zh.md              # Project documentation (Chinese)
```

## Usage Methods

This project provides two usage methods to launch Obsidian:

### Method 1: Direct Usage (No Python Required)

**Recommended for most users** - No Python installation required.

#### Quick Start
- **Silent Mode**: Double-click `start_obsidian.bat` to launch Obsidian directly without console output.
- **Console Mode**: Double-click `start_obsidian_console.bat` to launch with detailed console output for debugging.

Both methods will:
- Automatically fix the Obsidian configuration file (`%APPDATA%\obsidian\obsidian.json`)
- Detect and launch the locally installed Obsidian client

#### Supported Installation Paths
- `%LOCALAPPDATA%\Obsidian\Obsidian.exe` (User installation)
- `%PROGRAMFILES%\Obsidian\Obsidian.exe` (System installation)
- `%PROGRAMFILES(X86)%\Obsidian\Obsidian.exe` (32-bit installation)
- `%PROGRAMW6432%\Obsidian\Obsidian.exe` (64-bit installation)
- Any path where `obsidian.exe` is in system PATH

### Method 2: Build EXE (Python Required)

For developers or users who prefer a single executable file.

#### Requirements for Building
- Windows OS
- Python 3.7 or above
- pip
- pyinstaller (will be installed automatically on first build)

#### Build Instructions
1. Make sure Python 3 and pip are installed (check with `python --version` and `pip --version`).
2. Go to the `src` directory and run `.\build.bat` by double-clicking or from the command line.
3. On first build, pyinstaller will be installed automatically. The script will then restart and continue building, no manual steps required.
4. After building, the EXE file will be output to the `dist` directory.

#### Using the Built EXE
1. Run the generated `obsidian-pure-launcher.exe` (Windows only).
2. The program will automatically fix the Obsidian configuration file and attempt to launch the Obsidian client.
3. If Obsidian is not detected, please check if it is installed at one of the supported paths listed above.

## Contributing

Contributions are welcome! Please submit issues and pull requests to help improve this project.
