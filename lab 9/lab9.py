import tkinter as tk
import os
from tkinter import messagebox, filedialog


def create_directory():
    directory_name = entry.get()
    if directory_name:
        try:
            os.mkdir(directory_name)
            messagebox.showinfo("Success", "Директория успешно создана!")
            refresh_directory_list()
        except FileExistsError:
            messagebox.showerror("Error", "Директория уже существует!")
    else:
        messagebox.showerror("Error", "Введите название директории!")


def delete_directory():
    selected_directory = listbox.get(tk.ACTIVE)
    if selected_directory:
        if messagebox.askyesno("Warning", "Вы уверены, что хотите удалить директорию?"):
            try:
                os.rmdir(selected_directory)
                messagebox.showinfo("Success", "Директория успешно удалена!")
                refresh_directory_list()
            except OSError:
                messagebox.showerror("Error", "Невозможно удалить директорию!")
    else:
        messagebox.showerror("Error", "Выберите директорию!")


def rename_directory():
    selected_directory = listbox.get(tk.ACTIVE)
    if selected_directory:
        new_name = filedialog.askstring("Rename Directory", "Введите новое название директории:")
        if new_name:
            try:
                os.rename(selected_directory, new_name)
                messagebox.showinfo("Success", "Директория успешно переименована!")
                refresh_directory_list()
            except OSError:
                messagebox.showerror("Error", "Невозможно переименовать директорию!")
    else:
        messagebox.showerror("Error", "Выберите директорию!")


def refresh_directory_list():
    listbox.delete(0, tk.END)
    directories = os.listdir()
    for directory in directories:
        if os.path.isdir(directory):
            listbox.insert(tk.END, directory)


# Создание графического интерфейса
window = tk.Tk()
window.title("Простой файловый менеджер")

label = tk.Label(window, text="Список директорий:")
label.pack()

listbox = tk.Listbox(window)
listbox.pack()

entry = tk.Entry(window)
entry.pack()

create_button = tk.Button(window, text="Создать", command=create_directory)
create_button.pack()

delete_button = tk.Button(window, text="Удалить", command=delete_directory)
delete_button.pack()

rename_button = tk.Button(window, text="Переименовать", command=rename_directory)
rename_button.pack()

refresh_button = tk.Button(window, text="Обновить список", command=refresh_directory_list)
refresh_button.pack()

refresh_directory_list()

window.mainloop()
