import matplotlib.pyplot as plt
import numpy as np

N=np.zeros((72,72))

for i in range (72):
    for j in range (72):
        if (i+j)%2==0:
            N[i][j]=0.1
#ściany zewnętrzne
N[:,0]=1
N[:,71]=1
N[0,:]=1
N[71,:]=1

#ściany wewnętrzne

N[0:22,24]=1
N[0:22,25]=1

N[20,0:15]=1
N[21,0:15]=1

N[35,0:15]=1
N[36,0:15]=1

N[35,23]=1
N[36,23]=1

N[35:71,24]=1
N[35:71,25]=1

N[20:46,39]=1
N[20:46,40]=1

N[26,40:]=1
N[27,40:]=1

N[20,23:27]=1
N[21,23:27]=1

N[20,35:40]=1
N[21,35:40]=1


#okna
N[8:19,71]=2
N[35:44,71]=2



N[71,44:64]=2
N[71,7:18]=2

#grzejniki
N[9:18,69]=1.6
#9
N[36:43,69]=1.6
#7
N[69,45:63]=1.6
#18 
N[69,8:17]=1.6
#9
N[2,12:17]=1.6
#5
N[25:32,37]=1.6
#7



plt.imshow(N,origin='lower')
plt.title("Układ grzejników w mieszkaniu: opcja 1")
plt.show()