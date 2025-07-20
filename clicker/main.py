import pyautogui
import time
import threading
import customtkinter as ctk
import keyboard  # Для отслеживания нажатий клавиш
import json

# Переменная для контроля состояния кликера
running = False

def clicker(click_interval):
    """Функция для выполнения кликов мыши с заданным интервалом."""
    global running
    while running:
        pyautogui.click()  # Выполняем клик
        time.sleep(click_interval)  # Пауза между кликами

# Функция для запуска кликера
def start_clicker():
    global running
    click_interval = float(interval_entry.get())  # Получаем интервал из поля
    running = True
    clicking_thread = threading.Thread(target=clicker, args=(click_interval,))
    clicking_thread.start()
    # Запускаем поток для проверки нажатия клавиши 'q' только при запуске кликера
    check_stop_thread()

def check_stop_key():
    """Функция для остановки кликера по нажатию клавиши 'q'."""
    while running:
        if keyboard.is_pressed('q'):  # Если нажата клавиша 'q'
            stop_clicker()  # Останавливаем кликер
            print("Кликер остановлен нажатием 'q'.")
            break  # Выходим из цикла

def check_stop_thread():
    """Запуск потока для проверки клавиши остановки."""
    stop_thread = threading.Thread(target=check_stop_key)
    stop_thread.daemon = True  # Делая поток демоном, он закрывается при закрытии основного окна
    stop_thread.start()

# Функция для остановки кликера
def stop_clicker():
    global running
    running = False


def load_config():
    try:
        with open('config.json', 'r')as f:
            config = f.read()
            config_data = json.loads(config)
            interval_click_time = config_data['interval_click_time']
    except json.JSONDecodeError as exc:
        print(f'Возникла ошибка чтение config.json:\n{exc}')

# Создаем корневое окно
ctk.set_appearance_mode("dark")  # Устанавливаем темную тему
ctk.set_default_color_theme("blue")  # Устанавливаем цветовую тему

root = ctk.CTk()  # Создаем экземпляр окна
root.title("Супер быстрый кликер")

# Создаем элементы интерфейса
title_label = ctk.CTkLabel(root, text="Супер быстрый кликер")
title_label.pack(pady=10)

interval_label = ctk.CTkLabel(root, text="Интервал клика (секунды):")
interval_label.pack(pady=5)

interval_entry = ctk.CTkEntry(root, placeholder_text="0.01")
interval_entry.pack(pady=5)

start_button = ctk.CTkButton(root, text="Запустить", command=start_clicker)
start_button.pack(pady=5)

stop_button = ctk.CTkButton(root, text="Остановить", command=stop_clicker)
stop_button.pack(pady=5)

exit_button = ctk.CTkButton(root, text="Выход", command=root.quit)
exit_button.pack(pady=5)

# Запускаем основной цикл обработки событий
root.mainloop()

print("Программа завершена.")
