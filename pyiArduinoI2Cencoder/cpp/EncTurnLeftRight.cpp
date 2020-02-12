/*
 *	ПРИМЕР ЧТЕНИЯ ТАКТОВ ПОВОРОТА ЭНКОДЕРА:
 * В данном примере считываются такты поворотов
 * энкодера, отдельно вправо и отдельно влево.
 *
 */

#include <iostream>

//  Подключаем библиотеку для работы с энкодером I2C-flash.
#include "../iarduino_I2C_Encoder.h"

//  Объявляем объект enc для работы с функциями и методами
// библиотеки iarduino_I2C_Encoder, указывая адрес модуля на шине I2C.
//  Если объявить объект без указания адреса (iarduino_I2C_Encoder enc;),
// то адрес будет найден автоматически.
iarduino_I2C_Encoder enc(0x09);

void loop(void);

int main()
{
	//  Инициируем работу с энкодером.
	enc.begin();
	for (;;)
		loop();
}

void loop()
{
	int turnL=0, turnR=0;

	//  Считываем такты поворота энкодера:

	//  Считываем количество тактов поворота
	// энкодера влево  (против часовой стрелки).
	turnL=enc.getEncoder(ENC_TURN_LEFT);
	//  Считываем количество тактов поворота
        // энкодера вправо (по часовой стрелке).
	turnR=enc.getEncoder(ENC_TURN_RIGHT);

	//  Выводим считанные данные:
	if (turnL) {
		std::cout << "-";
		std::cout << turnL;
		std::cout << '\n';
	}
	if (turnR) {
		std::cout << "+" ;
		std::cout << turnR ;
		std::cout << '\n';
	}

	delay(100);
}
