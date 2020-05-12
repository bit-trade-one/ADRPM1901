import pigpio
import time

SW_PIN = 25
LED_PIN = 14

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW_PIN, pigpio.PUD_UP )
pi.set_mode( LED_PIN, pigpio.OUTPUT )

mode = 0

while True:
    sw = pi.read( SW_PIN )
    if ( sw == pigpio.LOW ):
        if ( mode == 0 ):
            pi.write( LED_PIN, pigpio.HIGH )
            mode = 1
        else:
            pi.write( LED_PIN, pigpio.LOW )
            mode = 0

        while ( pi.read( SW_PIN ) == pigpio.LOW ):
            time.sleep( 0.1 )



