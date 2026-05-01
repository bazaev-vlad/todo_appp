import tkinter as tk
from tkinter import messagebox
import json
import random

tasks = []

# ---------- ЛОГИКА ----------

def add_task():
    task = entry.get()

    if not task.strip():
        messagebox.showerror("Ошибка", "Введите задачу")
        return

    tasks.append(task)
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)


def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Ошибка", "Выберите задачу")
        return

    index = selected[0]
    listbox.delete(index)
    tasks.pop(index)


def save_tasks():
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


def load_tasks():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for task in data:
                tasks.append(task)
                listbox.insert(tk.END, task)
    except:
        pass


def random_task():
    if tasks:
        task = random.choice(tasks)
        messagebox.showinfo("Случайная задача", task)


def filter_tasks():
    keyword = filter_entry.get().lower()

    listbox.delete(0, tk.END)

    for task in tasks:
        if keyword in task.lower():
            listbox.insert(tk.END, task)


def show_all():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)


# ---------- GUI ----------

root = tk.Tk()
root.title("To-Do App")

# Ввод задачи
entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Добавить", command=add_task).pack()
tk.Button(root, text="Удалить", command=delete_task).pack()
tk.Button(root, text="Сохранить", command=save_tasks).pack()
tk.Button(root, text="Случайная задача", command=random_task).pack()

# Фильтр
filter_entry = tk.Entry(root, width=40)
filter_entry.pack()

tk.Button(root, text="Фильтр", command=filter_tasks).pack()
tk.Button(root, text="Показать всё", command=show_all).pack()

# Список задач
listbox = tk.Listbox(root, width=50)
listbox.pack()

# Загрузка при старте
load_tasks()

root.mainloop()