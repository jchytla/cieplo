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

zuzycie=read_csv("csvki/zuzycie_wroclaw_bezzmiany.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("wro1",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_bodo_bezzmiany.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("bodo1",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_rovaniemi_bezzmiany.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("ro13",round(sum(zuzycie[-1,:])/1000,3))


zuzycie=read_csv("csvki/zuzycie_wroclaw_okna.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("wro3",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_bodo_okna.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("bodo3",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_rovaniemi_okna.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("rov3",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_wroclaw_zmiana.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("wro2",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_bodo_zmiana.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("bodo2",round(sum(zuzycie[-1,:])/1000,3))

zuzycie=read_csv("csvki/zuzycie_rovaniemi_zmiana.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]
print("rov2",round(sum(zuzycie[-1,:])/1000,3))







