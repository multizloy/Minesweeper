from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.cellButtonObj = None
        self.x = x
        self.y = y

        # добавил клетку в лист в алл
        Cell.all.append(self)

    def createButtonObj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}",
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

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(Cell.all, settings.minesCount)
        for pickedCell in pickedCells:
            pickedCell.isMine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
