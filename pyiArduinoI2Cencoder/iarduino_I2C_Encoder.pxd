cdef extern from "iarduino_I2C_Encoder.cpp":
    pass

cdef extern from "iarduino_I2C_Encoder.h":
    cdef cppclass iarduino_I2C_Encoder:
        iarduino_I2C_Encoder() except +
        iarduino_I2C_Encoder(unsigned char) except +
        bint begin()
        bint changeAddress(unsigned char)
        bint reset()
        unsigned char getAddress()
        unsigned char getVersion()
        unsigned short getButton()
        short getEncoder(unsigned char)
        short getPosition()
        bint resPosition()
        bint resPosSettings(unsigned char, bint)
        bint setPinOut(unsigned char, unsigned char, unsigned short))

