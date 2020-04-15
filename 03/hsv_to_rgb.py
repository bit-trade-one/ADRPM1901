
def hsv_to_rgb( h, s, v ):
	h = h / 100.0
	s = s / 100.0
	v = v / 100.0

	r = 0.0
	g = 0.0
	b = 0.0

	if s == 0.0:
		return( v, v, v )
	i = int( h * 6.0 )
	f = ( h * 6.0 ) - float(i)
	p = v * ( 1.0 - s )
	q = v * ( 1.0 - s * f )
	t = v * ( 1.0 - s * ( 1.0 - f ) )
	i = i % 6
	if ( i == 0 ):
		r = v
		g = t
		b = p
	elif ( i == 1 ):
		r = q
		g = v
		b = p
	elif ( i == 2 ):
		r = p
		g = v
		b = t
	elif ( i == 3 ):
		r = p
		g = q
		b = v
	elif ( i == 4 ):
		r = t
		g = p
		b = v
	elif ( i == 5 ):
		r = v
		g = p
		b = q

	return ( int(r * 100), int(g * 100), int(b * 100) )

