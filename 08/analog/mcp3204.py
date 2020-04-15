import pigpio

class mcp3204:
    def __init__( self, handle, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.pi = handle
        
        self.spi = self.pi.spi_open( self.ss, self.speed )
                
    def get_value( self, ch ):
        command = 0x68 | ( 0x18 * ch ) 
        ( count, data ) = self.pi.spi_xfer( self.spi, [ command, 0x00  ] )

        value = ( data[0] << 8 | data[1] ) & 0x3ff
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 1023 )


