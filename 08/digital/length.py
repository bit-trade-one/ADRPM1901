import pigpio
import time

TRIG_PIN = 6
ECHO_PIN = 5

pi = pigpio.pi()

pi.set_mode( TRIG_PIN, pigpio.OUTPUT )
pi.set_mode( ECHO_PIN, pigpio.INPUT )

pi.write( TRIG_PIN, pigpio.LOW )
time.sleep( 1 )

def mesure():
    pi.write( TRIG_PIN, pigpio.HIGH )
    time.sleep(0.00001)
    pi.write( TRIG_PIN, pigpio.LOW )
    sigon = 0
    while ( pi.read( ECHO_PIN ) == pigpio.LOW ):
        sigoff = time.time()
    while (pi.read( ECHO_PIN ) == pigpio.HIGH ):
        sigon = time.time()
    if ( sigon == 0 ):
        return ( -1 )
    else:
        return ( sigon - sigoff ) * 17000

while True:
    length = mesure()
    if ( length == -1 ):
        print ( "Can't mesure." )
    else:
        print ( "Distance:" , mesure() , "cm" )
    time.sleep(1)
