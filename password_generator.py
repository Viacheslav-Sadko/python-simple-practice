import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

app_width = 600
app_height = 400
app_x = 450
app_y = 200

class PasswordGeneratorApp:
    def __init__(self, root, width = app_width, height = app_height, x = app_x, y = app_y, icon = "icon.ico"):
        # Налаштування вікна
        self.root = root
        self.root.iconbitmap(icon)
        self.root.title("Password Generator")
        self.root.resizable = (False, False)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Налаштування текстового поля
        tk.Label(root, text = "Довжина паролю:", font = ("Arial", 14)).pack(pady = 10)

        # Налаштування поля для вводу і відступи між полями
        self.length_entry = tk.Entry(root, font = ("Arial", 12), width = 10, justify = "center")
        self.length_entry.pack(pady = 5)

        # Параметри для чек-боксів
        self.include_uppercase = tk.BooleanVar(value = False)
        self.include_numbers = tk.BooleanVar(value = False)
        self.include_specials = tk.BooleanVar(value = False)

        # Налаштування чек-боксів
        tk.Checkbutton(root, text = "Великі літери (A-Z)", variable=self.include_uppercase).pack(anchor = "w", padx = 20)
        tk.Checkbutton(root, text = "Цифри (0-9)", variable=self.include_numbers).pack(anchor="w", padx=20)
        tk.Checkbutton(root, text = "Спеціальні символи ($!#)", variable=self.include_specials).pack(anchor = "w", padx = 20)

        # Налаштування кнопки "Згенерувати"
        tk.Button(root, text = "Згенерувати пароль", font = ("Arial", 12), command = self.generate_password).pack(pady = 20)



        # Налаштування поля для відображення паролю
        self.result_label = tk.Entry(root, font = ("Arial", 12), justify="center", state = "readonly")
        self.result_label.pack(pady = 10, padx = 10, fill = "x")
        # Налаштування кнопки "Скопіювати до буферу обміну"
        tk.Button(root, text="Скопіювати до буферу обміну", font=("Arial", 12), command=self.copy_to_clipboard).pack(
            pady=20)
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                raise ValueError("Довжина паролю має бути більше 4 символів")
            # Формуємо рядок "a..z"
            characters = string.ascii_lowercase

            # В залежності від чек-боксів до верхньої строки додаємо в кінець додаткові символи
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_specials.get():
                characters += "$#!_&"

            # Генерація паролю
            self.password = "".join(random.choice(characters) for _ in range(length))
            # Перед вставкою розблування поля
            self.result_label.config(state = "normal")

            # Очистка поля, щоб не було накладнь тексту поверх іншого
            self.result_label.delete(0, tk.END)

            # Вставка нового згенерованого паролю і знову обмежуємо доступ до поля
            self.result_label.insert(0, self.password)
            self.result_label.config(state = "readonly")

        except ValueError as e:
            messagebox.showerror("Помилка", str(e))

    def copy_to_clipboard(self):
        pyperclip.copy(self.password)
        messagebox.showinfo("Успіх!", "Пароль скопійовано до буферу обміну")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
