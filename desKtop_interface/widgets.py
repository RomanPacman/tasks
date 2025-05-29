import tkinter as tk
from tkinter import ttk
from config import *


class CryptoTable(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._sort_directions = {}
        self._create_table()

    def _create_table(self):
        # Настройка стиля для тёмной таблицы
        style = ttk.Style()
        style.configure("Treeview",
                        background=ENTRY_COLOR,
                        foreground=FG_COLOR,
                        fieldbackground=ENTRY_COLOR,
                        font=FONT_MAIN
                        )
        style.map("Treeview", background=[('selected', ACCENT_COLOR)])

        style.configure("Treeview.Heading",
                        background=TABLE_HEADER_COLOR,
                        foreground=FG_COLOR,
                        font=FONT_BOLD
                        )

        self["columns"] = ("id", "pair", "price", "delta", "change")
        self.column("#0", width=0, stretch=tk.NO)

        # Настройка колонок с привязкой сортировки
        columns = {
            "id": {"width": 50, "anchor": tk.CENTER, "type": "num"},
            "pair": {"width": 120, "anchor": tk.W, "type": "str"},
            "price": {"width": 100, "anchor": tk.E, "type": "num"},
            "delta": {"width": 80, "anchor": tk.E, "type": "num"},
            "change": {"width": 80, "anchor": tk.E, "type": "num"}
        }

        for col, params in columns.items():
            self.column(col, **{k: v for k, v in params.items() if k in ["width", "anchor"]})
            self.heading(col, text=col.capitalize(),
                         command=lambda c=col, t=params["type"]: self._sort_column(c, t))

        self._insert_demo_data()

    def _sort_column(self, column, data_type):
        """Сортировка колонки с переключением направления"""
        # Определяем направление сортировки
        if column not in self._sort_directions:
            self._sort_directions[column] = True  # По возрастанию

        direction = self._sort_directions[column]
        self._sort_directions[column] = not direction  # Переключаем

        # Получаем все данные
        data = [(self.set(item, column), item) for item in self.get_children("")]

        # Сортируем в зависимости от типа данных
        if data_type == "num":
            # Для числовых значений (удаляем лишние символы)
            data.sort(key=lambda x: float(x[0].replace('%', '').replace('+', '').replace(',', '')),
                      reverse=not direction)
        else:
            # Для строковых значений
            data.sort(reverse=not direction)

        # Перемещаем элементы в отсортированном порядке
        for index, (_, item) in enumerate(data):
            self.move(item, "", index)

        # Обновляем стрелки сортировки
        self._update_sort_indicators(column, direction)

    def _update_sort_indicators(self, column, ascending):
        """Обновление индикаторов сортировки в заголовках"""
        for col in self["columns"]:
            self.heading(col, text=col.capitalize())

        arrow = " ↑" if ascending else " ↓"
        self.heading(column, text=column.capitalize() + arrow)

    def _insert_demo_data(self):
        demo_pairs = [
            ("BTC/USDT", 42356.78, +1254.32, +3.05),
            ("ETH/USDT", 2987.45, -45.21, -1.49),
            ("SOL/USDT", 142.67, +8.32, +6.19),
            ("ADA/USDT", 1.25, -0.03, -2.34),
            ("DOT/USDT", 9.87, +0.45, +4.78),
            ("AVAX/USDT", 56.23, -2.11, -3.61),
            ("MATIC/USDT", 1.89, +0.12, +6.78),
            ("ATOM/USDT", 32.45, -1.23, -3.65),
            ("LINK/USDT", 18.76, +0.89, +4.99),
            ("XRP/USDT", 0.75, -0.01, -1.32)
        ]

        for i, (pair, price, delta, change) in enumerate(demo_pairs, 1):
            tag = 'up' if delta >= 0 else 'down'
            self.insert("", tk.END, values=(i, pair, f"{price:,.2f}", f"{delta:+.2f}", f"{change:+.2f}%"), tags=(tag,))

        # Цвета для положительных/отрицательных значений
        self.tag_configure('up', foreground='#4CAF50')  # Зелёный
        self.tag_configure('down', foreground='#F44336')  # Красный

class GraphPlaceholder(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._create_widgets()

    def _create_widgets(self):
        label = ttk.Label(self, text="Тут будет график", font=FONT_BOLD)
        label.pack(expand=True)