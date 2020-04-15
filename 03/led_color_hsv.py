import pigpio
import hsv_to_rgb

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

RED_OFFSET = 100
GREEN_OFFSET = 60
BLUE_OFFSET = 80

HUE = 70
STRONG = 100
VALUE = 100

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

( red, green, blue ) = hsv_to_rgb.hsv_to_rgb( HUE, STRONG, VALUE )

pi.set_PWM_dutycycle( RED_PIN, red * RED_OFFSET / 100 )
pi.set_PWM_dutycycle( GREEN_PIN, green * GREEN_OFFSET / 100 )
pi.set_PWM_dutycycle( BLUE_PIN, blue * BLUE_OFFSET / 100 )




