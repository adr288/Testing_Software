import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

#Read from the text file and replace the non numerical values with nan
df = pd.read_csv("DCIU_result.txt").apply(pd.to_numeric, errors='coerce')
DCIU_data = df.values #convert to a numpy list


for i in range(DCIU_data.shape[1]):
	voltage_values = DCIU_data[:,i][~np.isnan(DCIU_data[:,i])]
	time = np.arange(0,voltage_values.shape[0])
	
	#Plot
	plt.scatter(time,voltage_values, linewidths=0.1)
	plt.xlabel('time')
	plt.ylabel('voltage')
	plot_name = "Plots/" +'plot_' + str(i) + '.png' 
	plt.savefig(plot_name)
	plt.clf()
	print(i)





