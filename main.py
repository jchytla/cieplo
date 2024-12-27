import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib as mpl
from pandas.core.common import flatten
import gigabela as gb
import dane
from pogoda_interpolacja import temperatury_W

hx=0.1
liczba_dni=1/24
Tmax=60*60*24*liczba_dni
ht=1
X=np.arange(0,7.2,hx)
N=len(X)
T=np.arange(0,Tmax+ht, ht)
k=len(T)

X,Y=np.meshgrid(X,X)

zuzycie=[0]*6
srednie_temperatury=[0]*6

plt.plot(temperatury_W)
plt.show()

D2=[]
B=[0]*len(X)+[1,-2,1]+[0]*(len(X))
for i in range (len(X)):
  D2.append(B[len(X)-i+1:2*len(X)-i+1])
D2=np.asarray(D2)
I=np.identity(N)
L=np.kron(I,D2)+np.kron(D2,I)


def do_sciany_i_okna(U,t):
  for i in gb.Indeksy_scian_lewo:
    U[t,i]=U[t-1,i+1]
  for i in gb.Indeksy_scian_prawo:
    U[t,i]=U[t-1,i-1]
  for i in gb.Indeksy_scian_dol:
    U[t,i]=U[t-1,i+N]
  for i in gb.Indeksy_scian_gora:
    U[t,i]=U[t-1,i-N]
  for i in gb.Indeksy_okien:
    U[t,i]=srednie_temperatury[0]
  return 0

def aktualizuj_srednie_temperatury(srednie_temperatury,U,t):
  srednie_temperatury[0]=temperatury_W[t]

  srednie_temperatury[1]=sum([U[t-1,i] for i in gb.Indeksy_pokoj_1])/len(gb.Indeksy_pokoj_1)
  srednie_temperatury[2]=sum([U[t-1,i] for i in gb.Indeksy_pokoj_2])/len(gb.Indeksy_pokoj_2)
  srednie_temperatury[3]=sum([U[t-1,i] for i in gb.Indeksy_pokoj_3])/len(gb.Indeksy_pokoj_3)
  srednie_temperatury[4]=sum([U[t-1,i] for i in gb.Indeksy_pokoj_4])/len(gb.Indeksy_pokoj_4)
  srednie_temperatury[5]=sum([U[t-1,i] for i in gb.Indeksy_pokoj_5])/len(gb.Indeksy_pokoj_5)
  return 0



U=np.zeros((k,N**2))


U[0][:]=280+15*np.exp(-(X-3.6)**2 - (Y-3.6)**2).flatten()

for t in range(1,k):
  print(t)
  U[t][:]=U[t-1][:]+dane.alpha*ht/hx**2*(np.matmul(L,U[t-1][:]))
  aktualizuj_srednie_temperatury(srednie_temperatury,U,t)
  do_sciany_i_okna(U,t)
  for grzejnik in dane.Grzejniki:
    grzejnik.grzej(U,t,ht,srednie_temperatury,zuzycie)
  #print(zuzycie)



#for i in range(60):

  #plt.pcolormesh(X,Y,np.reshape(U[i*600][:],(N,N)),vmin=-5+dane.K,vmax=35+dane.K,cmap='jet')
  #plt.colorbar(ticks=np.arange(-5+dane.K,36+dane.K,5), format=mticker.FixedFormatter(np.arange(-5,36,5)))

  #plt.xlabel("x")
  #plt.ylabel("y")
  #plt.title(f't={round(T[i*100],2)}')
  #plt.show()


