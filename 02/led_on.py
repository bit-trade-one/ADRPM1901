import pigpio

LED_PIN = 14

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )

pi.write( LED_PIN, pigpio.HIGH)



