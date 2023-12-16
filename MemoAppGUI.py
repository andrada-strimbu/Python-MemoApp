import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as tb
from MemoDatabase import MemoDatabase
from tkinter import messagebox


def combo_update():
    titles = memo_database.get_all_titles()
    formatted_titles = [title[0] if isinstance(title, tuple) else title for title in titles]
    combo['values'] = formatted_titles


def save_memo():
    title = new_title.get("1.0", tk.END).strip()
    note = new_note_entry.get("1.0", "end-1c")

    if memo_database.memo_exists(title):
        error_message = f"The title '{title}' already exists. Please choose another title."
        print(error_message)
        messagebox.showerror("Eroare", error_message)
    else:
        print(f"Title: {title}")
        print(f"Note: {note}")
        memo_database.save_memo(title, note)
        new_title.delete("1.0", tk.END)
        new_note_entry.delete("1.0", tk.END)
        combo_update()
        memo_app_frame.pack(fill=tk.BOTH, expand=True)
        new_memo_frame.pack_forget()
        view_memo_frame.pack_forget()
        edit_memo_frame.pack_forget()


def remove_function(title):
    memo_database.delete_memo_by_title(title)
    back_button_function()

def new_memo_button_function():
    combo_update()
    memo_app_frame.pack_forget()
    view_memo_frame.pack_forget()
    edit_memo_frame.pack_forget()
    new_memo_frame.pack(fill=tk.BOTH, expand=True)

def back_button_function():
    combo_update()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()
    view_memo_frame.pack_forget()
    edit_memo_frame.pack_forget()

def view_note_function(title):
    memo_data = memo_database.load_memo_by_title(title)
    if memo_data:
        view_title_label.config(text=memo_data[1])
        view_note_label.config(text=memo_data[2])
        view_date_label.config(text=memo_data[3])
        memo_app_frame.pack_forget()
        view_memo_frame.pack(fill=tk.BOTH, expand=True)

def click_bind(event):
    selected_title = combo.get()
    print(f"Selected Title: {selected_title}")
    view_note_function(selected_title)

def edit_button_function(title):
    memo_app_frame.pack_forget()
    new_memo_frame.pack_forget()
    view_memo_frame.pack_forget()
    print(title)
    memo_data = memo_database.load_memo_by_title(title)
    if memo_data:
        edit_title_label.config(text=title)
        note_edit.delete(1.0, tk.END)
        note_edit.insert(tk.END, memo_data[2])

        edit_memo_frame.pack(fill=tk.BOTH, expand=True)

def update_function(title):
    title = edit_title_label.cget("text")
    note = note_edit.get("1.0", tk.END)
    print(f"Updated Title: {title}")
    print(f"Updated Note: {note}")
    memo_database.update_memo(title, note)
    combo_update()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()
    view_memo_frame.pack_forget()
    edit_memo_frame.pack_forget()

#GUI
root = tk.Tk()
root.title("Memo App")
root.geometry("500x500")
style = Style(theme='minty')
style = ttk.Style()
memo_database = MemoDatabase()

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
combo.bind("<<ComboboxSelected>>", click_bind)

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

new_title_label = ttk.Label(new_memo_frame, text="Title:", font=("Helvetica", 15), bootstyle="secondary")
new_title_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

new_title = tk.Text(new_memo_frame, width=60, height=1)
new_title.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Etichetă pentru notă
new_note_label = ttk.Label(new_memo_frame, text="Note:", font=("Helvetica", 15), bootstyle="secondary")
new_note_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

# Câmp de intrare pentru notă
new_note_entry = tk.Text(new_memo_frame, width=60, height=10)
new_note_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ns")

my_style = tb.Style()
my_style.configure('primary.TButton', font=("Helvetica", 15))
save_button = ttk.Button(new_memo_frame, text=" Save ", command=save_memo, style="primary.TButton")
save_button.grid(row=3, column=0, columnspan=2, pady=20)

back_button = ttk.Button(new_memo_frame, text="<Back", bootstyle="primary, link", command=back_button_function)
back_button.grid(row=0, column=0, columnspan=2, pady=10, sticky="nw")

new_memo_frame.pack(fill=tk.BOTH, expand=True)
# VIEW FRAME
view_memo_frame = ttk.Frame(root, padding=10)
view_memo_frame.columnconfigure(0, weight=1)
view_memo_frame.columnconfigure(1, weight=2)
view_memo_frame.columnconfigure(2, weight=1)
view_memo_frame.rowconfigure(0, weight=1)
view_memo_frame.rowconfigure(1, weight=1)
view_memo_frame.rowconfigure(2, weight=5)

back_button_view = ttk.Button(view_memo_frame, text="<Back", bootstyle="primary, link", command=back_button_function)
back_button_view.grid(row=0, column=0, columnspan=2, pady=10, sticky="nw")

view_title_label = ttk.Label(view_memo_frame, text="", font=("Helvetica", 30), bootstyle="secondary")
view_title_label.grid(row=1, column=1, padx=10, pady=10)

remove_button = ttk.Button(view_memo_frame, text="Remove", bootstyle="secondary, link",
                           command=lambda: remove_function(view_title_label.cget("text")))
remove_button.grid(row=0, column=1, pady=10, sticky="n")

view_note_label = ttk.Label(view_memo_frame, text="", font=("Helvetica", 15), bootstyle="secondary")
view_note_label.grid(row=2, column=1, padx=10, pady=10, sticky="nw")

edit_button = ttk.Button(view_memo_frame, text="Edit>", bootstyle="primary, link",
                         command=lambda: edit_button_function(view_title_label.cget("text")))
edit_button.grid(row=0, column=3, columnspan=2, pady=10, sticky="ne")

view_date_label = ttk.Label(view_memo_frame, text="", font=("Helvetica", 5), bootstyle="secondary")
view_date_label.grid(row=1, column=3, padx=10, pady=10, sticky="ne")

# EDIT FRAME
edit_memo_frame = ttk.Frame(root, padding=10)
edit_memo_frame.rowconfigure(0, weight=1)
edit_memo_frame.rowconfigure(1, weight=1)
edit_memo_frame.rowconfigure(2, weight=2)
edit_memo_frame.rowconfigure(3, weight=1)
edit_memo_frame.rowconfigure(4, weight=1)
edit_memo_frame.columnconfigure(0, weight=1)

# Etichetă pentru titlu
edit_title_label = ttk.Label(edit_memo_frame, text="", font=("Helvetica", 30), bootstyle="secondary")
edit_title_label.grid(row=1, column=1, padx=10, pady=10)

# Etichetă pentru notă
edit_note_label = ttk.Label(edit_memo_frame, text="Note:", font=("Helvetica", 15), bootstyle="primary")
edit_note_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

# Câmp de intrare pentru notă
note_edit = tk.Text(edit_memo_frame, width=60, height=10)
note_edit.grid(row=2, column=1, padx=10, pady=10, sticky="ns")

my_style = tb.Style()
my_style.configure('secondary.TButton', font=("Helvetica", 15))
save_edit = ttk.Button(edit_memo_frame, text=" Save changes ",
                       command=lambda: update_function(view_title_label.cget("text")),
                       style="secondary.TButton")
save_edit.grid(row=3, column=0, columnspan=2, pady=20)

back_button_edit = ttk.Button(edit_memo_frame, text="<Back", bootstyle="secondary, link", command=back_button_function)
back_button_edit.grid(row=0, column=0, columnspan=2, pady=10, sticky="nw")

edit_memo_frame.pack(fill=tk.BOTH, expand=True)

def main():
    combo_update()
    memo_app_frame.pack(fill=tk.BOTH, expand=True)
    new_memo_frame.pack_forget()
    edit_memo_frame.pack_forget()
    view_memo_frame.pack_forget()
    root.mainloop()


main()
