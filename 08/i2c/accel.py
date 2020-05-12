import pigpio
from lis3dh import lis3dh
import time

lis3dh_addr = 0x18
i2c_channel = 1

pi = pigpio.pi()

accel = lis3dh( pi, i2c_channel, lis3dh_addr )

while True:
    ( x, y, z ) = accel.read_accel()
    print ( "x:", x, "  y:", y, "  z:", z )

    ( x_angle, y_angle ) = accel.conv_angle( x, y, z )
    print ( "X Angle:", x_angle , " Y Angle:", y_angle )

    time.sleep(1)
