from tkinter import Button


class Cell:
    def __init__(self, isMine=False):
        self.isMine = isMine
        self.cellButtonObj = None

    def createButtonObj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text="Text",
        )
        btn.bind("<Button-1>", self.leftClickAction)  # левая кнопка мыши
        btn.bind("<Button-3>", self.rightClickAction)  # правая кнопка мыши
        self.cellButtonObj = btn

    def leftClickAction(self, Event):
        print(Event)
        print("I am left clicked")

    def rightClickAction(self, Event):
        print(Event)
        print("I am right clicked")
