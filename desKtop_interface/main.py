import tkinter as tk
from tkinter import ttk
from config import *
from widgets import CryptoTable, GraphPlaceholder
from db_stubs import *


class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Crypto Trading App")
        self.geometry("1200x800")
        self.configure(bg=BG_COLOR)
        self._setup_style()
        self._create_widgets()

    def _setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background=BG_COLOR, foreground=FG_COLOR)
        style.configure("TButton", background=ENTRY_COLOR, font=FONT_MAIN)
        style.map("TButton", background=[("active", ACCENT_COLOR)])
        style.configure("TEntry", fieldbackground=ENTRY_COLOR, insertcolor=FG_COLOR)
        style.configure("TCombobox", fieldbackground=ENTRY_COLOR)

    def _create_widgets(self):
        # Левая часть: таблица (30% ширины)
        table_frame = ttk.Frame(self, width=self.winfo_screenwidth() * TABLE_WIDTH_PERCENT)
        table_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.table = CryptoTable(table_frame)
        self.table.pack(fill=tk.BOTH, expand=True)

        # Правая часть: график и управление
        right_frame = ttk.Frame(self)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # График (30% высоты)
        graph_frame = ttk.Frame(right_frame, height=self.winfo_screenheight() * GRAPH_HEIGHT_PERCENT)
        graph_frame.pack(fill=tk.X)
        self.graph = GraphPlaceholder(graph_frame)
        self.graph.pack(fill=tk.BOTH, expand=True)

        # Информация о монете
        info_frame = ttk.Frame(right_frame)
        info_frame.pack(fill=tk.X, pady=10)

        ttk.Label(info_frame, text=f"Текущая монета: {get_current_coin()}", font=FONT_MAIN).pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Текущий курс: {get_current_price():,.2f} USDT", font=FONT_MAIN).pack(anchor=tk.W)
        ttk.Label(info_frame, text=f"Баланс: {get_wallet_balance():,.2f} USDT", font=FONT_MAIN).pack(anchor=tk.W)

        # Формы управления
        self._create_controls(right_frame)

    def _create_controls(self, parent):
        control_frame = ttk.Frame(parent)
        control_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 1. Внести средства
        ttk.Label(control_frame, text="Сумма $:").grid(row=0, column=0, sticky=tk.W)
        amount_entry = ttk.Entry(control_frame)
        amount_entry.grid(row=0, column=1, sticky=tk.EW)

        users_combo = ttk.Combobox(control_frame, values=["Рома", "Юра", "Вася"], state="readonly")
        users_combo.grid(row=0, column=2, padx=5)
        users_combo.set("Рома")

        ttk.Button(control_frame, text="Внести", command=lambda: insert_transaction(
            float(amount_entry.get()),
            users_combo.get()
        )).grid(row=0, column=3)

        # 2. Вывод
        ttk.Label(control_frame, text="Вывод монет:").grid(row=1, column=0, sticky=tk.W)
        withdraw_entry = ttk.Entry(control_frame)
        withdraw_entry.grid(row=1, column=1, sticky=tk.EW)
        ttk.Button(control_frame, text="Вывести", command=lambda: withdraw_coins(
            float(withdraw_entry.get())
        )).grid(row=1, column=3)

        # 3. Обмен
        self.exchange_var = tk.BooleanVar(value=False)
        ttk.Button(control_frame, text="Разрешить обмен", command=self._toggle_exchange).grid(row=2, column=0)
        self.exchange_indicator = ttk.Label(control_frame, text="❌ Запрещено", foreground="red")
        self.exchange_indicator.grid(row=2, column=1, sticky=tk.W)

        # 4-6. Настройки
        self._create_setting_row(control_frame, 3, "Граница обмена", "50000")
        self._create_setting_row(control_frame, 4, "Минимальная граница", "100")
        self._create_setting_row(control_frame, 5, "% отката", "5")

    # def _create_setting_row(self, frame, row, label, default):
    #     ttk.Label(frame, text=f"{label}:").grid(row=row, column=0, sticky=tk.W)
    #     entry = ttk.Entry(frame)
    #     entry.insert(0, default)
    #     entry.grid(row=row, column=1, sticky=tk.EW)
    #     ttk.Button(frame, text="Изменить", command=lambda: update_exchange_threshold(
    #         float(entry.get())
    #     ).grid(row=row, column=3))

    def _toggle_exchange(self):
        toggle_exchange_allowed()
        new_state = not self.exchange_var.get()
        self.exchange_var.set(new_state)
        if new_state:
            self.exchange_indicator.config(text="✅ Разрешено", foreground="green")
        else:
            self.exchange_indicator.config(text="❌ Запрещено", foreground="red")

    def _create_setting_row(self, frame, row, label, default):
        ttk.Label(frame, text=f"{label}:").grid(row=row, column=0, sticky=tk.W)

        # Поле ввода
        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky=tk.EW)

        # Label для отображения значения
        value_label = ttk.Label(frame, text=default, font=FONT_MAIN)
        value_label.grid(row=row, column=2, sticky=tk.W, padx=5)

        # Кнопка "Изменить" с правильным lambda
        ttk.Button(frame,
                   text="Изменить",
                   command=lambda l=label.lower(), e=entry, vl=value_label: self._update_setting(l, e.get(), vl)
                   ).grid(row=row, column=3, padx=5)

    def _update_setting(self, setting_name, value, value_label=None):
        """Обновление настроек с изменением Label"""
        try:
            value = float(value)
            print(f"Изменение {setting_name} на {value}")

            # Обновляем Label если он передан
            if value_label:
                value_label.config(text=str(value))

            # Логика обновления параметров
            if setting_name == "граница обмена":
                update_exchange_threshold(value)
            elif setting_name == "минимальная граница":
                print("Минимальная граница изменена")
            elif setting_name == "% отката":
                print("Процент отката изменён")

        except ValueError:
            print("Ошибка: введите число")


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()