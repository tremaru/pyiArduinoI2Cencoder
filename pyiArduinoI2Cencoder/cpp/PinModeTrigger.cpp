/*
 *	ПРИМЕР НАСТРОЙКИ ВЫХОДА В РЕЖИМ ПЕРЕКЛЮЧАТЕЛ:
 * Режимы работы выхода модуля энергонезависимы
 * (сохраняются и после отключения питания).
 */

// Подключаем библиотеку для работы с энкодером I2C-flash.
#include "../iarduino_I2C_Encoder.h"

// Инстанциируем объект, указывая адрес модуля на шине I2C.
iarduino_I2C_Encoder enc(0x09);

int main()
{
	// Инициируем работу с энкодером.
	enc.begin();

	// Указываем выводу модуля работать
	// как кнопочный переключатель (триггер).
	enc.setPinOut(ENC_PIN_MODE_TRG);

	return 0;
}
