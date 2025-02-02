Witam
tu znajdziesz kod, za pomocą którego symulowałem i generowałem wykresy.
W dane.py znajdziesz stałe, klasę grzejników, zapisane temperatury
W gigabela.py znajdziesz dyskretyzację mieszkania.
W main.py znajdziesz główny kod który generuje, przy czym w tym momencie jest ustawiony na generowanie kodu do opcji grzejników poza oknami. Aby zmienić opcje grzejników należy zmienić w dane.py zmienną "podoknami" z False na True. Aby ustawić zmiany termostatu trzeba dodać w symulacji warunek który mówi, jeżeli jest odpowiedni czas, zmień poziom w każdym grzejniku.

W wykresy_macierze.py i wykresy_temp_i_zuz.py znajdziesz kod który obrabia rezulataty i wyrzuca jakieś wykresy. Aby otrzymać wykresy z innych symulacji niż tej, którą aktualnie analizuje trzeba mu zmienić csv i potencjalnie zakresy osi.
W plikach pogoda_dane_'nazwamiasta'.py jest kod uzyskany z pomocą chata GPT, który pozyskuje pogodę w danym mieście. Kolejno w pogoda_interpolacja przekształcamy te dane.
W pokoje.py, sciany.py, flat_1.py i flat_2.py są proste wykresiki obrazujące mieszkanie.
W animacja.py znajduje się kod, który z csv zaczynających się od macierze... jest w stanie generować animacje z klatkami co pół godziny. Nie ma ich w raporcie bo nie umiem ich wstawić, więc nawet ich nie generowałem, ale kod jest.
W folderze plots są wszelakie wykresy wygenerowane w trakcie symulacji, które użyłem (lub nie) w raporcie.
legenda wykresów:
pierwsza litera oznacza miasto,
liczba: 1 to grzejniki pod oknami i bez zmian termostatu, 2 to grzejniki pod oknami i zmiana termostatu, 3 to grzejniki poza oknami
kolejna litera: t oznacza wykres temperatur, z oznacza wykres zużycia energii, macierz oznacza wykres temoeratur w mieszkaniu o 0:30
dalej: dla temperatur mamy 24 czyli 24 godziny i 8 i 16 które obrazują zmiany temperatur przy zmienianiu termostatu o 8:00 i 16:00
dla zużycia mamy:
d czyli te grzejniki, które miały duże zużycie
s czyli średnie (tylko dla rovaniemi)
m czyli małe

Do tego oczywiście cała masa csv o strukturze "co jest w csv"_"miasto"_"która symulacja", gdzie:
-mamy temperatury średnie w pomieszczeniach co minutę, zużycie energii co 0.1s i macierze, czyli temperatury w każdym kwadracie co minutę
- zmiana i bez zmiany dotyczą zmiany i braku zmiany termostatu a okna dotyczy symulacji gdzie grzejniki NIE są pod oknami (tak wyszło, trudno)
edit może nie być csv bo wyglada na to że git nie chce ich przyjąć
