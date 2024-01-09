import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

def minimize_window():
    root.iconify()  # Iconify (minimize) the window

def restore_window():
    root.deiconify()  # Deiconify (restore) the window

minimize_button = tk.Button(root, text="Minimize", command=minimize_window)
minimize_button.pack()

restore_button = tk.Button(root, text="Restore", command=restore_window)
restore_button.pack()

root.mainloop()
