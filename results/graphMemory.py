import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cycler


language = 'assembly'
data = pd.read_excel('./results.xlsx',sheet_name=language)

color1 = '#11c700'
color2 = '#15ff00'
color3 = '#0da100'
background = '#151515'
white =  '#ffffff'

dimension = data['dimension']
time= data['time']
memory = data['memory']



plt.rc('axes', facecolor=white, edgecolor='none',
       axisbelow=True, grid=True )
plt.rc('grid', color=white, linestyle='solid')
plt.rc('xtick', direction='out', color=white)
plt.rc('ytick', direction='out', color=white)
plt.rc('patch', edgecolor=white)
plt.rc('lines', color=color1,linewidth=2)

plt.figure(facecolor=background)

ax = plt.axes()
plt.xlabel("Dimension de la matriz cuadrada",color= color2)
plt.ylabel("Memoria utilizada por el proceso [B]",color =color2)
p = plt.plot(dimension,memory,color= color1)
ax.set_facecolor(background)
plt.savefig('./'+language+'Memory.png')

print(data.head())
