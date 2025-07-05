import tkinter as tk
from tkinter import messagebox

# Функции для кнопок
def on_button1_click():
    messagebox.showinfo("Кнопка 1", "Вы нажали на Кнопку 1!")

def on_button2_click():
    messagebox.showinfo("Кнопка 2", "Вы нажали на Кнопку 2!")

# Создаем главное окно
root = tk.Tk()
root.title("Пример приложения")
root.geometry("300x150")  # Размер окна

# Создаем кнопки
button1 = tk.Button(root, text="Кнопка 1", command=on_button1_click)
button1.pack(pady=10)

button2 = tk.Button(root, text="Кнопка 2", command=on_button2_click)
button2.pack(pady=10)

button3 = tk.Button(root, text="Кнопка 3", command=on_button2_click)
button3.pack(pady=10)

button4 = tk.Button(root, text="Кнопка 4", command=on_button2_click)
button4.pack(pady=10)


# Запускаем главный цикл
root.mainloop()
