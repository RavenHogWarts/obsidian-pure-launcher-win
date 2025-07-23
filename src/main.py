# 导入os包
import os
import subprocess

# 替换obsidian.json中的冗余字符串
with open(os.getenv("APPDATA") + '\obsidian\obsidian.json', 'r', encoding="utf-8") as file:
    content = file.read()
replaced_content = content.replace(',"open":true', '')
with open(os.getenv("APPDATA") + '\obsidian\obsidian.json', 'w', encoding="utf-8") as file:
    file.write(replaced_content)

# 启动obsidian
# os.system('start C:\\Users\\' + os.getlogin() + '\\AppData\\Local\\Obsidian\\Obsidian.exe')
# os.system(r'start "" "C:\Program Files\Obsidian\Obsidian.exe"')

OBSIDIAN_PATHS = [
    fr'C:\Users\{os.getlogin()}\AppData\Local\Obsidian\Obsidian.exe',
    r'C:\Program Files\Obsidian\Obsidian.exe'
]

for path in OBSIDIAN_PATHS:
    if os.path.exists(path):
        # os.system(f'start "" "{path}"')
        subprocess.Popen([path], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        break
else:
    # print("Obsidian 未找到，请检查安装路径。")
    pass  # 可加提示或日志