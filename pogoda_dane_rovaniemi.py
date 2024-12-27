import requests
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from math import floor

# Klucz API z OpenWeatherMap
api_key = "b70f2d076abc2f0572fc142cbe0f34f2"

# Parametry zapytania
city = "Rovaniemi"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# Wysyłamy zapytanie do API
response = requests.get(url)
data = response.json()

# Sprawdzamy, czy odpowiedź jest poprawna
if response.status_code == 200:
    # Oczekiwane dane: 5-dniowa prognoza, co 3 godziny
    times = [datetime.utcfromtimestamp(item['dt']) for item in data['list']]
    temperatures = [item['main']['temp'] for item in data['list']]

    # Przygotowujemy dane co godzinę
    hours = [time.hour for time in times]

    mid_temperatures=[0]*9
    for t in range (8):
        mid_temperatures[t]=sum([temperatures[8*i+t] for i in range(5)])/5
    mid_temperatures[8]=mid_temperatures[0]
    hours=hours[:8]

    plt.plot(hours, temperatures[0:8], marker='.', color=(0,0.2,1), label='Dzień 1')
    plt.plot(hours, temperatures[8:16], marker='.', color=(0,0.4,1), label='Dzień 2')
    plt.plot(hours, temperatures[16:24], marker='.', color=(0,0.6,1), label='Dzień 3')
    plt.plot(hours, temperatures[24:32], marker='.', color=(0,0.8,1), label='Dzień 4')
    plt.plot(hours, temperatures[32:40], marker='.', color=(0,1,1), label='Dzień 5')
    plt.plot(hours, mid_temperatures[0:8], marker='o', color='red', label='Średnia z 5 dni')
    plt.xlabel('Godzina')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura powietrza w dniach 27.12-31.12 w Rovaniemi')
    plt.xticks(range(0,24,3))
    plt.grid()
    plt.legend()
    plt.show()
    print(temperatures)
    print(hours)


else:
    print(f"Błąd pobierania danych: {response.status_code}")
