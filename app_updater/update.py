import requests
import zipfile
import os
import shutil
import subprocess
import time
from tkinter import messagebox, Tk

# === Настройки ===
SERVER_VERSION_URL = "https://fridem-code.github.io/app-distribution/version.txt"   # замени
SERVER_APP_URL = "https://fridem-code.github.io/app-distribution/app.zip"           # замени
LOCAL_VERSION_FILE = "version.txt"
APP_EXECUTABLE = "app.exe"
ZIP_FILE = "app.zip"

def show_error(msg):
    root = Tk()
    root.withdraw()
    messagebox.showerror("Ошибка", msg)
    root.destroy()

def get_local_version():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0.0"
    with open(LOCAL_VERSION_FILE, "r") as f:
        return f.read().strip()

def get_server_version():
    try:
        r = requests.get(SERVER_VERSION_URL)
        if r.status_code == 200:
            return r.text.strip()
    except Exception as e:
        show_error(f"Не удалось получить версию: {e}")
    return None

def download_new_version():
    try:
        with requests.get(SERVER_APP_URL, stream=True) as r:
            with open(ZIP_FILE, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        show_error(f"Ошибка скачивания: {e}")

def install_update():
    try:
        with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
            zip_ref.extractall()
        os.remove(ZIP_FILE)
    except Exception as e:
        show_error(f"Ошибка установки: {e}")

def run_app():
    subprocess.Popen([APP_EXECUTABLE])
    time.sleep(1)

def main():
    local_version = get_local_version()
    server_version = get_server_version()

    if not server_version:
        run_app()
        return

    if server_version != local_version:
        root = Tk()
        root.withdraw()
        confirm = messagebox.askyesno("Обновление", f"Доступна новая версия {server_version}. Обновить?")
        root.destroy()
        if confirm:
            download_new_version()
            install_update()
            with open(LOCAL_VERSION_FILE, "w") as f:
                f.write(server_version)
    run_app()

if __name__ == "__main__":
    main()