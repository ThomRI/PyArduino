# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:45:49 2018

@author: Thom
"""
import serial

class Arduino():
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(port, baudrate=baudrate)
        
        ''' Welcome sequence '''
        seq = [0, 255, 0]
        rec_char = -1
        for i in range(len(seq)):
            print("Waiting for welcome char :", seq[i], "...")
            while ord(rec_char) != seq[i]:
                rec_char = self.serial.read(1)
        print("Welcomed !\n")
        
        ''' Commands '''
        self.DONE = 100
        self.PIN_MODE = 101
        self.DIGITAL_WRITE = 102
        self.DIGITAL_READ = 103
        self.ANALOG_WRITE = 104
        self.ANALOG_READ = 105
        
        ''' Defines '''
        self.LOW = 0
        self.HIGH = 1
        self.INPUT = 0
        self.OUTPUT = 1
    
    def sendCommand(self, commandId, args, waitForDone = False):
        self.serial.write(chr(commandId))
        
        for arg in args:
            self.serial.write(chr(arg))
        
        if waitForDone:
            rec_char = -1
            while ord(rec_char) != self.DONE:
                rec_char = self.serial.read(1)
    
    def pinMode(self, pin, mode):
        self.sendCommand(self.PIN_MODE, [pin, mode], True)
        
    def digitalWrite(self, pin, output):
        self.sendCommand(self.DIGITAL_WRITE, [pin, output], True)
        
    def digitalRead(self, pin):
        self.sendCommand(self.DIGITAL_READ, [pin])
        return ord(self.serial.read(1))
        
    def analogWrite(self, pin, value):
        self.sendCommand(self.ANALOG_WRITE, [pin, value], True)
        
    def analogRead(self, pin):
        self.sendCommand(self.ANALOG_READ, [pin])
        
        char1 = ord(self.serial.read(1))
        char2 = ord(self.serial.read(1))
        
        return char1 * 0x100 + char2

    def close(self):
        self.ser.close()
                