# ПРИМЕР ФИКСИРУЕТ СМЕНУ СОСТОЯНИЯ КНОПКИ:  # Светодиод на плате Arduino будет включаться при каждом нажатии и отпускании кнопки.
                                            #
from time import sleep                      #
from pyiArduinoI2Cencoder import *          # Подключаем библиотеку для работы с энкодером I2C-flash.
enc = pyiArduinoI2Cencoder(0x09)            # Объявляем объект enc для работы с функциями и методами библиотеки pyiArduinoI2Cencoder, указывая адрес модуля на шине I2C.
                                            # Если объявить объект без указания адреса (pyiArduinoI2Cencoder enc ), то адрес будет найден автоматически.
                                            #
                                            #
while True:                                 #
#  Фиксируем смену состояния кнопки:        #
    if enc.getButton(KEY_CHANGED):          # Если состояние кнопки изменилось, то ...
        print("Click")                      # выводим сообщение в stdout
                                            #
    sleep(.1)                               #
