from helper import *
from Stage import *

xaxis = Stage(0x32, 6000, 1)
print(xaxis.address)
print(xaxis.getAddress())
print(2 * xaxis.getAddress())
while True:
    bus = smbus.SMBus(1)

    next = input('What do you want to do next?')
    print(next)
    if next == 1:
        temp = bus.read_i2c_block_data(0x32, 19)
        print('temp', temp)
    elif next == '2':
        moveToNew = input('Where should the stage move next?')
        # com = xaxis.buildCommand('08',encoderConvert(moveToNew))
        # print(com)
        # xaxis.calibrate()
        # bus.write_i2c_block_data(0x32, 0, [100, 60, 48, 56, 32, 48, 48, 48, 48, 48, 51, 69, 56, 62, 13])
        xaxis.sendCommand('08', encoderCountConvert(moveToNew))





