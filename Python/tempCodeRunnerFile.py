
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

ol = pd.read_csv(dir_path+"\\"+dir_list[3])

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