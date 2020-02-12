# ПРИМЕР ЧТЕНИЯ ТАКТОВ ПОВОРОТА ЭНКОДЕРА:

from pyiArduinoI2Cencoder import *                # Подключаем библиотеку для работы с энкодером I2C-flash.
from time import sleep
enc = pyiArduinoI2Cencoder(0x09)                  # Объявляем объект enc для работы с функциями и методами библиотеки pyiArduinoI2Cencoder, указывая адрес модуля на шине I2C.
                                                  # Если объявить объект без указания адреса (enc = pyiArduinoI2Cencoder), то адрес будет найден автоматически.
try:
    while True:
        #  Считываем такты поворота энкодера:     #
        turn = enc.getEncoder(ENC_TURN)           # Считываем количество тактов поворота энкодера (как влево, так и вправо).
        #  Выводим считанные данные:              #
        if turn is not 0:                         # Выводим количество совершённых тактов (в одном полном обороте 20 тактов).
            print(turn)
        #  Приостанавливаем выполнение скетча:    #
        sleep(.1)                                 # Без задержки в stdout будут появляться только ±1.
except:
    del enc
