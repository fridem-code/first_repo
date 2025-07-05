import zipfile
import os

APP_EXE = "app.exe"
VERSION = "1.0.6"
ZIP_NAME = "app.zip"

# Создаем версию
with open("version.txt", "w") as f:
    f.write(VERSION)

if os.path.exists(ZIP_NAME):
    os.remove(ZIP_NAME)

with zipfile.ZipFile(ZIP_NAME, 'w') as zipf:
    zipf.write(APP_EXE)
    zipf.write("version.txt")

print(f"[✓] Архив {ZIP_NAME} успешно создан.")