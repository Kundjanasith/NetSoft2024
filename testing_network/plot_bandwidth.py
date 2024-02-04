import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

plt.title('FROM 10.10.100.45')
df = pd.read_csv('check_bandwidth.csv')
df[['l0','l1','l2','l3']] = df['IP'].str.split('.', expand=True) 
plt.bar(df['l3'],df['LATENCY'])
plt.ylabel('Latency [ms]')
plt.xlabel('TO 10.10.100.__')
plt.xticks(rotation=90)
plt.savefig('plot_bandwidth.png',bbox_inches='tight')

# EXP
