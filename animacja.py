import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import matplotlib.animation as anm
import matplotlib.gridspec as gridspec
from pandas.core.common import flatten
import dane
from main import U,T,X,Y,N,k
U=U.reshape(k,N,N)
solution = U[0::60*10,:, :]

t_cp = T[::60*10]

fig=plt.figure()



plt.xlim((np.min(X), np.max(X)))
plt.ylim((np.min(Y), np.max(Y)))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ciepło w czasie")


pcolormesh = plt.pcolormesh(X,Y,solution[0,:,:],vmin=-5+dane.K,vmax=35+dane.K,cmap='jet')

plt.colorbar(ticks=np.arange(-5+dane.K,36+dane.K,5), format=mticker.FixedFormatter(np.arange(-5,36,5)))


def animation(j):
  pcolormesh.set_array(solution[j, :, :].ravel())

  return pcolormesh


anim = anm.FuncAnimation(fig,
                         func=animation,
                         frames=len(t_cp),
                         interval=500,
                         blit=False
                         )

plt.rc('animation', html='jshtml')
anim.save('anim.gif',fps=1)
plt.show()
plt.close()
