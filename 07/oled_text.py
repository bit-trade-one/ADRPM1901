import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 23
DC = 4
SPI_CH = 0
SPI_CS = 1

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 14

disp = Adafruit_SSD1306.SSD1306_128_64( rst=RST, dc=DC, spi=SPI.SpiDev( SPI_CH, SPI_CS, max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )

jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

draw.text( ( 5, 5 ), "Raspberry Pi", font=jpfont, fill=255 )
draw.text( ( 5, 25 ), "ラズパイマガジン", font=jpfont, fill=255 )
draw.text( ( 5, 45 ), "電子工作", font=jpfont, fill=255 )

disp.image(image)
disp.display()



