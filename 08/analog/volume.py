import pigpio
import time
from mcp3204 import mcp3204

Rx = 10000

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3204( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    value = adc.get_value( READ_CH )
    volt = adc.get_volt( value )

    print ( " Volt:", round( volt, 3 ), "V  Value :" , value  )

    time.sleep( 1 )


