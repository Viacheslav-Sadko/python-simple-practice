from tkinter import *

width = 600
height = 300
x = 400
y = 200

window = Tk()
window.title("My app")
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False, False)
window.iconbitmap("icon.ico")

window.mainloop()