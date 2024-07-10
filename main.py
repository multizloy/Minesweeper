from tkinter import *
import settings
import utils

# создаем окно игры
root = Tk()
# задаем цвет заднего фона окна игры
root.configure(bg="black")
# размер окна
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
# название игры
root.title("Minesweeper game")
# отключаем возможность изменения сторон окна
root.resizable(False, False)

# создаем верхнюю рамку в окне игры
topFrame = Frame(
    root,
    bg="black",  # изменить цвет, если потребуется
    width=settings.WIDTH,
    height=utils.heightPerct(25),
)
# задаем положение рамки в окне
topFrame.place(x=0, y=0)
# создаем левую рамку в окне
leftFrame = Frame(
    root,
    bg="black",  # изменить цвет, если потребуется
    width=utils.widthPerct(25),
    height=utils.heightPerct(75),
)
leftFrame.place(
    x=0,
    y=utils.heightPerct(25),
)
# центральная рамка окна
centerFrame = Frame(
    root,
    bg="black",  # change if needed
    width=utils.widthPerct(75),
    height=utils.heightPerct(75),
)
centerFrame.place(
    x=utils.widthPerct(25),
    y=utils.heightPerct(25),
)
# закрываем окно игры
root.mainloop()
