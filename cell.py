from tkinter import Button

class Cell:
    def __init__(self, isMine=False):
        self.isMine = isMine
        self.cellButtonObj = None
    
    def createButtonObj(self, location):
        btn = Button(
            location,
            text = "Text"
        )
        self.cellButtonObj = btn