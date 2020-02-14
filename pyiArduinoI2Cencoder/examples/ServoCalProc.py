from time import sleep
from pyiArduinoI2Cencoder import *
enc = pyiArduinoI2Cencoder(0x09)

txt1 = "Поворотом ручки энкодера добейтесь требуемого\r\nкрайнего положения вала сервопривода.\r\nНажмите на ручку энкодера..."
txt2 = "Поворотом ручки энкодера добейтесь другого\r\nкрайнего положения вала сервопривода.\r\nНажмите на ручку энкодера..."

# Определяем ширину импульсов для крайних
# положений вала сервопривода в мкс.

i, j =450, 2450

#   Указываем выводу модуля работать с сервоприводом,
# отведя под управление 2 полных оборота вала энкодера.
enc.setPinOut(ENC_PIN_MODE_SER, 2)

# Задаём границы поворота сервопривода, указав ширину
# импульсов в мкс для минимального и максимального угла.
enc.setServoLimit(i, j)

# Выводим текст информирующий о действиях которые необходимо выполнить.
print(txt1)

# Бесконечно ждём нажатия кнопки энкодера ...
while enc.getButton(KEY_PUSHED) == False:
    sleep(.1)

# Получаем ширину импульсов текущего положения вала сервопривода.
i  =  enc.getServoWidth()
print("Ок."  )

# Бесконечно ждём отпускания кнопки энкодера ...
while enc.getButton(KEY_RELEASED) == False:
    sleep(.1)

# Выводим текст информирующий о действиях которые необходимо выполнить.
print(txt2)

# Бесконечно ждём нажатия кнопки энкодера ...
while enc.getButton(KEY_PUSHED) == False :
    sleep(.1)

# Получаем ширину импульсов текущего положения вала сервопривода.
j  =  enc.getServoWidth()
print("Ок."  )

# Бесконечно ждём отпускания кнопки энкодера ...
while enc.getButton(KEY_RELEASED) == False:
    sleep(.1)

# Задаём новые границы поворота сервопривода, указав ширину импульсов
# в мкс для минимального и максимального угла.
enc.setServoLimit(i, j)

print("Калибровка завершена!")

