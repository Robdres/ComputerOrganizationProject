import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cycler


lan1 = 'assembly'
lan2 = 'javaScript'
lan3 = 'python'
lan4 = 'cpp'
lan5 = 'java'
assembly = pd.read_excel('./results.xlsx',sheet_name=lan1)
javaScript = pd.read_excel('./results.xlsx',sheet_name=lan2)
python = pd.read_excel('./results.xlsx',sheet_name=lan3)
cpp = pd.read_excel('./results.xlsx',sheet_name=lan4)
java = pd.read_excel('./results.xlsx',sheet_name=lan5)

color1 = '#11c700'
color2 = '#15ff00'
color3 = '#0da100'
background = '#151515'
white =  '#ffffff'

dimensionAs   = assembly['dimension']
timeAs        = assembly['time']
memoryAs      = assembly['memory']
dimensionJs   = javaScript['dimension']
timeJs        = javaScript['time']
memoryJs     = javaScript['memory']
dimensionPy   = python['dimension']
timePy        = python['time']
memoryPy      = python['memory']
dimensionJava = java['dimension']
timeJava      = java['time']
memoryJava    = java['memory']
dimensionCpp  = cpp['dimension']
timeCpp       = cpp['time']
memoryCpp     = cpp['memory']

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
plt.ylabel("Tiempo del proceso [B]",color =color2)
plt.plot(dimensionAs,timeAs,color= color1, label = "Assembly")
plt.plot(dimensionJs,timeJs,color = 'red', label = "javaScript")
plt.plot(dimensionPy,timePy,color = '#0a6b5c', label = "python")
plt.plot(dimensionJava,timeJava,color = 'white', label = "Java")
plt.plot(dimensionCpp,timeCpp,color = 'blue', label = "Cpp")


plt.legend()
ax.set_facecolor(background)

plt.savefig('./resultsTime.png')

