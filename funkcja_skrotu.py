"""
Napisz program który pobiera od użytkownika długość skrótu k oraz wiadomość
a następnie tworzy tabelę o k kolumnach i odpowiednio wielu wierszach po czym dodaje liczby
otrzymane w poszczególnych kolumnach i otrzymaną sumę przekształca na litery alfabetu - male lub wielkie
wedle uznania autora
"""
import math


string = input("Podaj wiadomosc (bez polskich znakow): ")
k = int(input("Podaj dlugosc skrotu: "))


def split(word):  # metoda dzieląca stringa na pojedyncze znaki
    return [char for char in word]


splitted_string = list(split(string)) # dzielenie stringa na listę znaków


tab = [[0 for col in range(k)] for row in range(int(math.ceil(len(string)/k)))] # tworzenie tabeli


for i, c in enumerate(string): #wpisywanie liter do tabeli
    row = int(i / k)
    col = i % k
    tab[row][col] = ord(c) # ord() - zamiana na kod ascii


for col in zip(*tab):
    if (sum(col) % (ord('Z')-ord('A')+1)) < 32 or (sum(col)%127) == 0:
        print(chr((sum(col) % (ord('Z')-ord('A')+1)) + 65))
    else:
        print(chr(sum(col) % (ord('Z')-ord('A')+1)))
