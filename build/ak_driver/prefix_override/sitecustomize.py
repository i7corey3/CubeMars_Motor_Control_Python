import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/corey/CubeMars_Motor_Control_Python/install/ak_driver'
