import ctypes
import sys
from tkinter import Button, Label
import random
import settings
from ctypes import *


class Cell:
    all = []
    cellsCount = settings.cellCount
    cellCountLabelObj = None

    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.isOpened = False
        self.cellButtonObj = None
        self.isMineCandidate = False
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
            # если клетка имеет значение 0, значит мин вокруг нет. открываем клетки автоматически
            if self.surroundedCellsMinesLength == 0:
                for cellObj in self.surroundedCells:
                    cellObj.showCell()
            self.showCell()
        # Отмена правого и левого клика мыши если клетка открыта
        self.cellButtonObj.unbind("<Button-1>")
        self.cellButtonObj.unbind("<Button-3>")
        # если количество клеток равно количеству мин, игрок победил
        if Cell.cellsCount == settings.minesCount:
            ctypes.windll.user32.MessageBoxW(0, "You win!", "Game Over", 0)

    @staticmethod
    def createCellCountLabel(location):
        lbl = Label(
            location,
            text=f"Cells left:{Cell.cellsCount}",
            width=12,
            height=4,
            font=("", 30),
        )
        Cell.cellCountLabelObj = lbl

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
        if not self.isOpened:
            Cell.cellsCount -= 1
            self.cellButtonObj.configure(text=self.surroundedCellsMinesLength)
            # замена числа оставшихся клеток
            if Cell.cellCountLabelObj:
                Cell.cellCountLabelObj.configure(
                    text=f"Cells left:{Cell.cellsCount}",
                )
            # функцианал автоматического перевода цвета, даже при ранее выбранной возможной мине
            self.cellButtonObj.configure(
                bg="SystemButtonFace",
            )
        # отмечаем, открытые клетки
        self.isOpened = True

    def getCellByAxis(self, x, y):
        # вернуть клетку со значением х,у
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def showMine(self):
        # logic to interrupt the game
        self.cellButtonObj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "Game Over", 0)
        sys.exit()

    # функцианал на правую кнопку мыши для выделения клеток, в которых могут быть мины не открывая клетку
    def rightClickAction(self, Event):
        if not self.isMineCandidate:
            self.cellButtonObj.configure(
                bg="orange",
            )
            self.isMineCandidate = True
        else:
            self.cellButtonObj.configure(
                bg="SystemButtonFace",
            )
            self.isMineCandidate = False

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(Cell.all, settings.minesCount)
        for pickedCell in pickedCells:
            pickedCell.isMine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
