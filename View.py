from tkinter import *

class View(Tk):
    def __init__(self, controller):
        super().__init__()

        self.title("StatQ")
        self.resizable(False, False)
        self.centerApp(WIDTH=550, HEIGHT=700)
        self.iconbitmap("./img/statQ.ico")

        self.controller = controller

    def centerApp(self, WIDTH: int, HEIGHT: int):
        xPosition = (self.winfo_screenwidth())/2 - (WIDTH/2)
        yPosition = (self.winfo_screenheight())/2 - (HEIGHT/2)
        self.geometry(f"{WIDTH}x{HEIGHT}+{int(xPosition)}+{int(yPosition)}")

    def main(self):
        self.mainloop()