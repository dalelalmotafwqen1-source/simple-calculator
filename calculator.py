import tkinter as tk
from tkinter import messagebox

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("خطأ", "عملية غير صالحة")

root = tk.Tk()
root.title("آلة حاسبة بسيطة")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=tk.X, padx=10, pady=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(frame, text=text, font=("Arial", 16), bg="green", fg="white", command=calculate)
    else:
        btn = tk.Button(frame, text=text, font=("Arial", 16), command=lambda t=text: click(t))
    btn.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

clear_btn = tk.Button(root, text="مسح (C)", font=("Arial", 14), bg="red", fg="white", command=clear)
clear_btn.pack(fill=tk.X, padx=10, pady=5)

for i in range(5):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()
