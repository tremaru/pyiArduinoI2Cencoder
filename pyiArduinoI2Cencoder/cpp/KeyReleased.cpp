/*
 *	ДАННЫЙ ПРИМЕР ФИКСИРУЕТ ОТПУСКАНИЕ КНОПКИ:
 * При каждом отпускании кнопки, будет
 * выводится сообщение в stdout
 */

#include <iostream>
// Подключаем библиотеку для работы с энкодером I2C-flash.
#include "../iarduino_I2C_Encoder.h"
// Инстанциируем объект для работы с функциями указывая адрес модуля на шине I2C.
iarduino_I2C_Encoder enc(0x09);

void loop(void);

int main()
{
	// Инициируем работу с энкодером.
	enc.begin();
	for (;;)
		loop();
}

void loop()
{
	// Фиксируем событие отпускания кнопки:
	// Если кнопка энкодера отпускается, то ...
	if (enc.getButton(KEY_RELEASED)) {
		// Выводим текст в stdout
		std::cout << "Click" << '\n';
	}
	delay(100);
}
