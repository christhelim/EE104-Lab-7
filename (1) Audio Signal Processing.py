# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:44:33 2022

@author: chris
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import statistics as stats
from scipy.io import wavfile
from scipy import fftpack, signal

#amplitudes
a1 = 120
a2 = 411
a3 = 295

#frequencies in Hz
f1 = 1230
f2 = 690
f3 = 430

#periods in s
t1 = 1/f1
t2 = 1/f2
t3 = 1/f3

#time divisions
time = 1/10000
tdiv = np.arange(0, 1, time)

#3 signals
s1 = a1*(np.sin(2 * np.pi / t1 * tdiv))
s2 = a2*(np.sin(2 * np.pi / t2 * tdiv))
s3 = a3*(np.sin(2 * np.pi / t3 * tdiv))

#all 3 signals combined
s = s1 + s2 + s3
plt.figure(figsize = (45, 25))
plt.title('Graph of 3 Tones (1230, 690, and 430Hz)', fontsize = 80)
plt.ylabel('Amplitude', fontsize = 50)
plt.xlabel('Time (s)', fontsize = 50)
plt.xticks(fontsize = 40)
plt.yticks(fontsize = 40)
plt.xlim(0, 0.5)
plt.plot(tdiv, s, 'purple')

#.wav generation
wavfile.write('3ToneSignal.wav', 44100, s.astype(np.int16))

#frquency domain
fd = fftpack.fft(s)
fr = np.abs(fd)**2
freq = fftpack.fftfreq(s.size, d = time)
plt.figure(figsize=(45, 25))
plt.title('Frequency Domain Plot of 3-Tone Signal', fontsize = 80)
plt.ylabel('Power', fontsize=50)
plt.xlabel('Frequency (Hz)', fontsize=50)
plt.xticks(fontsize = 40)
plt.yticks(fontsize = 40)
plt.xlim(-2000, 2000)
plt.plot(freq, fr)