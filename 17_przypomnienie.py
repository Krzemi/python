# liczba = input('Podaj liczbę: ')
# liczba = int(liczba)

# for i in range(1, liczba + 1):
#     if liczba % i == 0:
#         print(i)

import time

# def wyszukaj_dzielniki(liczba):
#     wynik = []
#     for i in range(1, liczba + 1):
#         if liczba % i == 0:
#             wynik.append(i)
#     return wynik

def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return True

start = time.time()
maksimum = 100
for liczba in range(1, maksimum + 1):
    if czy_pierwsza(liczba):
        print(liczba)

print(time.time() - start)