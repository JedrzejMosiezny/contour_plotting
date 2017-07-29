import os, sys
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import cm
import scipy.interpolate as scin

#path = str(input('Podaj ścieżkę do katalogu z plikami: ')) #Tutaj można skopiować ścieżkę
#result_file = input('Podaj nazwę pliku wyjściowego: ')



#path = 'C:/Users/HP/Dysk Google/ICS/reburning/badania/Wyniki/TXT/Wyniki/Reburning_29_05/dobre/' #ścieżka do katalogu z interesującymi nas plikami
#lista = os.listdir(path)            #Tworzy listę z plików w danym katalogu
#print(lista)                        #Wyświetla listę plików

x = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['    x-coordinate'])
x = x['    x-coordinate'].values.tolist()
#print(x)
#print(max(x))
#print(min(x))

y = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['    y-coordinate'])
y = y['    y-coordinate'].values.tolist()
#print(y)

o2 = pd.read_csv('NG_SG01-03-C01-00500_cross-section.dat', usecols=['          o2_dry'])
o2 = o2['          o2_dry'].values.tolist()
#print(o2)

#Xi, Yi = np.meshgrid(x,y)
#rbf = scin.griddata(x, y, o2, method='linear')
#chart = rbf(Xi, Yi)

plt.figure(figsize=(7,10))
#plt.contourf(x,y,o2)

#plt.contourf(chart)
plt.scatter(x, y, s=21, c=o2, marker = 'o', cmap = cm.jet)
#plt.xlim(-0.1,0.0)
#plt.ylim(0.,0.4)
plt.colorbar()
plt.show()



input('cos')
