import smbus
import time

def int_sw_swap(x):
    """Interpret integer as signed word with bytes swapped"""
    xl = x & 0xff
    xh = x >> 8
    xx = (xl << 8) + xh
    return xx - 0xffff if xx > 0x7fff else xx

class SensorITG3200(object):
    """ITG3200 digital gyroscope control class.
    Supports data polling at the moment.
    """
    def __init__(self, bus_nr, addr):
        self.bus = smbus.SMBus(bus_nr)
        self.addr = addr
        self.x_offset=0
        self.y_offset=0
        self.z_offset=0

    def default_init(self):
        self.bus.write_byte_data(self.addr, 0x3E, 0x80)
        self.bus.write_byte_data(self.addr, 0x15, 0)
        self.bus.write_byte_data(self.addr, 0x16, 0x18)
        x_offset_temp = 0
        y_offset_temp = 0
        z_offset_temp = 0
        for i in range(0,100):
            time.sleep(0.1)
            x, y, z = self.read_data()
            x_offset_temp += x
            y_offset_temp += y
            z_offset_temp += z

        self.x_offset = abs(x_offset_temp) / 100
        self.y_offset = abs(y_offset_temp) / 100
        self.z_offset = abs(z_offset_temp) / 100
        if x_offset_temp > 0:
            self.x_offset = -self.x_offset
        if y_offset_temp > 0:
            self.y_offset = -self.y_offset
        if z_offset_temp > 0:
            self.z_offset = -self.z_offset
        print("Calibrated!")
        print(self.x_offset)
        print(self.y_offset)
        print(self.z_offset)

    def read_data(self):
        gx = int_sw_swap(self.bus.read_word_data(self.addr, 0x1d))+self.x_offset
        gy = int_sw_swap(self.bus.read_word_data(self.addr, 0x1f))+self.y_offset
        gz = int_sw_swap(self.bus.read_word_data(self.addr, 0x21))+self.z_offset
        return (gx, gy, gz)
