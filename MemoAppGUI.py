import sqlite3
from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as tb

global combo
def load_names_from_database():
    connection = sqlite3.connect('memo.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM MemoDatabase')
    names = [row[0] for row in cursor.fetchall()]
    connection.close()
    return names


def save_memo():
    title = title_entry.get()
    note = note_entry.get("1.0", "end-1c")

    print(f"Title: {title}")
    print(f"Note: {note}")
    combo['values'] = load_names_from_database()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()


def on_combobox_select(event):
    global combo
    print(f"am intrat in on_combo")
    selected_name = combo.get()
    print(f"Selected Name: {selected_name}")


def new_memo_button_function():
    combo['values'] = load_names_from_database()
    memo_app_frame.pack_forget()
    new_memo_frame.pack(fill=tk.BOTH, expand=True)

def back_button_function():
    combo['values'] = load_names_from_database()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()

root = tk.Tk()
root.title("Memo App")
root.geometry("500x500")
style = Style(theme='minty')
style = ttk.Style()

# Memo App

memo_app_frame = tk.Frame(root)

memo_app_frame.columnconfigure(0, weight=1)
memo_app_frame.columnconfigure(1, weight=3)
memo_app_frame.columnconfigure(2, weight=1)
memo_app_frame.rowconfigure(0, weight=1)
memo_app_frame.rowconfigure(1, weight=3)
memo_app_frame.rowconfigure(2, weight=2)
memo_app_frame.rowconfigure(3, weight=1)

my_label = tb.Label(memo_app_frame, text="Memo App", font=("Helvetica", 40), bootstyle="secondary")
my_label.grid(row=1, column=1, pady=50)

combo = ttk.Combobox(memo_app_frame, font=("Helvetica", 15), bootstyle="primary")
combo.grid(row=2, column=1, pady=20, sticky="new")
combo.bind("<<ComboboxSelected>>", lambda event: print(f"Selected Name: {combo.get()}"))



my_style = tb.Style()
my_style.configure('primary.TButton', font=("Helvetica", 15))
new_memo_button = ttk.Button(memo_app_frame, text="New memo", command=new_memo_button_function, style="primary.TButton")
new_memo_button.grid(row=2, column=1, pady=20, sticky="sew")

memo_app_frame.pack()

# NEW FRAME

new_memo_frame = ttk.Frame(root, padding=10)
new_memo_frame.rowconfigure(0, weight=1)
new_memo_frame.rowconfigure(1, weight=1)
new_memo_frame.rowconfigure(2, weight=2)
new_memo_frame.rowconfigure(3, weight=1)
new_memo_frame.rowconfigure(4, weight=1)
new_memo_frame.columnconfigure(0, weight=1)

# Etichetă pentru titlu
title_label = ttk.Label(new_memo_frame, text="Titlu:", font=("Helvetica", 15), bootstyle="secondary")
title_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

# Câmp de intrare pentru titlu
title_entry = ttk.Entry(new_memo_frame, width=60)
title_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Etichetă pentru notă
note_label = ttk.Label(new_memo_frame, text="Notă:", font=("Helvetica", 15), bootstyle="secondary")
note_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

# Câmp de intrare pentru notă
note_entry = tk.Text(new_memo_frame, width=60, height=10)
note_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ns")

my_style = tb.Style()
my_style.configure('primary.TButton', font=("Helvetica", 15))
save_button = ttk.Button(new_memo_frame, text=" Save ", command=save_memo, style="primary.TButton")
save_button.grid(row=3, column=0, columnspan=2, pady=20)

back_button = ttk.Button(new_memo_frame, text="<Back", bootstyle="primary, link", command=back_button_function)
back_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="nw")

new_memo_frame.pack(fill=tk.BOTH, expand=True)


def main():
    combo['values'] = load_names_from_database()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()
    root.mainloop()


main()
