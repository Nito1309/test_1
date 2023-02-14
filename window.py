import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry("300x300")
label = tk.Label(root, text = "Hello")
label.pack()
root.mainloop()