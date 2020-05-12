import pigpio

MOTOR_1_PIN = 12
MOTOR_2_PIN = 16

pi = pigpio.pi()

pi.set_mode( MOTOR_1_PIN, pigpio.OUTPUT )
pi.set_mode( MOTOR_2_PIN, pigpio.OUTPUT )

pi.write( MOTOR_1_PIN, pigpio.LOW )
pi.write( MOTOR_2_PIN, pigpio.LOW )

