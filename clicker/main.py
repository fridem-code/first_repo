import pyautogui
import keyboard
import time
import threading

# Переменная для контроля состояния кликера
running = True

def clicker():
    """Функция для выполнения кликов мыши."""
    while running:
        pyautogui.click()  # Выполняем клик
        time.sleep(0.01)   # Пауза между кликами (настройте по необходимости)

def stop_clicker(e):
    """Функция для остановки кликера."""
    global running
    running = False
    print("Кликер остановлен.")

# Установите слушатель нажатия клавиш
keyboard.add_hotkey('q', stop_clicker)

# Запускаем кликер в отдельном потоке
clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()

print("Кликер запущен. Нажмите 'q' для остановки.")
clicking_thread.join()  # Ждем завершения потока кликера
print("Программа завершена.")
