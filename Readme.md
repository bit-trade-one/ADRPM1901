## 部品表・取り付け位置

|基板番号|パーツ名|品番等|取り付け位置|向き|
|:-:|:-:|:-:|:-:|:-:|
|U1|ICソケット|8ピン</td><td rowspan="2">![DIP8](img/DIP8-1.JPG)|![DIP-8Socket](img/DIP8-2.JPG)|
|U1|ADコンバータ|MCP3002-I/P|![DIP-8IC](img/DIP8-3.JPG)|
|U2|ICソケット|22ピン400mil</td><td rowspan="2">![DIP22](img/DIP22-1.JPG)|![DIP-22Socket](img/DIP22-2.JPG)|
|U2|モータドライバ|NJM2670D2|![DIP-22IC](img/DIP22-3.JPG)|
|U3|OLEDグラフィックディスプレイ|SSD1306|||
|Q1|MOSFET Nch 2N7000|2N7000|![TO92](img/TO92-1.JPG)|![TO92IC](img/TO92-2.JPG)|
|D1|LED（赤）|φ3 赤||![RLED](img/RLED.JPG)|
|D2|フルカラーLED|φ5||![FLED](img/FLED.JPG)|
|SW1|タクトスイッチ||||
|R1|抵抗 1/4W|330Ω|||
|R2|抵抗 1/4W|100Ω|||
|R4|抵抗 1/4W|1kΩ|||
|R5|抵抗 1/4W|1kΩ|||
|R6|抵抗 1/4W|1kΩ|||
|R7|抵抗 1/4W|10kΩ|||
|R8|抵抗 1/4W|10kΩ|||
|R9|抵抗 1/4W|10kΩ|||
|R10|抵抗 1/4W|10kΩ|||
|R11|抵抗 1/4W|10kΩ|||
|R12|抵抗 1/4W|10kΩ|||
|C1|積層セラミックコンデンサ|0.1μF 50V 2.54mm|||
|C2|積層セラミックコンデンサ|0.1μF 50V 2.54mm|||
|C3|積層セラミックコンデンサ|0.1μF 50V 2.54mm|||
|C4|積層セラミックコンデンサ|0.1μF 50V 2.54mm|||
|JP1|ピンヘッダ 3P||||
|JP1|ジャンパーピン 2P つまみ付き||||
|J1|ピンフレーム 2P||||
|J2|ピンフレーム 5P||||
|J3|ターミナルブロック 2P 5.08mm 青||</td><td rowspan="3">![Terminal](img/Terminal.JPG)|
|J4|ターミナルブロック 2P 5.08mm 青||||
|J5|ターミナルブロック 2P 5.08mm 緑||||
|J6|ピンフレーム 6P||||
|J7|ピンヘッダ 4P||||
|J8|ピンヘッダ 3P||||
|J9|ピンヘッダ 9P||||
|J10|ピンヘッダ 4P||||
|J11|ピンフレーム 20×2P||||

## 初回セットアップ

### I2C/SPI有効化

![setting1](img/setting1.PNG)
![setting2](img/setting2.PNG)

### pigpio有効化

```$ sudo systemctl enable pigpiod```
```$ sudo systemctl start pigpiod```

### OLED用ライブラリ・フォントインストール

```$ sudo apt install fonts-takao```
```$ wget https://github.com/adafruit/Adafruit_Python_SSD1306/archive/master.zip```
```$ unzip master.zip```
```$ sudo python3 master.zip/setup.py install```

### サンプルプログラムダウンロード

```$ wget サンプルプログラムのURL```
```$ unzip サンプルプログラムのzip```

## 02 LED

### led_on.py

### led_off.py

### led_pwm.py

### led_blink.py

## 03 フルカラーLED

### led_color.py

### led_color_hsv.py

### led_color_offset.py

## 04 スイッチ

### sw_read.py

### sw_led.py

## 05 温湿度・気圧センサ

### weather.py

## 06 DCモータ

### motor_foward.py

### motor_reverse.py

### motor_pwm.py

### motor_stop.py

## 07 OLEDディスプレイ

### oled_text.py

### oled_image.py

### oled_weather.py