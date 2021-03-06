#   ПРИМЕР НАСТРОЙКИ ВЫХОДА В РЕЖИМ КНОПКИ:
# Режимы работы выхода модуля энергонезависимы
# (сохраняются и после отключения питания).

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанцируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Указываем выводу модуля работать как выход кнопки энкодера.
enc.setPinOut(ENC_PIN_MODE_KEY)
