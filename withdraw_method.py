import tkinter as tk

def show_window():
    window.deiconify()  # Show the window

window = tk.Tk()
window.withdraw()  # Hide the window initially

button = tk.Button(window, text="Show Window", command=show_window)
button.pack()

window.mainloop()
