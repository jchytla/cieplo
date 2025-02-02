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
print(k)
X,Y=np.meshgrid(X,X)

temp=read_csv("temperatury_rovaniemi_okna.csv", delimiter=",",header=None)
temp=temp.to_numpy()
temp=temp.reshape(k,6)

plt.plot(temp[1:,0],label="na dworze")
plt.plot(temp[1:,1],label="na korytarzu")
plt.plot(temp[1:,2],label="w łazience")
plt.plot(temp[1:,3],label="w małej sypialni")
plt.plot(temp[1:,4],label="w dużej sypialni")
plt.plot(temp[1:,5],label="w salonie")
plt.yticks(np.arange(258.15,305,5),labels=np.arange(-15,32,5))
plt.xticks(np.arange(0,60*24,60),labels=np.arange(0,24,1))
plt.xlabel("godzina")
plt.ylabel("temperatura (°C)")
plt.title("Temperatury dla grzejników nie przy oknach dla Rovaniemi")
plt.legend()
plt.show()


zuzycie=read_csv("zuzycie_rovaniemi_okna.csv", delimiter=",",header=None)
zuzycie=zuzycie.to_numpy()
zuzycie=zuzycie.reshape(len(T),6)
zuzycie=zuzycie[::M,:]



#plt.plot(zuzycie[1:,0],label="na korytarzu")
#plt.plot(zuzycie[1:,1],label="w łazience")
plt.plot(zuzycie[1:,2],label="w małej sypialni")
plt.plot(zuzycie[1:,3],label="w dużej sypialni")
plt.plot(zuzycie[1:,4],label="w salonie (mały grzejnik)")
plt.plot(zuzycie[1:,5],label="w salonie (duży grzejnik)")
plt.yticks(np.arange(0,2000005,500000), labels=np.arange(0,2005,500))
plt.xticks(np.arange(0,60*24,60),labels=np.arange(0,24,1))
plt.xlabel("godzina")
plt.ylabel("zużyta mocy (kW)")
plt.title("Zużyta moc dla grzejników nie przy oknach dla Rovaniemi")
plt.legend()
plt.show()



plt.plot(zuzycie[1:,0],label="na korytarzu")
plt.yticks(np.arange(0,120005,20000), labels=np.arange(0,125,20))
plt.xticks(np.arange(0,60*24,60),labels=np.arange(0,24,1))
plt.xlabel("godzina")
plt.ylabel("zużyta mocy (kW)")
plt.title("Zużyta moc dla grzejników nie przy oknach dla Rovaniemi")
plt.legend()
plt.show()


plt.plot(zuzycie[1:,0],label="na korytarzu")
plt.plot(zuzycie[1:,1],label="w łazience")

plt.yticks(np.arange(0,1205,400),labels=[0,0.4,0.8,1.2])
plt.xticks(np.arange(0,60*24,60),labels=np.arange(0,24,1))
plt.xlabel("godzina")
plt.ylabel("zużyta mocy (kW)")
plt.title("Zużyta moc dla grzejników nie przy oknach dla Rovaniemi")
plt.legend()
plt.show()




