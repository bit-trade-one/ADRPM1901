import pigpio

PIN = [12, 14, 15, 16, 17, 20, 21, 22, 27 ]

pi = pigpio.pi()

i = 0
while ( i < len(PIN) ):
	pi.set_mode( PIN[i], pigpio.OUTPUT )
	pi.write( PIN[i], pigpio.LOW )
	i = i + 1


