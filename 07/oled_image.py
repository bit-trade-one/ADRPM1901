import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image

RST = 23
DC = 4
SPI_CH = 0
SPI_CS = 1

disp = Adafruit_SSD1306.SSD1306_128_64( rst=RST, dc=DC, spi=SPI.SpiDev( SPI_CH, SPI_CS, max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display()

image = Image.open('image.png').convert('1')

disp.image(image)
disp.display()



