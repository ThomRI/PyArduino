# -*- coding: utf-8 -*-
"""
Created on Sun May 20 14:55:58 2018

@author: Ira
"""

from arduino import Arduino
from math import sin, floor
import numpy as np
import matplotlib.pyplot as plt
import time

msleep = lambda t: time.sleep(1. * t / 1000)

ard = Arduino("COM3", 115200)

ard.pinMode(12, ard.OUTPUT)
ard.pinMode(13, ard.OUTPUT)
ard.pinMode(5, ard.OUTPUT)
ard.pinMode(3, ard.INPUT)
ard.pinMode(1, ard.INPUT)

def left():
    ard.digitalWrite(12, ard.LOW)
    ard.digitalWrite(13, ard.HIGH)
    
def right():
    ard.digitalWrite(12, ard.HIGH)
    ard.digitalWrite(13, ard.LOW)

def stop():
    ard.digitalWrite(13, ard.LOW)
    ard.digitalWrite(12, ard.LOW)
'''
delay = 10

T = 400 # Aller (ms)
w = np.pi / T
    
X = [x for x in np.linspace(0, T, floor(T / delay))]
Y = [abs(sin(w * t)) for t in X]

m = 0.45 # alpha max
n = 0.4 # alpha min

A = [floor(((m - n) * y + n) * 255) for y in Y]

V = []

plt.plot(X, A, "o")

for aller in range(10):
    if aller % 2 == 0:  left()
    else:               right()

    for i in range(len(X)):    
        ard.analogWrite(5, A[i])
        if aller == 0: V.append(ard.analogRead(1) * m / 1023)   
        msleep(delay)
        
stop()
ard.digitalWrite(5, ard.LOW)

ard.end()

plt.plot(X, V, "o")
plt.show()
'''

print(ard.analogRead(1))
ard.end()

'''
for i in range(15):
    alpha = sin()

alpha = 0.5
ard.analogWrite(5, floor(alpha * 255))

freq = 2
T = 1./freq

for i in range(5):
    right()
    msleep((T / 2) * 1000)
    left()
    msleep((T / 3) * 1000)



''

''
a = (1023. / 2)
while True:
    r = ard.analogRead(3) - a
    print(r)
    
    if r > 0:   right()
    else:       left()
    
    alpha = abs(r) / a
    ard.analogWrite(5, floor(alpha * 255))


stop()
ard.digitalWrite(5, ard.LOW)

ard.end()
'''