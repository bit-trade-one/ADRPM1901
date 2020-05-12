import pigpio

MOTOR_1_PIN = 12
MOTOR_2_PIN = 16

SPEED = 20

pi = pigpio.pi()

pi.set_mode( MOTOR_1_PIN, pigpio.OUTPUT )
pi.set_mode( MOTOR_2_PIN, pigpio.OUTPUT )

pi.set_PWM_frequency( MOTOR_1_PIN, 50 )
pi.set_PWM_frequency( MOTOR_2_PIN, 50 )

pi.set_PWM_range( MOTOR_1_PIN, 100 )
pi.set_PWM_range( MOTOR_2_PIN, 100 )

pi.set_PWM_dutycycle( MOTOR_1_PIN,  SPEED )
pi.set_PWM_dutycycle( MOTOR_2_PIN,  0 )




