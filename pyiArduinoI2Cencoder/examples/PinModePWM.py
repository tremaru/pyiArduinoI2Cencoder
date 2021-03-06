# ПРИМЕР НАСТРОЙКИ ВЫХОДА В РЕЖИМ ШИМ:
# Режимы работы выхода модуля энергонезависимы
# (сохраняются и после отключения питания).

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанцируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Инициируем работу с энкодером.
# Указываем выводу модуля работать как выход с ШИМ,
# коэффициент заполнения которого меняется от 0% до 100%
# за 2 полных оборота вала энкодера.
enc.setPinOut(ENC_PIN_MODE_PWM, 2)
