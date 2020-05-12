import pigpio

LED_PIN = 14
DUTY = 30

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( LED_PIN, 50 )
pi.set_PWM_range( LED_PIN, 100 )

pi.set_PWM_dutycycle( LED_PIN,  DUTY )




