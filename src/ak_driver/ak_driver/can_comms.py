import can
import os

class CANComms:
    def __init__(self, channel, bitrate):
        self.channel = channel
        self.bitrate = bitrate

        self.CAN_PACKET_SET_DUTY = 0
        self.CAN_PACKET_SET_CURRENT = 1
        self.CAN_PACKET_SET_CURRENT_BRAKE = 2
        self.CAN_PACKET_SET_RPM = 3
        self.CAN_PACKET_SET_POS = 4
        self.CAN_PACKET_SET_ORIGIN_HERE = 5 
        self.CAN_PACKET_SET_POS_SPD = 6


    def setup(self):
        os.system(f"sudo ifconfig can{self.channel} down")
        os.system(f"sudo ip link set can{self.channel} type can bitrate {self.bitrate} dbitrate 1000000 fd on")
        os.system(f"sudo ifconfig can{self.channel} up")

    
    def comm_can_set_rpm(self, channel_id, rpm): 
        
        buffer = [0x00, 0x00, 0x00, 0x00]
        buffer[0] = rpm >> 24
        buffer[1] = rpm >> 16 & 0x0FFF
        buffer[2] = rpm >> 8 & 0x00FF
        buffer[3] = rpm & 0x00FF
        print(list(hex(i) for i in buffer))
        id = channel_id | self.CAN_PACKET_SET_RPM << 8
        print(hex(id))
        self.can_transmit(id, buffer, len(buffer))
        
        
    def can_transmit(self, id, data, length):
        if length > 8:
            length = 8
        with can.Bus(channel="can0", interface='socketcan')as bus:
            msg = can.Message(arbitration_id=id, data=[data[0], data[1], data[2],data[3], 0, 0, 0, 0], is_extended_id=True)
            bus.send(msg)
            print(bus.channel_info)

if __name__ == "__main__":

    c = CANComms(0, 1000000)
    #c.setup()
    c.comm_can_set_rpm(0x00002968, 12000)

