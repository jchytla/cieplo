
import matplotlib.pyplot as plt
from dane import temperatures_W as temp_W
from dane import temperatures_R as temp_R
from dane import K
from math import floor


hours=range(0,24,3)
mid_temp_W=[0]*8
for t in range (8):
    mid_temp_W[t]=sum([temp_W[8*i+t] for i in range(5)])/5



temperatury_W=[0]*24*60*60
mid_temp_W+=[mid_temp_W[0]]

for t in range(24*60*60):
    temperatury_W[t]=mid_temp_W[floor(t/10800)]*(10800-t%10800)/10800 + mid_temp_W[floor(t/10800)+1]*(t%10800)/10800 


hours=range(0,24,3)
mid_temp_R=[0]*8
for t in range (8):
    mid_temp_R[t]=sum([temp_R[8*i+t] for i in range(5)])/5


temperatury_R=[0]*24*60*60
mid_temp_R+=[mid_temp_R[0]]

for t in range(24*60*60):
    temperatury_R[t]=mid_temp_R[floor(t/10800)]*(10800-t%10800)/10800 + mid_temp_R[floor(t/10800)+1]*(t%10800)/10800 


if __name__=="__main__":
    plt.plot(hours, temp_W[0:8], marker='.', color=(0,0.2,1), label='Dzień 1')
    plt.plot(hours, temp_W[8:16], marker='.', color=(0,0.4,1), label='Dzień 2')
    plt.plot(hours, temp_W[16:24], marker='.', color=(0,0.6,1), label='Dzień 3')
    plt.plot(hours, temp_W[24:32], marker='.', color=(0,0.8,1), label='Dzień 4')
    plt.plot(hours, temp_W[32:40], marker='.', color=(0,1,1), label='Dzień 5')
    plt.plot(hours, mid_temp_W[:8], marker='o', color='red', label='Średnia z 5 dni')
    plt.xlabel('Godzina')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura powietrza w dniach 27.12-31.12 we Wrocławiu')
    plt.xticks(range(0,24,3))
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.plot(temperatury_W)
    plt.xlabel('Czas (s)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura powietrza w dniach 27.12-31.12 we Wrocławiu')
    plt.xticks(range(0,24*60*60,10800))
    plt.grid()
    plt.show()

    plt.plot(hours, temp_R[0:8], marker='.', color=(0,0.2,1), label='Dzień 1')
    plt.plot(hours, temp_R[8:16], marker='.', color=(0,0.4,1), label='Dzień 2')
    plt.plot(hours, temp_R[16:24], marker='.', color=(0,0.6,1), label='Dzień 3')
    plt.plot(hours, temp_R[24:32], marker='.', color=(0,0.8,1), label='Dzień 4')
    plt.plot(hours, temp_R[32:40], marker='.', color=(0,1,1), label='Dzień 5')
    plt.plot(hours, mid_temp_R[:8], marker='o', color='red', label='Średnia z 5 dni')
    plt.xlabel('Godzina')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura powietrza w dniach 27.12-31.12 w Rovaniemi')
    plt.xticks(range(0,24,3))
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.plot(temperatury_R)
    plt.xlabel('Czas (s)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura powietrza w dniach 27.12-31.12 w Rovaniemi')
    plt.xticks(range(0,24*60*60,10800))
    plt.grid()
    plt.show()



temperatury_W=[t+K for t in temperatury_W]
temperatury_R=[t+K for t in temperatury_R]