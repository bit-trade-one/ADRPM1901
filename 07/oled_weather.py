import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import pigpio
import time
import bme280

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

BME280_ADDR = 0x76
I2C_CH = 1

RST = 23
DC = 4
SPI_CH = 0
SPI_CS = 1

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 14

pi = pigpio.pi()

sensor = bme280.bme280( pi, I2C_CH, BME280_ADDR )
sensor.setup()

disp = Adafruit_SSD1306.SSD1306_128_64( rst=RST, dc=DC, spi=SPI.SpiDev( SPI_CH, SPI_CS, max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

draw = ImageDraw.Draw( image )

while True:
    draw.rectangle( ( 0, 0, width, height ), outline=0, fill=0)

    ( temp, humi, press ) = sensor.get_value()

    draw.text( ( 2, 0 ), "温度：" + str( round( temp, 2 ) ) + "度", font=jpfont, fill=255 )
    draw.text( ( 2, 20 ), "湿度：" + str( round( humi, 2 ) ) + "%", font=jpfont, fill=255 )
    draw.text( ( 2, 40 ), "気圧：" + str( round( press, 2 ) ) + "hPa", font=jpfont, fill=255 )

    disp.image(image)
    disp.display()

    time.sleep(1)

