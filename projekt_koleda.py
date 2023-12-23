import sounddevice as sd
from numpy import pi
import numpy as np

fs = 44100
dt = 1/fs

t1 = np.arange(0, 2, dt)
t2 = np.arange(0, 1, dt)
t4 = np.arange(0, 1/2, dt)
t8 = np.arange(0, 1/4, dt)
t16 = np.arange(0, 1/8, dt)
t6 = np.arange(0, 6/4, dt)
t12 = np.arange(0, 3/8, dt)

h3         = 246.94
c4         = 261.63
d4         = 293.7
e4         = 329.63
f4         = 349.23
g4         = 392.00
a4         = 440.00
h4         = 493.88
c5         = 523.25

h3_16 = np.sin(2*pi*h3*t16)
c4_4 = np.sin(2*pi*c4*t4)
c4_8 = np.sin(2*pi*c4*t8)
g4_4 = np.sin(2*pi*g4*t2)
g4_8 = np.sin(2*pi*g4*t8)
a4_4 = np.sin(2*pi*a4*t4)
a4_8 = np.sin(2*pi*a4*t8)
d4_2 = np.sin(2*pi*d4*t2)
d4_4 = np.sin(2*pi*d4*t4)
d4_8 = np.sin(2*pi*d4*t8)
e4_4 = np.sin(2*pi*e4*t4)
e4_8 = np.sin(2*pi*e4*t8)
f4_8 = np.sin(2*pi*f4*t8)
h4_8 = np.sin(2*pi*h4*t8)
c5_4 = np.sin(2*pi*c5*t4)
c5_8 = np.sin(2*pi*c5*t8)
stupid_f4 = np.sin(2*pi*f4*t6)
even_more_stupid_g4 = np.sin(2*pi*g4*t12)

x = np.concatenate((c4_8, c5_8, c5_4, h4_8, a4_8, a4_8, a4_8, a4_4, g4_8, f4_8, e4_8, g4_8, c5_8, g4_8, f4_8, e4_8, e4_4, d4_2, c4_8, c5_8, c5_4, h4_8, a4_8, a4_8, a4_8, a4_4, g4_8, f4_8, e4_8, g4_8, c5_8, g4_8, f4_8, e4_8, e4_4, d4_2, stupid_f4, d4_8, e4_8, f4_8, g4_8, g4_8, e4_4, g4_4, stupid_f4, d4_8, e4_8, f4_8, g4_8, g4_8, e4_4, g4_4, stupid_f4, d4_8, e4_8, f4_8, g4_8, g4_8, e4_4, g4_8, g4_8, stupid_f4, d4_8, e4_8, f4_8, even_more_stupid_g4, h3_16, d4_4, c4_4))

sd.play(x, fs)
sd.wait()