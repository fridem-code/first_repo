import zipfile
import os

APP_FOLDER = "app"
VERSION = "1.0.6"
ZIP_NAME = "app.zip"
folder_path = f'D:/Python/git_loc/app_updater/output/{APP_FOLDER}'
output_path = f'D:/Python/git_loc/app_updater/output/{ZIP_NAME}'

# Создаем версию
with open("version.txt", "w") as f:
    f.write(VERSION)

if os.path.exists(ZIP_NAME):
    os.remove(ZIP_NAME)

with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, folder_path)
            zipf.write(abs_path, rel_path)

print(f"[✓] Архив {ZIP_NAME} успешно создан.")