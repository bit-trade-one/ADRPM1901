import pigpio

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

RED_OFFSET = 100
GREEN_OFFSET = 60
BLUE_OFFSET = 80

RED = 20
GREEN = 50
BLUE = 100

pi = pigpio.pi()

pi.set_mode( RED_PIN, pigpio.OUTPUT )
pi.set_mode( GREEN_PIN, pigpio.OUTPUT )
pi.set_mode( BLUE_PIN, pigpio.OUTPUT )

pi.set_PWM_frequency( RED_PIN, 50 )
pi.set_PWM_frequency( GREEN_PIN, 50 )
pi.set_PWM_frequency( BLUE_PIN, 50 )

pi.set_PWM_range( RED_PIN, 100 )
pi.set_PWM_range( GREEN_PIN, 100 )
pi.set_PWM_range( BLUE_PIN, 100 )

pi.set_PWM_dutycycle( RED_PIN,  RED * RED_OFFSET / 100 )
pi.set_PWM_dutycycle( GREEN_PIN, GREEN * GREEN_OFFSET / 100 )
pi.set_PWM_dutycycle( BLUE_PIN, BLUE * BLUE_OFFSET / 100 )




