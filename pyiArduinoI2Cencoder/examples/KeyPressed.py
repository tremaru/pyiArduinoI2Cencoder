#   ПРИМЕР РАБОТЫ С КНОПКОЙ ЭНКОДЕРА:
# В stdout выводится состояние кнопки
# энкодера на момент запуска сценария

from pyiArduinoI2Cencoder import *      # Подключаем библиотеку для работы с энкодером I2C-flash.
enc = pyiArduinoI2Cencoder(0x09)        # Объявляем объект enc для работы с функциями и методами библиотеки pyiArduinoI2Cencoder, указывая адрес модуля на шине I2C.
                                        # Если объявить объект без указания адреса (enc = pyiArduinoI2Cencoder()), то адрес будет найден автоматически.
f = enc.getButton(KEY_PRESSED)          # Считываем состояние кнопки энкодера в переменную f.
if not f:
    print("OFF")
else:
    print("ON")
