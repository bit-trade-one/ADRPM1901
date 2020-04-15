import pigpio
import time

SW_PIN = 25

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW_PIN, pigpio.PUD_UP )

while True:
	print( pi.read( SW_PIN ) )
	
	time.sleep( 0.5 )


