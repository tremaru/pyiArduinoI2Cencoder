// ПРИМЕР ФИКСИРУЕТ СМЕНУ СОСТОЯНИЯ КНОПКИ:     //   Светодиод на плате Arduino будет включаться при каждом нажатии и отпускании кнопки.

#include <iostream>
#include "../iarduino_I2C_Encoder.h"         	//   Подключаем библиотеку для работы с энкодером I2C-flash.
iarduino_I2C_Encoder enc(0x09);                 //   Объявляем объект enc для работы с функциями и методами библиотеки iarduino_I2C_Encoder, указывая адрес модуля на шине I2C.
                                                //   Если объявить объект без указания адреса (iarduino_I2C_Encoder enc;), то адрес будет найден автоматически.
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
	// Если состояние кнопки изменилось, то ...
	if (enc.getButton(KEY_CHANGED)) {
		// Выводим текст в stdout
		std::cout << "Click" << '\n';
	}
}
