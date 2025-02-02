import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pandas.core.common import flatten
from pandas import read_csv
import dane

hx=0.1
liczba_dni=1
Tmax=60*60*24*liczba_dni
ht=0.1
X=np.arange(0,7.2,hx)
N=len(X)
T=np.arange(0,Tmax+ht, ht)
M=600
k=len(T)//M+1
#print(k)
X,Y=np.meshgrid(X,X)

U=read_csv("macierze_wroclaw_bezzmiany.csv", delimiter=",",header=None)
U=U.to_numpy()
U=U.reshape(k,N,N)


fig=plt.figure()

plt.xlim((np.min(X), np.max(X)))
plt.ylim((np.min(Y), np.max(Y)))
plt.xlabel("x")
plt.ylabel("y")
plt.pcolormesh(X,Y,U[30,:,:],vmin=-5+dane.K,vmax=35+dane.K,cmap='jet')
plt.title("Ciepło w godzinie 0:30")
plt.colorbar(ticks=np.arange(-5+dane.K,41+dane.K,5), format=mticker.FixedFormatter(np.arange(-5,41,5)))
plt.show()

