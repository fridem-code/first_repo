import pyautogui
import time
import threading
import customtkinter as ctk
import keyboard  # Для отслеживания нажатий клавиш
import json


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Мой кликер. BETA')
        self.geometry('400x400')
        self.center_window()

        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color='transparent')
        self.main_frame.pack(anchor='center', expand=True)

        self.start_btn = ctk.CTkButton(self.main_frame, text='Запустить', command=self.start_clicker)
        self.start_btn.pack()

        self.interval_entry = ctk.CTkEntry(self.main_frame, placeholder_text='0.01')
        self.interval_entry.pack(pady=5)

        self.stop_button = ctk.CTkButton(self.main_frame, text="Остановить", command=self.stop_clicker)
        self.stop_button.pack(pady=5)

        self.exit_button = ctk.CTkButton(self.main_frame, text="Выход", command=self.quit)
        self.exit_button.pack(pady=5)

        ctk.set_appearance_mode("dark")  # Устанавливаем темную тему
        ctk.set_default_color_theme("blue")  # Устанавливаем цветовую тему

        self.start_app()

    def center_window(self):
        w = 400
        h = 400

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def clicker(self, click_interval):
        """Функция для выполнения кликов мыши с заданным интервалом."""
        while self.running:
            pyautogui.click()  # Выполняем клик
            time.sleep(click_interval)  # Пауза между кликами

    def start_clicker(self):
        try:
            click_interval = float(self.interval_entry.get())  # Получаем интервал из поля
        except ValueError:
            print("Некорректный интервал. Введите число.")
            return

        self.running = True
        clicking_thread = threading.Thread(target=self.clicker, args=(click_interval,))
        clicking_thread.start()
        # Запускаем поток для проверки нажатия клавиши 'q' только при запуске кликера
        self.check_stop_thread()

    def check_stop_key(self):
        """Функция для остановки кликера по нажатию клавиши 'q'."""
        while self.running:
            if keyboard.is_pressed('q'):  # Если нажата клавиша 'q'
                self.stop_clicker()  # Останавливаем кликер
                print("Кликер остановлен нажатием 'q'.")
                break  # Выходим из цикла

    def check_stop_thread(self):
        """Запуск потока для проверки клавиши остановки."""
        stop_thread = threading.Thread(target=self.check_stop_key)
        stop_thread.daemon = True  # Делая поток демоном, он закрывается при закрытии основного окна
        stop_thread.start()

    def stop_clicker(self):
        global running
        running = False

    # Функция для остановки кликера
    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                config = f.read()
                config_data = json.loads(config)
                interval_click_time = config_data['interval_click_time']
        except json.JSONDecodeError as exc:
            print(f'Возникла ошибка чтение config.json:\n{exc}')

    def start_app(self):
        # Переменная для контроля состояния кликера
        self.running = False


if __name__ == '__main__':
    app = App()
    app.mainloop()

print("Программа завершена.")
