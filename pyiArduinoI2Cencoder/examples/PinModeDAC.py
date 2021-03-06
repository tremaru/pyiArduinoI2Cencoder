#   ПРИМЕР НАСТРОЙКИ ВЫХОДА В АНАЛОГОВЫЙ РЕЖИМ:
# Режимы работы выхода модуля энергонезависимы
# (сохраняются и после отключения питания).

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанцируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Указываем выводу модуля работать как аналоговый выход,
# напряжение которого меняется от 0 до 3.3В
# за 2 полных оборота вала энкодера.
enc.setPinOut(ENC_PIN_MODE_DAC, 2)
