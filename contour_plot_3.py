import os, sys
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.interpolate as scin
from matplotlib.mlab import griddata
import matplotlib.patches as patches
#from matplotlib.patches import Patch

#path = str(input('Podaj ścieżkę do katalogu z plikami: ')) #Tutaj można skopiować ścieżkę
#result_file = input('Podaj nazwę pliku wyjściowego: ')



#path = 'C:/Users/HP/Dysk Google/ICS/reburning/badania/Wyniki/TXT/Wyniki/Reburning_29_05/dobre/' #ścieżka do katalogu z interesującymi nas plikami
#lista = os.listdir(path)            #Tworzy listę z plików w danym katalogu
#print(lista)                        #Wyświetla listę plików

x = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['    x-coordinate'])
x = x['    x-coordinate'].values.tolist()
new_x = [i*(-1) for i in x]

x = x + new_x

#print(max(x))
#print(min(x))

y = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['    y-coordinate'])
y = y['    y-coordinate'].values.tolist()
y = y + y
#print(y)

o2 = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['          o2_dry'])
o2[o2>15] = 15     #obcięcie wszystkich wartości powyżej (tutaj akurat 15)
o2 = o2['          o2_dry'].values.tolist()
o2 = o2 + o2
#print(o2)

#Xi, Yi = np.meshgrid(x,y)
#rbf = scin.griddata(x, y, o2, method='linear')
#chart = rbf(Xi, Yi)


#grid(x, y, o2, resX=100, resY=100)
Xi = np.linspace(min(x), max(x), num=500)
Yi = np.linspace(min(y), max(y), num=500)
Z = griddata(x, y, o2, Xi, Yi, interp = 'linear')
X, Y = np.meshgrid (Xi, Yi)


plt.figure(figsize=(5,10))
plt.contourf(X,Y,Z,100,cmap=cm.jet)
#box.Rectangle((0.1,0.1),0.5, 0,5, fill='white', edgecolor='none')

#plt.contourf(chart)
#plt.scatter(x, y, s=21, c=o2, marker = 'o', cmap = cm.jet)
#plt.xlim(-0.1,0.0)
#plt.ylim(0.,0.4)
plt.colorbar()
plt.show()



input('cos')
