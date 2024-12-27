alpha=19/10000

p=1.225
Temperatury_co_godzine=0
Temperatury_graniczne_grzejnikow=0
c=1005
K=273.15
progi_temperatur=[6+K,12+K,15+K,18+K,22+K,25+K]

#temperatury zapisane z pogoda.py
temperatures_R=[1.12, 0.8, 0.89, 1.13, 1.73, 2.16, 1.78, 1.5, 1.01, -0.75, -2.38, -2.76, -1.86, -1.15, -0.6, -0.34, -0.17, 0.14, 0.05, -0.12, -1.36, -0.94, -1.43, -2, -6.52, -6.28, -4.27, -3.63, -4.81, -2.74, -4.78, -7.67, -11.98, -11.14, -8.09, -5.93, -4.81, -6.11, -7.45, -8.18]
temperatures_W=[-1.31, -0.38, 0.49, 2.27, 4.83, 1.97, 1.18, 1.06, 0.95, 0.82, 0.72, 2.68, 5.4, 2.43, 1.69, 1.61, 1.57, 1.37, 1.09, 3, 5.3, 2.34, 1.46, 1.91, 3.15, 3.62, 3.94, 4.39, 7.61, 6.1, 6.36, 5.89, 5.16, 4.28, 3.55, 5.37, 7.48, 8.38, 6.78, 5.68]


rozmiary_pokojow=[661,445,790,1043,1665]
rozmiar_mieszkania=4604

potrzebna_energia_na_pokoj=[i/100*2.5*40*1.2 for i in rozmiary_pokojow]
#print(potrzebna_energia_na_pokoj)

moce_grzejnikow=[800,550,1000,1300,600,1500]

pokoje_grzejnikow=[1,2,3,4,5,5]




Indeksy_grzejnikow=[0]*6

#grzejnik [25:32,37]
Indeksy_grzejnikow[0]=[x*72+37 for x in range(25,32)]

#grzejnik[2,12:17]
Indeksy_grzejnikow[1]=[2*72+y for y in range(12,17)]

#grzejnik[69,8:17]
Indeksy_grzejnikow[2]=[69*72+y for y in range(8,17)]


#grzejnik[9:18,69]
Indeksy_grzejnikow[3]=[x*72+69 for x in range(9,18)]

#grzejnik[36:43,69]
Indeksy_grzejnikow[4]=[x*72+69 for x in range(36,43)]

#grzejnik[69,45:63]
Indeksy_grzejnikow[5]=[69*72+y for y in range(45,63)]


rozmiary_grzejnikow=[len(Indeksy_grzejnikow[i])/100 for i in range(6)]

wartosc_grzewcza=[0]*6
for i in range(6):
    wartosc_grzewcza[i]=moce_grzejnikow[i]/(p*c*rozmiary_grzejnikow[i])



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

    def grzej(self,U,t,ht,srednie_temperatury,zuzycie):
        if(self.temperatura_aktywacji>=srednie_temperatury[self.numer_pokoju]):
            for i in self.indeksy:
                U[t][i]+=ht*self.wartosc_grzewcza
            zuzycie[self.nr_grzejnika]+=self.wartosc_grzewcza*self.rozmiar

Grzejniki=[GRZEJNIK(i,Indeksy_grzejnikow[i],pokoje_grzejnikow[i],rozmiary_grzejnikow[i],wartosc_grzewcza[i] )for i in range(6)]
Grzejniki[1].zmien_poziom(4)
