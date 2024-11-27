from tkinter import *

app_width = 600
app_height = 300
app_x = 400
app_y = 200

class Window():
    def __init__(self, width = app_width, height = app_height, x = app_x, y = app_y, title = "Window", resizable = (False, False), icon = "icon.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()

wind = Window()
wind.run()