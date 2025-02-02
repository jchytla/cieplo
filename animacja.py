import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import matplotlib.animation as anm
import matplotlib.gridspec as gridspec
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
print(k)
X,Y=np.meshgrid(X,X)

U=read_csv("macierze_wroclaw_okna.csv", delimiter=",",header=None)
U=U.to_numpy()
print(U.shape)
print(U[0][0])
U=U.reshape(k,N,N)
solution = U[::30,:, :]
#print(U[10,50,50]-273.15)
t_cp = T[::M]
t_cp=t_cp[::30]

fig=plt.figure()

plt.xlim((np.min(X), np.max(X)))
plt.ylim((np.min(Y), np.max(Y)))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ciepło w czasie")


pcolormesh = plt.pcolormesh(X,Y,solution[0,:,:],vmin=-5+dane.K,vmax=35+dane.K,cmap='jet')

plt.colorbar(ticks=np.arange(-5+dane.K,41+dane.K,5), format=mticker.FixedFormatter(np.arange(-5,41,5)))


def animation(j):
  pcolormesh.set_array(solution[j, :, :].ravel())
  plt.suptitle(f"{int(t_cp[j]//60)//60}:{(int(t_cp[j]//60)%60) : 03d}")

  return pcolormesh


anim = anm.FuncAnimation(fig,
                         func=animation,
                         frames=len(t_cp),
                         interval=200,
                         blit=False
                         )

plt.rc('animation', html='jshtml')
anim.save('anim.gif',fps=1)
plt.show()
plt.close()
