import tkinter as tk

root = tk.Tk()
root.title("Hello Window")
label = tk.Label(root, text="Ziad was here", font=("Arial", 42))
label.pack(padx=20, pady=20)

root.mainloop()
