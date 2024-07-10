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
        )
        btn.bind("<Button-1>", self.leftClickAction)  # левая кнопка мыши
        btn.bind("<Button-3>", self.rightClickAction)  # правая кнопка мыши
        self.cellButtonObj = btn

    def leftClickAction(self, Event):
        if self.isMine:
            self.showMine()
        else:
            self.showCell()

    # описание окружающих клеток
    @property
    def surroundedCells(self):
        cells = [
            self.getCellByAxis(self.x - 1, self.y - 1),
            self.getCellByAxis(self.x - 1, self.y),
            self.getCellByAxis(self.x - 1, self.y + 1),
            self.getCellByAxis(self.x, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y),
            self.getCellByAxis(self.x + 1, self.y + 1),
            self.getCellByAxis(self.x, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    # подсчет мин
    @property
    def surroundedCellsMinesLength(self):
        counter = 0
        for cell in self.surroundedCells:
            if cell.isMine:
                counter += 1
        return counter

    def showCell(self):
        self.cellButtonObj.configure(
            text=self.surroundedCellsMinesLength,
        )

    def getCellByAxis(self, x, y):
        # вернуть клетку со значением х,у
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def showMine(self):
        # logic to interrupt the game
        self.cellButtonObj.configure(bg="red")

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
