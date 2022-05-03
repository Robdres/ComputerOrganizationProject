import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cycler


languaje = 'java'
data = pd.read_excel('./results.xlsx', sheet_name=languaje)

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
plt.ylabel("Tiempo de ejecucion del proceso [s]",color =color2)
plt.plot(dimension,time,color = color1)
ax.set_facecolor(background)
plt.savefig('./'+languaje+'Time.png')


print(data.head())
