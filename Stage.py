# import smbus
from helper import *
class Stage:

    def __init__(self, address, position, bus):
        self.position = position
        self.address = address
        self.bus = bus
    # bus = smbus.SMBus(self.bus)
   # def getPosFromM3LS(self):

    def getPosition(self):
        return int(self.position)
    def getAddress(self):
        return self.address

    def buildCommand(self, commandCode, commandVars):
        ''''
        Function that builds a command that is ready to be sent to a stage. The command is output in a list that is
        comprised of the hexadecimal values
        '''

        command = [] #empty list to hold command
        command += ['0x' + str(int(self.address[2:]) << 1)]  # address of stage bit shifted 1 left
        command += ['0x3C'] # open carat
        for i in str(commandCode):
            command += [hex(ord(i))]
        command += ['0x20'] # space
        command += commandVars
        command += ['0x3E'] # close carat
        command += ['0x0D'] # carriage return
        return command

    def buildCommandNoVars(self, commandCode):
        ''''
        Function that builds a command that is ready to be sent to a stage. The command is output in a list that is
        comprised of the hexadecimal values
        '''

        command = []
        command += ['0x' + str(int(self.address[2:]) << 1)]
        command += ['0x3C']
        for i in str(commandCode):
            command += [hex(ord(i))]
        command += ['0x3E']
        command += ['0x0D']
        return command


    def write(self, command):
        bus.write_i2c_block_data(self.address, 0, command)
    def sendCommand(self, commandCode, commandVars):
        commandToSend = self.buildCommand(commandCode, commandVars)
        self.write(commandToSend)

    def sendCommandNoVars(self, commandCode):
        commandToSend = self.buildCommandNoVars(commandCode)
        self.write(commandToSend)

    def calibrate(self):
        self.sendCommand('87', ['0x35'])

    def startup(self):
        forwardStep = ['0x31', '0x20', '0x30', '0x30', '0x30', '0x30', '0x30', '0x30', '0x36', '0x34']
        backwardStep =
        self.sendCommand('06', ['0x31'] + ['0x20'] + encoderConvert(64))
    def getPositionFromM3LS(self):
        self.sendCommandNoVars(19)
        temp =[]
        temp = bus.read_i2c_block_data(32, char cmd)