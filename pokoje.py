import matplotlib.pyplot as plt
import numpy as np

N=np.zeros((72,72))

for x in range (72):
    for y in range (72):
        if x<=20 and y<=23:
            N[x,y]=-2
        elif x>=36 and y<=23:
            N[x,y]=-3
        elif (x<=20 and y>=26) or (x<=25 and y>=41):
            N[x,y]=-4
        elif (x>=28 and y>=41) or (x>=46 and y>=26):
            N[x,y]=-5
        else:
            N[x,y]=-1

#ściany zewnętrzne
N[:,0]=0
N[:,71]=0
N[0,:]=0
N[71,:]=0

#ściany wewnętrzne

N[0:22,24]=0
N[0:22,25]=0

N[20,0:15]=0
N[21,0:15]=0

N[35,0:15]=0
N[36,0:15]=0

N[35,23]=0
N[36,23]=0

N[35:71,24]=0
N[35:71,25]=0

N[20:46,39]=0
N[20:46,40]=0

N[26,40:]=0
N[27,40:]=0

N[20,23:27]=0
N[21,23:27]=0

N[20,35:40]=0
N[21,35:40]=0

#okna
N[8:19,71]=1
N[35:44,71]=1

N[71,44:64]=1
N[71,7:18]=1




plt.imshow(N,origin='lower')
plt.title("Podział na pokoje")
plt.show()