import pigpio
import time
import bme280

BME280_ADDR = 0x76
I2C_CH = 1

pi = pigpio.pi()

sensor = bme280.bme280( pi, I2C_CH, BME280_ADDR )
sensor.setup()

while True:
    ( temp, humi, press ) = sensor.get_value()

    print ( "Temperature:", round( temp, 2 ) ,"C  Humidity:", round( humi, 2 ) ,"%  Pressure:", round( press, 2 ) , "hPa" )
    time.sleep(1)

