import tkinter as tk
from tkinter import ttk
import time
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Цвета темы (можно менять под свои предпочтения)
BG_COLOR = "#2e2e2e"  # Тёмно-серый (фон окна)
FG_COLOR = "#ffffff"  # Белый (текст)
BUTTON_COLOR = "#3c3f41"  # Цвет кнопок
ENTRY_COLOR = "#3c3f41"  # Цвет полей ввода
HOVER_COLOR = "#4e5254"  # Цвет кнопки при наведении



def on_button_click():
    """Обработчик нажатия кнопки"""
    input_text = entry.get()  # Получаем текст из поля ввода
    label_result.config(text=f"Вы ввели: {input_text}")

def clear_input():
    """Очистка поля ввода"""
    entry.delete(0, tk.END)
    label_result.config(text="")

def update_time():
    """Обновляет время в метке каждую секунду"""
    current_time = time.strftime("%H:%M:%S")  # Получаем текущее время
    label_time.config(text=f"Текущее время: {current_time}")
    root.after(1000, update_time)  # Через 1000 мс (1 сек) снова вызываем update_time

# Создаем главное окно
root = tk.Tk()
root.title("Криптовалютный анализатор")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")  # Базовый стиль ('clam' лучше подходит для кастомизации)

# Настройка стилей
style.configure(".", background=BG_COLOR, foreground=FG_COLOR)  # Общий стиль
style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Arial", 12))
style.configure("TButton", background=BUTTON_COLOR, foreground=FG_COLOR, font=("Arial", 10))
style.map("TButton", background=[("active", HOVER_COLOR)])  # Цвет при наведении
style.configure("TEntry", fieldbackground=ENTRY_COLOR, foreground=FG_COLOR, insertbackground=FG_COLOR)


# Метка (Label)
label = ttk.Label(root, text="Введите название криптовалюты:")
label.pack(pady=10)

# Поле ввода (Entry)
entry = ttk.Entry(root, width=30)
entry.pack(pady=5)

crypto_list = ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)", "Solana (SOL)", "Polkadot (DOT)"]

combo = ttk.Combobox(root, values=crypto_list)
combo.pack(pady=10)
combo.set("Bitcoin (BTC)")
style.configure("TCombobox",
    fieldbackground=ENTRY_COLOR,
    background=ENTRY_COLOR,
    foreground=FG_COLOR,
    insertcolor=FG_COLOR
)

# Создаем Combobox с темным стилем
combo = ttk.Combobox(root, values=crypto_list, style="TCombobox")


# Кнопка для обработки ввода
button = ttk.Button(root, text="Получить данные", command=on_button_click)
button.pack(pady=5)
button.place(x=100, y=50, width=200, height=40)

label_time = ttk.Label(root, text="Текущее время: ", font=("Arial", 14))
label_time.pack(pady=20)

# Кнопка для очистки
button_clear = ttk.Button(root, text="Очистить", command=clear_input)
button_clear.pack(pady=5)

# Метка для вывода результата
label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

# Область для графика (пока заглушка)
frame_plot = ttk.Frame(root, height=300, width=700, relief=tk.SUNKEN)
frame_plot.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
frame_plot.pack_propagate(False)  # Фиксируем размер

# Заглушка графика (Matplotlib)
# fig, ax = plt.subplots(figsize=(7, 3))
# ax.set_title("График цены (здесь будет график)")
# canvas = FigureCanvasTkAgg(fig, master=frame_plot)
# canvas.draw()
# canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
update_time()
# Запуск приложения
root.mainloop()