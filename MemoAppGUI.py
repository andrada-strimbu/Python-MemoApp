from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap.constants import *
import  ttkbootstrap as tb
from ttkbootstrap import Style

def new_memo_function():
    new_memo = tk.Tk()
    new_memo.title("Notes App")
    new_memo.geometry("500x500")
    style = Style(theme='minty')
    style = ttk.Style()

    style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

    notebook = ttk.Notebook(new_memo, style="TNotebook")
    notebook = ttk.Notebook(new_memo)

    notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")
    # Create entry widgets for the title and content of the note
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)


root = tk.Tk()
root.title("Memo App")
root.geometry("500x500")
style = Style(theme='minty')
style = ttk.Style()

my_label=tb.Label(text="Memo App", font=("Helvetica",30), bootstyle="secondary")
my_label.pack(pady=50)
new_memo_button=tb.Button(text="New memo", bootstyle="primary", command=new_memo_function)
new_memo_button.pack(pady=20)

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


root.mainloop()