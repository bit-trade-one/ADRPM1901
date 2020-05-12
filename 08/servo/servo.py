import pigpio

SERVO_PIN = 24

degree = 90

MIN_DEG = 0
MAX_DEG = 180
MIN_PULSE = 500
MAX_PULSE = 2400

a = float( MAX_PULSE - MIN_PULSE ) / float( MAX_DEG - MIN_DEG )
b = MAX_PULSE - MAX_DEG * a

if ( degree >= MIN_DEG and degree <= MAX_DEG ): 
    pulse = int( a * float( degree) + b )

    pi = pigpio.pi()
    pi.set_servo_pulsewidth( SERVO_PIN, pulse )


