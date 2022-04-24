# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:09:08 2022

@author: chris
"""
import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp
import matplotlib.pyplot as plt

#import csv
hbcsv = hp.get_data('heartbeat.csv')

rate = 500

plt.figure(figsize = (10, 5))
plt.plot(hbcsv)

wd, m = hp.process(hbcsv, rate)
hp.plotter(wd, m)
