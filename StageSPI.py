'''
This file contains the stage functions for the x and y axis communicating via SPI. DO NOT USE THIS FOR COMMUNICATING

WITH I2C Stages. It will fail. This only contains the Overide methods for the SPI stuff.


Last Modified: R. Nance 5/15/2018
#####################DO NOT EDIT BELOW INFORMATION##################################
Originating Branch: Master
Originally Created: R. Nance 05/2018
'''

from Stage import Stage

from helper import *
import time
import spidev
EXPECTED_RETURN_LENGTH = 24


class StageSPI(Stage):
    def __init__(self, bus, device, position):
        Stage.__init__(self, position)

        self.position = position
        self.bus = bus
        self.device = device
        self.home = 6000

        #self.axis = axis
        #stageAxis = axis
        #axis = spidev.SpiDev()
        #axis.open(bus, device)
        #axis.mode = 0b01
        #axis.max_speed_hz = 1000000

      #this is definitely not the right way to do this. Should do something with self here.

        axis = spidev.SpiDev()
        axis.open(self.bus, self.device)
        axis.mode = 0b01
        axis.max_speed_hz = 1000000
        self.axis = axis


    def write(self, command):
        """
        Function to write to the SPI Stages.
        :param command: Command in the form of a list of decimal integers, each of which represents an ascii character
        in the command to be sent to the stage.
        :return: NA
        """
        print(commandToString(command))  # print the command in a user readable format
        self.axis.writebytes(command)

    def read(self):
        """
        Reads from the output register of the stage
        :return: List of signed values that represent what is on the output register of the stage
        """
        temp = self.axis.readbytes(EXPECTED_RETURN_LENGTH)
        print('temp', temp)
        return_buffer = []
        for i in temp:
            return_buffer += str(chr(int(i)))
        print(return_buffer)
        return return_buffer




