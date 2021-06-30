from View import View

class Controller:
    
    def __init__(self):
        self.view = View(self)
        self.view.main()

    def main(self):
        self.view.mainloop()