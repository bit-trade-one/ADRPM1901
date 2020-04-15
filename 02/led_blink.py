import pigpio
import time

LED_PIN = 14

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )

while True:
	pi.write( LED_PIN, pigpio.LOW )
	time.sleep( 1 )
	pi.write( LED_PIN, pigpio.HIGH )
	time.sleep( 1 )



