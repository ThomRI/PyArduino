# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:45:49 2018

@author: Thom
"""
import serial
import math

class Arduino():
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(port, baudrate=baudrate)
        
        ''' Welcome sequence '''
        seq = [0, 255, 0]
        rec_char = '1'
        for i in range(len(seq)):
            print("Waiting for welcome char :", seq[i], "...")
            while ord(rec_char) != seq[i]:
                rec_char = self.serial.read(1)
                if(rec_char == b''): rec_char = '1'
                print(rec_char)
                
        print("Welcomed !\n")
        
        ''' Commands '''
        self.DONE = 100
        self.END = 99
        
        self.PIN_MODE = 101
        self.DIGITAL_WRITE = 102
        self.DIGITAL_READ = 103
        self.ANALOG_WRITE = 104
        self.ANALOG_READ = 105
        
        self.SEQUENCE_PWM = 106
        
        ''' Defines '''
        self.LOW = 0
        self.HIGH = 1
        self.INPUT = 0
        self.OUTPUT = 1
        
        self.toByte = lambda n: bytes(chr(n), 'utf-8')
    
    def sendCommand(self, commandId, args = [], waitForDone = False):
        #print(self.toByte(commandId))
        self.serial.write(self.toByte(commandId))
        
        for arg in args:
            self.serial.write(self.toByte(arg))
        
        if waitForDone:
            rec_char = '1'
            while ord(rec_char) != self.DONE:
                rec_char = self.serial.read(1)
    
    def pinMode(self, pin, mode):
        self.sendCommand(self.PIN_MODE, [pin, mode], True)
        
    def digitalWrite(self, pin, output):
        self.sendCommand(self.DIGITAL_WRITE, [pin, output], True)
        
    def digitalRead(self, pin):
        self.sendCommand(self.DIGITAL_READ, [pin])
        return self.serial.read(1)
        
    def analogWrite(self, pin, value):
        if value > 255: value = 255
        elif value < 0: value = 0

        self.sendCommand(self.ANALOG_WRITE, [pin, (value >> 4) & 0xF, value & 0xF], True)
        
    def analogRead(self, pin):
        self.sendCommand(self.ANALOG_READ, [pin])
        
        valueMSB = ord(self.serial.read(1))
        valueNSB = ord(self.serial.read(1))
        valueLSB = ord(self.serial.read(1))
        
        return (valueMSB << 6) + (valueNSB << 2) + valueLSB
    
    
    def sequencePWM(self, datas, size):
        self.sendCommand(self.SEQUENCE, waitForDone = True)
        self.serial.write(self.toByte(size))
        
        for data in datas:
            self.serial.write(self.toByte(data))
    
    def end(self):
        self.sendCommand(self.END)
        self.close()

    def close(self):
        self.serial.close()
                