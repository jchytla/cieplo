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
#1=lewa ściana pokoju
#2=prawa
#3=dolna
#4=gorna
#5=okno
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


Indeksy=np.zeros(72**2)


for i in range (72):
    for j in range (72):
        Indeksy[i*72+j]=N[i,j]

Indeksy_scian_lewo=[i for i in range(72**2) if Indeksy[i]==1]
Indeksy_scian_prawo=[i for i in range(72**2) if Indeksy[i]==2]
Indeksy_scian_dol=[i for i in range(72**2) if Indeksy[i]==3]
Indeksy_scian_gora=[i for i in range(72**2) if Indeksy[i]==4]
Indeksy_okien=[i for i in range(72**2) if Indeksy[i]==5]

Indeksy_pokoj_1=[i for i in range(72**2) if Indeksy[i]==-1]
Indeksy_pokoj_2=[i for i in range(72**2) if Indeksy[i]==-2]
Indeksy_pokoj_3=[i for i in range(72**2) if Indeksy[i]==-3]
Indeksy_pokoj_4=[i for i in range(72**2) if Indeksy[i]==-4]
Indeksy_pokoj_5=[i for i in range(72**2) if Indeksy[i]==-5]
print(len(Indeksy_pokoj_1))
print(len(Indeksy_pokoj_2))
print(len(Indeksy_pokoj_3))
print(len(Indeksy_pokoj_4))
print(len(Indeksy_pokoj_5))
print(len(Indeksy_pokoj_5)+len(Indeksy_pokoj_4)+len(Indeksy_pokoj_3)+len(Indeksy_pokoj_2)+len(Indeksy_pokoj_1))


plt.imshow(N,origin='lower')
plt.title("Układ grzejników w mieszkaniu: opcja 1")
plt.show()