import matplotlib.pyplot as plt
import numpy as np

N=np.zeros((72,72))

#ściany zewnętrzne
N[:,0]=1
N[:,71]=2
N[0,:]=3
N[71,:]=4

N[0:22,24]=2
N[0:22,25]=1

N[20,0:15]=4
N[21,0:15]=3

N[35,0:15]=4
N[36,0:15]=3

N[35:71,24]=2
N[35:71,25]=1

N[35,23:25]=4
N[36,23:24]=3

N[20:46,39]=2
N[20:46,40]=1

N[26,40:]=4
N[27,40:]=3

N[20,23:27]=4
N[21,23:27]=3

N[20,35:40]=4
N[21,35:40]=3


#okna
N[8:19,71]=5
N[35:44,71]=5


N[71,44:64]=5
N[71,7:18]=5



for i in range (72):
    for j in range (72):
        if N[i,j]==0:
            N[i,j]=np.nan

plt.imshow(N,origin='lower')
plt.title("Podział ścian")
plt.show()