import pigpio
import time, math

class lis3dh:
    def __init__( self, handle, ch, addr ):
        self.addr = addr
        self.ch = ch
        self.pi = handle

        self.i2c = self.pi.i2c_open( self.ch, self.addr )
        
        self.pi.i2c_write_byte_data( self.i2c, 0x20, 0x77 )

    def conv_two_byte( self, high, low ):
        dat = high << 8 | low
        if ( high >= 0x80 ):
            dat = dat - 65536
        dat = dat >> 4
        return ( dat )

    def conv_angle( self, x, y, z ):
        x_angle = math.degrees( math.atan2( x, math.sqrt( y ** 2 + z ** 2 ) ) )
        y_angle = math.degrees( math.atan2( y, math.sqrt( x ** 2 + z ** 2 ) ) )
        return ( x_angle, y_angle )

    def read_accel( self ):
        lb = self.pi.i2c_read_byte_data( self.i2c, 0x28 )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x29 )
        x = self.conv_two_byte( hb, lb )

        lb = self.pi.i2c_read_byte_data( self.i2c, 0x2a )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x2b )
        y = self.conv_two_byte( hb, lb )

        lb = self.pi.i2c_read_byte_data( self.i2c, 0x2c )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x2d )
        z = self.conv_two_byte( hb, lb )
    
        return ( x, y, z )
    


