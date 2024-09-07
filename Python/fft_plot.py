# https://data.mendeley.com/datasets/tbrnp6vrnj/1
# Reference dataset

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.fftpack import fft

figprop = 1.2

def multiPlot(nl_output,cc_output,gl_output,lc_output,ol_output):
    """Plotting on single plot"""
    fig, ax = plt.subplots()

    fig.set_figheight(figprop*fig.get_figheight())
    fig.set_figwidth(figprop*fig.get_figwidth())

    (line1, )=ax.plot(abs(nl_output),color="green",label="nl")
    (line2, )=ax.plot(abs(cc_output),color="violet",label="cc")
    (line3, )=ax.plot(abs(gl_output),color="red",label="gl")
    (line4, )=ax.plot(abs(lc_output),color="blue",label="lc")
    (line5, )=ax.plot(abs(ol_output),color="yellow",label="ol")
    
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Amplitude")

    leg = ax.legend(fancybox=True, shadow=True)

    lines = [line1, line2, line3, line4, line5]
    map_legend_to_ax = {}

    pickradius = 5

    for legend_line, ax_line in zip(leg.get_lines(), lines):
        legend_line.set_picker(pickradius)  # Enable picking on the legend line.
        map_legend_to_ax[legend_line] = ax_line

    def on_pick(event):
        legend_line = event.artist

        if legend_line not in map_legend_to_ax:
            return

        ax_line = map_legend_to_ax[legend_line]
        visible = not ax_line.get_visible()
        ax_line.set_visible(visible)
        
        legend_line.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()
    
    fig.canvas.mpl_connect('pick_event', on_pick)

    leg.set_draggable(False)

def subPlot(nl_output,cc_output,gl_output,lc_output,ol_output):
    """Plotting on different plots"""
    fig, ax = plt.subplots(3,2)
    
    fig.set_figheight(figprop*fig.get_figheight())
    fig.set_figwidth(figprop*fig.get_figwidth())

    ax[0,0].plot(abs(nl_output),color="green",label="nl")
    ax[1,0].plot(abs(cc_output),color="violet",label="cc")
    ax[1,1].plot(abs(gl_output),color="red",label="gl")
    ax[2,0].plot(abs(lc_output),color="blue",label="lc")
    ax[2,1].plot(abs(ol_output),color="black",label="ol")
    
    fig.supxlabel("Frequency")
    fig.supylabel("Amplitude")
    
    fig.legend(fancybox=True, shadow=True)
    # ax.set_xlabel("Frequency")
    # ax.set_ylabel("Amplitude")
    # ax.legend()

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

dir_list = os.listdir(dir_path)
dir_list = [file for file in dir_list if file.endswith('.csv')]
print(dir_list)

nl = pd.read_csv(dir_path+"\\"+dir_list[3])   

nl_time = nl.loc[:,"Sample"].values
nl_sample = nl.loc[:,"Value"].values

cc = pd.read_csv(dir_path+"\\"+dir_list[0])

cc_time = cc.loc[:,"Sample"].values
cc_sample = cc.loc[:,"Value"].values

gl = pd.read_csv(dir_path+"\\"+dir_list[1])

gl_time = gl.loc[:,"Sample"].values
gl_sample = gl.loc[:,"Value"].values

lc = pd.read_csv(dir_path+"\\"+dir_list[2])

lc_time = lc.loc[:,"Sample"].values
lc_sample = lc.loc[:,"Value"].values

ol = pd.read_csv(dir_path+"\\"+dir_list[4])

ol_time = ol.loc[:,"Sample"].values
ol_sample = ol.loc[:,"Value"].values


nl_output = fft(nl_sample)
cc_output = fft(cc_sample)
gl_output = fft(gl_sample)
lc_output = fft(lc_sample)
ol_output = fft(ol_sample)

print(type(lc_time))

# nl_PSD = nl_output * np.conj(nl_output) / len()

multiPlot(nl_output,cc_output,gl_output,lc_output,ol_output)
# subPlot(nl_output,cc_output,gl_output,lc_output,ol_output)

# Sampling rate of 51.2kS/s/ch
plt.xlim(0,51200)

plt.show()