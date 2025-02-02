import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib as mpl
from pandas.core.common import flatten
import gigabela as gb
import dane


hx=0.1
liczba_dni=1
Tmax=60*60*24*liczba_dni
ht=0.1
X=np.arange(0,7.2,hx)
N=len(X)
T=np.arange(0,Tmax+ht, ht)
k=len(T)
M=600

X,Y=np.meshgrid(X,X)

D2=[]
B=[0]*len(X)+[1,-2,1]+[0]*(len(X))
for i in range (len(X)):
  D2.append(B[len(X)-i+1:2*len(X)-i+1])
D2=np.asarray(D2)
I=np.identity(N)
L=np.kron(I,D2)+np.kron(D2,I)


def do_sciany_i_okna(U,t):
  for i in gb.Indeksy_scian_lewo:
    U[t%M,i]=U[(t-1)%M,i+1]
  for i in gb.Indeksy_scian_prawo:
    U[t%M,i]=U[(t-1)%M,i-1]
  for i in gb.Indeksy_scian_dol:
    U[t%M,i]=U[(t-1)%M,i+N]
  for i in gb.Indeksy_scian_gora:
    U[t%M,i]=U[(t-1)%M,i-N]
  for i in gb.Indeksy_okien:
    U[t%M,i]=srednie_temperatury[0]
  return 0

def aktualizuj_srednie_temperatury(srednie_temperatury,U,t):
  srednie_temperatury[0]=temperatury_w_miescie[t-1]

  srednie_temperatury[1]=float(sum([U[(t-1)%M,i] for i in gb.Indeksy_pokoj_1])/len(gb.Indeksy_pokoj_1))
  srednie_temperatury[2]=float(sum([U[(t-1)%M,i] for i in gb.Indeksy_pokoj_2])/len(gb.Indeksy_pokoj_2))
  srednie_temperatury[3]=float(sum([U[(t-1)%M,i] for i in gb.Indeksy_pokoj_3])/len(gb.Indeksy_pokoj_3))
  srednie_temperatury[4]=float(sum([U[(t-1)%M,i] for i in gb.Indeksy_pokoj_4])/len(gb.Indeksy_pokoj_4))
  srednie_temperatury[5]=float(sum([U[(t-1)%M,i] for i in gb.Indeksy_pokoj_5])/len(gb.Indeksy_pokoj_5))
  return 0



#----------------------------------------------------------------------------------------------------------
from pogoda_interpolacja import temperatury_W as temperatury_w_miescie
zuzycie=np.zeros((k,6))
srednie_temperatury=[0]*6
temp_w_pokojach=np.zeros((k//M+1,6))


U=np.zeros((M,N**2))
U_min=np.zeros((k//M+1,N**2))


U[0][:]=280+8*np.exp(-(X-3.6)**2 - (Y-3.6)**2).flatten()
U_min[0][:]=U[0][:]
for t in range(1,k):
  U[t%M][:]=U[(t-1)%M][:]+dane.alpha*ht/hx**2*(np.matmul(L,U[(t-1)%M][:]))
  aktualizuj_srednie_temperatury(srednie_temperatury,U,t)
  do_sciany_i_okna(U,t)
  
  for grzejnik in dane.Grzejniki:
    grzejnik.grzej(U,t,ht,srednie_temperatury,zuzycie,M)
  if(t%M==0):
    U_min[t//M][:]=U[0][:]
    temp_w_pokojach[t//M,:]=srednie_temperatury[:]
    print(t)
    #print(srednie_temperatury)
print(U.shape)
np.savetxt("macierze_wroclaw_okna.csv",U_min,delimiter=",")
np.savetxt("zuzycie_wroclaw_okna.csv",zuzycie,delimiter=",")
np.savetxt("temperatury_wroclaw_okna.csv",temp_w_pokojach,delimiter=",")

#---------------------------------------------------------------

from pogoda_interpolacja import temperatury_B as temperatury_w_miescie
zuzycie=np.zeros((k,6))
srednie_temperatury=[0]*6
temp_w_pokojach=np.zeros((k//M+1,6))


U=np.zeros((M,N**2))
U_min=np.zeros((k//M+1,N**2))


U[0][:]=280+8*np.exp(-(X-3.6)**2 - (Y-3.6)**2).flatten()
U_min[0][:]=U[0][:]
for t in range(1,k):
  U[t%M][:]=U[(t-1)%M][:]+dane.alpha*ht/hx**2*(np.matmul(L,U[(t-1)%M][:]))
  aktualizuj_srednie_temperatury(srednie_temperatury,U,t)
  do_sciany_i_okna(U,t)
  
  for grzejnik in dane.Grzejniki:
    grzejnik.grzej(U,t,ht,srednie_temperatury,zuzycie,M)
  if(t%M==0):
    U_min[t//M][:]=U[0][:]
    temp_w_pokojach[t//M,:]=srednie_temperatury[:]
    print(t)
    #print(srednie_temperatury)
print(U.shape)
np.savetxt("macierze_bodo_okna.csv",U_min,delimiter=",")
np.savetxt("zuzycie_bodo_okna.csv",zuzycie,delimiter=",")
np.savetxt("temperatury_bodo_okna.csv",temp_w_pokojach,delimiter=",")



#----------------------------------------------------------------------------------------------------------
from pogoda_interpolacja import temperatury_R as temperatury_w_miescie
zuzycie=np.zeros((k,6))
srednie_temperatury=[0]*6
temp_w_pokojach=np.zeros((k//M+1,6))


U=np.zeros((M,N**2))
U_min=np.zeros((k//M+1,N**2))


U[0][:]=280+8*np.exp(-(X-3.6)**2 - (Y-3.6)**2).flatten()
U_min[0][:]=U[0][:]
for t in range(1,k):
  U[t%M][:]=U[(t-1)%M][:]+dane.alpha*ht/hx**2*(np.matmul(L,U[(t-1)%M][:]))
  aktualizuj_srednie_temperatury(srednie_temperatury,U,t)
  do_sciany_i_okna(U,t)
  
  for grzejnik in dane.Grzejniki:
    grzejnik.grzej(U,t,ht,srednie_temperatury,zuzycie,M)
  if(t%M==0):
    U_min[t//M][:]=U[0][:]
    temp_w_pokojach[t//M,:]=srednie_temperatury[:]
    print(t)
    #print(srednie_temperatury)
print(U.shape)
np.savetxt("macierze_rovaniemi_okna.csv",U_min,delimiter=",")
np.savetxt("zuzycie_rovaniemi_okna.csv",zuzycie,delimiter=",")
np.savetxt("temperatury_rovaniemi_okna.csv",temp_w_pokojach,delimiter=",")