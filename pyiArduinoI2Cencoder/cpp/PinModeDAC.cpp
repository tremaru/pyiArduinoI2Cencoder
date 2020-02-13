/*
 *	ПРИМЕР НАСТРОЙКИ ВЫХОДА В АНАЛОГОВЫЙ РЕЖИМ:
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

	/* Указываем выводу модуля работать как аналоговый выход,
	 * напряжение которого меняется от 0 до 3.3В
	 * за 2 полных оборота вала энкодера.
	 */
	enc.setPinOut(ENC_PIN_MODE_DAC, 2);

	return 0;
}
