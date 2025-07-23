# 导入os包
import os
import subprocess
from registry_utils import get_enhanced_obsidian_paths

# 替换obsidian.json中的冗余字符串
try:
    obsidian_config_path = os.path.join(os.getenv("APPDATA"), 'obsidian', 'obsidian.json')
    if os.path.exists(obsidian_config_path):
        with open(obsidian_config_path, 'r', encoding="utf-8") as file:
            content = file.read()
        replaced_content = content.replace(',"open":true', '')
        with open(obsidian_config_path, 'w', encoding="utf-8") as file:
            file.write(replaced_content)
        print("[成功] 配置文件已修改")
    else:
        print("[警告] 未找到obsidian.json配置文件")
except Exception as e:
    print(f"[错误] 修改配置文件失败: {e}")

# 启动obsidian - 使用增强的路径查找
print("\n检查Obsidian安装路径...")
print("=" * 40)

# 使用注册表增强的路径查找
OBSIDIAN_PATHS = get_enhanced_obsidian_paths()

path_found = False
for i, path in enumerate(OBSIDIAN_PATHS, 1):
    print(f"正在检查路径 {i}: {path}")
    if os.path.exists(path):
        print(f"[成功找到] {path}")
        print("即将启动Obsidian...")
        subprocess.Popen([path], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("启动命令已执行")
        path_found = True
        break
    else:
        print(f"[未找到] {path}")
    print()

if not path_found:
    print("所有路径都未找到Obsidian")
    print("请检查Obsidian是否已正确安装")
else:
    print("\n" + "=" * 40)
    print("成功启动Obsidian！")
    print("=" * 40)