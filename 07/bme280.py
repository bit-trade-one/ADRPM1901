import pigpio

class bme280:
	def __init__( self, handle, ch, addr ):
		self.addr = addr
		self.ch = ch
		self.pi = handle
		self.cb_temp = []
		self.cb_humi = []
		self.cb_press = []
		self.t_fine = 0.0
		self.i2c = self.pi.i2c_open( self.ch, self.addr )

	def setup(self):
		self.pi.i2c_write_byte_data( self.i2c, 0xf2, 0x01 )
		self.pi.i2c_write_byte_data( self.i2c, 0xf4, 0x27 )
		self.pi.i2c_write_byte_data( self.i2c, 0xf5, 0xa0 )
		
		self.set_calib()

	def set_calib(self):
		buf = []
		for i in range ( 0x88, 0x88 + 24 ):
			buf.append( self.pi.i2c_read_byte_data( self.i2c, i ) )
		buf.append( self.pi.i2c_read_byte_data( self.i2c, 0xA1 ) )
		for i in range ( 0xE1, 0xE1 + 7 ):
			buf.append( self.pi.i2c_read_byte_data( self.i2c, i ) )

		self.cb_temp.append((buf[1] << 8) | buf[0])
		self.cb_temp.append((buf[3] << 8) | buf[2])
		self.cb_temp.append((buf[5] << 8) | buf[4])
		self.cb_press.append((buf[7] << 8) | buf[6])
		self.cb_press.append((buf[9] << 8) | buf[8])
		self.cb_press.append((buf[11]<< 8) | buf[10])
		self.cb_press.append((buf[13]<< 8) | buf[12])
		self.cb_press.append((buf[15]<< 8) | buf[14])
		self.cb_press.append((buf[17]<< 8) | buf[16])
		self.cb_press.append((buf[19]<< 8) | buf[18])
		self.cb_press.append((buf[21]<< 8) | buf[20])
		self.cb_press.append((buf[23]<< 8) | buf[22])
		self.cb_humi.append( buf[24] )
		self.cb_humi.append((buf[26]<< 8) | buf[25])
		self.cb_humi.append( buf[27] )
		self.cb_humi.append((buf[28]<< 4) | (0x0F & buf[29]))
		self.cb_humi.append((buf[30]<< 4) | ((buf[29] >> 4) & 0x0F))
		self.cb_humi.append( buf[31] )

		for i in range(1,2):
			if self.cb_temp[i] & 0x8000:
				self.cb_temp[i] = (-self.cb_temp[i] ^ 0xFFFF) + 1

		for i in range(1,8):
			if self.cb_press[i] & 0x8000:
				self.cb_press[i] = (-self.cb_press[i] ^ 0xFFFF) + 1

		for i in range(0,6):
			if self.cb_humi[i] & 0x8000:
				self.cb_humi[i] = (-self.cb_humi[i] ^ 0xFFFF) + 1

	def calc_press( self, adc_P ):
		pressure = 0.0
		
		v1 = ( self.t_fine / 2.0) - 64000.0
		v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) *  self.cb_press[5]
		v2 = v2 + ((v1 * self.cb_press[4]) * 2.0)
		v2 = (v2 / 4.0) + (self.cb_press[3] * 65536.0)
		v1 = (((self.cb_press[2] * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8)  + ((self.cb_press[1] * v1) / 2.0)) / 262144
		v1 = ((32768 + v1) * self.cb_press[0]) / 32768
		
		if v1 == 0:
			return 0
		pressure = ((1048576 - adc_P) - (v2 / 4096)) * 3125
		if pressure < 0x80000000:
			pressure = (pressure * 2.0) / v1
		else:
			pressure = (pressure / v1) * 2
		v1 = (self.cb_press[8] * (((pressure / 8.0) * (pressure / 8.0)) / 8192.0)) / 4096
		v2 = ((pressure / 4.0) * self.cb_press[7]) / 8192.0
		pressure = ( pressure + ((v1 + v2 + self.cb_press[6]) / 16.0) ) / 100
		return ( pressure )

	def calc_temp( self, adc_T ):
		v1 = (adc_T / 16384.0 - self.cb_temp[0] / 1024.0) * self.cb_temp[1]
		v2 = (adc_T / 131072.0 - self.cb_temp[0] / 8192.0) * (adc_T / 131072.0 - self.cb_temp[0] / 8192.0) * self.cb_temp[2]
		self.t_fine = v1 + v2
		temperature = self.t_fine / 5120.0
		return( temperature )

	def calc_humi( self, adc_H ):
		var_h = self.t_fine - 76800.0
		if var_h != 0:
			var_h = (adc_H - (self.cb_humi[3] * 64.0 + self.cb_humi[4]/16384.0 * var_h)) * (self.cb_humi[1] / 65536.0 * (1.0 + self.cb_humi[5] / 67108864.0 * var_h * (1.0 + self.cb_humi[2] / 67108864.0 * var_h)))
		else:
			return 0
		var_h = var_h * (1.0 - self.cb_humi[0] * var_h / 524288.0)
		if var_h > 100.0:
			var_h = 100.0
		elif var_h < 0.0:
			var_h = 0.0
		return( var_h )
		
	def get_value( self ):
		data = []
		i = 0
		while ( i < 8 ):
			data.append( self.pi.i2c_read_byte_data( self.i2c, 0xf7 + i ) )
			i = i + 1

		press_mesure = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
		temp_mesure = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
		humi_mesure  = (data[6] << 8)  |  data[7]
		
		temp = self.calc_temp ( temp_mesure )
		humi = self.calc_humi ( humi_mesure )
		press = self.calc_press ( press_mesure )

		return( temp, humi, press)





