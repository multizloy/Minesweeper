import settings


# функция для быстрого подсчета высоты
def heightPerct(percentage):
    return (settings.HEIGHT / 100) * percentage


# функция для быстрого подсчета ширины
def widthPerct(percentage):
    return (settings.WIDTH / 100) * percentage
