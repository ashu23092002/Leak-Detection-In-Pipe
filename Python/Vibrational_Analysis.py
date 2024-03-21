# https://data.mendeley.com/datasets/tbrnp6vrnj/1
# Reference dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.fftpack import fft

nl = pd.read_csv('BR_NL_0.18 LPS_A1.csv')

nl_time = nl.loc[:,"Sample"].values
nl_sample = nl.loc[:,"Value"].values

cc = pd.read_csv('BR_CC_0.18 LPS_A1.csv')

cc_time = cc.loc[:,"Sample"].values
cc_sample = cc.loc[:,"Value"].values

gl = pd.read_csv('BR_GL_0.18 LPS_A1.csv')

gl_time = gl.loc[:,"Sample"].values
gl_sample = gl.loc[:,"Value"].values

lc = pd.read_csv('BR_LC_0.18 LPS_A1.csv')

lc_time = lc.loc[:,"Sample"].values
lc_sample = lc.loc[:,"Value"].values

ol = pd.read_csv('BR_OL_0.18 LPS_A1.csv')

ol_time = ol.loc[:,"Sample"].values
ol_sample = ol.loc[:,"Value"].values

nl_output = fft(nl_sample)
cc_output = fft(cc_sample)
gl_output = fft(gl_sample)
lc_output = fft(gl_sample)
ol_output = fft(ol_sample)

"""Plotting on single plot"""
# plt.plot(nl_output)
# plt.plot(cc_output)
# plt.plot(gl_output)
# plt.plot(lc_output)
# plt.plot(ol_output)

"""Plotting on different plots"""
figure, axis = plt.subplots(3,2)

axis[0,0].plot(nl_output)
axis[1,0].plot(cc_output)
axis[1,1].plot(gl_output)
axis[2,0].plot(lc_output)
axis[2,1].plot(ol_output)

plt.show()