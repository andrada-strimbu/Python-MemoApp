import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as tb


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


def new_memo_function():
    global title_entry, note_entry
    root = tk.Toplevel()
    root.title("Add Memo")
    root.geometry("500x500")
    style = Style(theme='minty')

    new_memo_frame = ttk.Frame(root, padding=10)
    new_memo_frame.pack(fill=tk.BOTH, expand=True)

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

    back_button = ttk.Button(new_memo_frame, text="<Back", bootstyle="primary, link")
    back_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="nw")


def main():
    root = tk.Tk()
    root.title("Memo App")
    root.geometry("500x500")
    style = Style(theme='minty')
    style = ttk.Style()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=3)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)

    my_label = tb.Label(root, text="Memo App", font=("Helvetica", 40), bootstyle="secondary")
    my_label.grid(row=1, column=1, pady=50)

    combo = ttk.Combobox(root, values=load_names_from_database(), font=("Helvetica", 15), bootstyle="primary")
    combo.grid(row=2, column=1, pady=20, sticky="new")

    my_style = tb.Style()
    my_style.configure('primary.TButton', font=("Helvetica", 15))
    new_memo_button = ttk.Button(root, text="New memo", command=new_memo_function, style="primary.TButton")
    new_memo_button.grid(row=2, column=1, pady=20, sticky="sew")

    def on_combobox_select(event):
        selected_name = combo.get()
        print(f"Selected Name: {selected_name}")

    combo.bind("<<ComboboxSelected>>", on_combobox_select)

    root.mainloop()


main()
