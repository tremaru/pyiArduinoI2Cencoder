#   ПРИМЕР ЧТЕНИЯ ТЕКУЩЕЙ ПОЗИЦИИ ВАЛА ЭНКОДЕРА:
# Зная точную позицию Вала энкодера, работа
# с модулем похожа на работу с потенциометром.

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанцируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Указываем считать до 2 полных оборотов.
enc.setPosSettings(2)

print("Вращайте вал!")

while True:

    p = enc.getPosition()
    # Выводим текущую позицию вала энкодера.
    print(p)

    sleep(.5)

