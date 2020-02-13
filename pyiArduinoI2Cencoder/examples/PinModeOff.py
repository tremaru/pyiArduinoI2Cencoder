#   ПРИМЕР ОТКЛЮЧЕНИЯ ВЫХОДА МОДУЛЯ:
# Режимы работы выхода модуля энергонезависимы
# (сохраняются и после отключения питания).

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Инициируем работу с энкодером.
enc.begin()

# Указываем выводу модуля не работать.
enc.setPinOut(ENC_PIN_MODE_KEY)
