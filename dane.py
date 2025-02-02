alpha=0.025

p=1.225
Temperatury_co_godzine=0
Temperatury_graniczne_grzejnikow=0
c=1005
K=273.15
progi_temperatur=[6+K,12+K,15+K,19+K,22+K,25+K]
podoknami=False

#temperatury zapisane z pogoda.py
temperatures_R=[-17.69, -20.17, -20.49, -18.56, -14.71, -14.27, -11.61, -10.56, -10.04, -10.34, -10.24, -9.92, -9.63, -11.38, -16.44, -19.25, -20.79, -21.83, -21.57, -15.96, -16.48, -17.7, -15.06, -13.94, -13.17, -14.62, -17.06, -16.21, -10.15, -7.87, -6.24, -4.4, -3.4, -3.4, -0.92, 0.32, 0.2, 0.3, 0.58, 0.55]
temperatures_B=[-2.89, -3.46, -3.51, -3.2, -3.43, -4.14, -4.46, -4.7, -4.97, -5.5, -6.26, -6.91, -7.08, -7.27, -7.22, -6.96, -6.66, -6.34, -6.34, -6.14, -5.41, -5.14, -4.86, -4.29, -4.15, -3.94, -4.01, -4.14, -3.97, -3.94, -3.67, -2.94, -3.28, -5.03, -4.42, -4.64, -3.15, -2.5, -1.96, -0.99]
temperatures_W=[1.04, 0.51, 0.84, 2.51, 4.16, 2.98, 1.52, 0.95, 0.69, 0.47, 0.08, 2.5, 5.49, 3.34, 1.42, 0.88, 1.53, 1.35, 1.98, 4.46, 6.59, 5.04, 5.03, 3.87, 3.56, 1.44, 1.53, 4.27, 5.87, 4.54, 2.69, 3.34, 6.03, 6.76, 7.9, 9.11, 10.33, 8.7, 6.55, 7]

rozmiary_pokojow=[661,445,790,1043,1665]
rozmiar_mieszkania=4604

#potrzebna_energia_na_pokoj=[i/100*2.5*40*1.2 for i in rozmiary_pokojow]
#print(potrzebna_energia_na_pokoj)

moce_grzejnikow=[600,500,5000,5000,4000,10000]

pokoje_grzejnikow=[1,2,3,4,5,5]




Indeksy_grzejnikow=[0]*6

#grzejnik [25:32,37]
Indeksy_grzejnikow[0]=[x*72+37 for x in range(25,32)]

#grzejnik[2,12:17]
Indeksy_grzejnikow[1]=[2*72+y for y in range(12,17)]


if(podoknami==True):
    #grzejnik[69,8:17]
    Indeksy_grzejnikow[2]=[69*72+y for y in range(8,17)]


    #grzejnik[9:18,69]
    Indeksy_grzejnikow[3]=[x*72+69 for x in range(9,18)]

    #grzejnik[36:43,69]
    Indeksy_grzejnikow[4]=[x*72+69 for x in range(36,43)]

    #grzejnik[69,45:63]
    Indeksy_grzejnikow[5]=[69*72+y for y in range(45,63)]
else:
    #grzejnik[38,3:12]
    Indeksy_grzejnikow[2]=[38*72+y for y in range(3,12)]

    #grzejnik[2,45:54]
    Indeksy_grzejnikow[3]=[2*72+y for y in range(45,54)]

    #grzejnik[61:68,27]
    Indeksy_grzejnikow[4]=[x*72+27 for x in range(61,68)]

    #grzejnik[50:68,69]
    Indeksy_grzejnikow[5]=[x*72+69 for x in range(50,68)]





rozmiary_grzejnikow=[len(Indeksy_grzejnikow[i])/100 for i in range(6)]

wartosc_grzewcza=[0]*6
for i in range(6):
    wartosc_grzewcza[i]=moce_grzejnikow[i]/(p*c*rozmiary_grzejnikow[i])
#print(wartosc_grzewcza)



class GRZEJNIK:
    def __init__(self,nr_grzejnika, indeksy, numer_pokoju, rozmiar, wartosc_grzewcza, poziom=3):

        self.nr_grzejnika=nr_grzejnika
        self.indeksy=indeksy
        self.numer_pokoju=numer_pokoju
        self.rozmiar=rozmiar
        self.wartosc_grzewcza=wartosc_grzewcza
        self.poziom=poziom
        self.temperatura_aktywacji=progi_temperatur[poziom]

    def zmien_poziom(self, nowy_poziom):
        self.poziom=nowy_poziom
        self.temperatura_aktywacji=progi_temperatur[nowy_poziom]

    def grzej(self,U,t,ht,srednie_temperatury,zuzycie,M):
        zuzycie[t][self.nr_grzejnika]=zuzycie[t-1][self.nr_grzejnika]
        if(self.temperatura_aktywacji>=srednie_temperatury[self.numer_pokoju]):
            for i in self.indeksy:
                U[t%M][i]+=ht*self.wartosc_grzewcza
            zuzycie[t][self.nr_grzejnika]+=self.wartosc_grzewcza*self.rozmiar

Grzejniki=[GRZEJNIK(i,Indeksy_grzejnikow[i],pokoje_grzejnikow[i],rozmiary_grzejnikow[i],wartosc_grzewcza[i] )for i in range(6)]
