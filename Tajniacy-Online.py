print("Witaj w generatorze plansz do tajniaków!")
#import słów z pliku slowa.csv do katalogu
zpliku = []
import csv
with open('slowa.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        zpliku.append(row[0])
#przerzucenie do katalogu słów niepowtarzalnych
katalog = []
a = 0
while a < len (zpliku):
    if len(zpliku[a]) < 3:
        a = a + 1
    if zpliku[a] in katalog:
        a = a + 1
    else:
        katalog.append(zpliku[a])
        a = a + 1
# wybór wielkości planszy, enter = wymiary z gry planszowej
import random
print('katalog zawiera', len(katalog), 'niepowtarzalnych słów.')
bladplan = 1
while bladplan == 1:
    blad = 1
    while blad == 1:
        print ("Wciśnij enter dla standardowych parametrów, lub wpisz liczbę wierszy:")
        wejscie = input()
        if wejscie == '':
            ilwierszy = 5
            ilkolumn = 5
            l = [8, 9]
            agenci1 = random.choice(l)
            if agenci1 == 8:
                agenci2 = 9
                print("Rozpoczyna drużyna 2")
                Iruch = 2
            else:
                agenci2 = 8
                print("Rozpoczyna drużyna 1")
                Iruch = 1
            killers = 1
            blad = 0
        else:
            try:
                ilwierszy = int(wejscie)
                if ilwierszy < 1:
                    print("Musisz wpisać liczbę naturalną.")
                    blad = 1
                else:
                    blad = 0
            except:
                print ("Musisz wpisać liczbę naturalną.")
                blad = 1
    # jeśli nie wybrano wymiarów z gry planszowej, wybór ilości kolumn
    if wejscie != '':
        blad = 1
        while blad == 1:
            print("Wpisz liczbę kolumn:")
            wejscie = input ()
            try:
                ilkolumn = int(wejscie)
                if ilkolumn < 1:
                    print('musisz wpisać liczbę naturalną')
                else:
                    blad = 0
            except:
                print ('musisz wpisać liczbę naturalną')
                blad = 1
    if ilwierszy*ilkolumn > len(katalog):
        print ('wybrana plansza jest za duża, w katalogu nie ma wystarczającej ilości słów na tak dużą planszę, spróbuj jeszcze raz.')
    else:
        bladplan = 0
if wejscie != '':
    bladag = 1
    while bladag == 1:
        blad = 1
        while blad == 1:
            print("Wpisz liczbę agentów dla drużyny 1:")
            wejscie = input()
            try:
                agenci1 = int(wejscie)
                if agenci1 < 1:
                    print("Musisz wpisać liczbę naturalną.")
                    blad = 1
                else:
                    blad = 0
            except:
                print("Musisz wpisać liczbę naturalną.")
                blad = 1
        blad = 1
        while blad == 1:
            print("Wpisz liczbę agentów dla drużyny 2:")
            wejscie = input()
            try:
                agenci2 = int(wejscie)
                if agenci2 < 1:
                    print("Musisz wpisać liczbę naturalną.")
                    blad = 1
                else:
                    blad = 0
            except:
                print("Musisz wpisać liczbę naturalną.")
                blad = 1
        blad = 1
        while blad == 1:
            print("Wpisz liczbę zabójców:")
            wejscie = input()
            try:
                killers = int(wejscie)
                if killers < 1:
                    print("Musisz wpisać liczbę naturalną.")
                    blad = 1
                else:
                    blad = 0
            except:
                print("Musisz wpisać liczbę naturalną.")
                blad = 1
        if agenci1 + agenci2 + killers > ilkolumn*ilwierszy:
            print ('Ilość haseł do odgadnięcia i zabójców jest większa, niż ilość pól, wpisz mniejsze wartości')
        else:
            bladag = 0
#losowanie słów
slowa = []
while len(slowa) < ilwierszy * ilkolumn:
    a = random.choice(katalog)
    if a not in slowa:
        slowa.append(a)
# zmiana wszystkich słów na pisane wielkimi literami
s = 0
while s < len(slowa):
    slowa[s] = slowa[s].upper()
    s = s+ 1
# Tworzenie listy z długościami najdłuższego wyrazu w kolejnych kolumnach = szerokość kolejnych kolumn
k = 0  # numer kolumny
r = 0  # numer rzędu
lenKol = []
while k < ilkolumn:
    makss = 0  # maksymalna długość bieżąco sprawdzanej kolumny
    s = k  # numer bieżącego słowa
    r = 0 #numr rzędu
    while r < ilwierszy:
        if len(slowa[s]) > makss:
            makss = len(slowa[s])
            s = s + ilkolumn
        else:
            s = s + ilkolumn
        r = r + 1
    lenKol.append(makss)
    k = k + 1
#Rysowanie planszy
k = 0  # numer kolumny
r = 0  # numer rzędu
plik = open('plansza.txt', 'w')
try:
    if Iruch == 1:
        plik.write("Rozpoczyna drużyna 1\n")
    if Iruch == 2:
        plik.write("Rozpoczyna drużyna 2\n")
except:
    plik.write("Plansza nietypowa, nie wiadomo kto zaczyna\n")
while r < ilwierszy+1:
    k = 0
    s = r * ilkolumn
    rząd = []  # lista znaków bierząco rysowanego rzędu
    while k < ilkolumn:
        print("+", end="")
        rząd.append('+')
        lit = 0
        while lit < lenKol[k]:
            print("-", end="")
            rząd.append('-')
            lit = lit + 1
        k = k + 1
    print("+", end="")
    rząd.append('+')
    print()
    rząd.append("\n")
    dopliku = ''.join(rząd)
    plik.write(dopliku)
    rząd = []
    if r < ilwierszy:
        k = 0
        while k < ilkolumn:
            print("|", end="")
            rząd.append('|')
            print(slowa[s], end="")
            rząd.append(slowa[s])
            l = len(slowa[s])
            while l < lenKol[k]:
                print(" ", end="")
                rząd.append(' ')
                l = l + 1
            k = k + 1
            s = s + 1
        print("|")
        rząd.append('|')
    rząd.append('\n')
    dopliku = ''.join(rząd)
    plik.write(dopliku)
    r = r + 1
print ()
plik.close()
#losowanie słów - agentów i zabójców
cywile = slowa[:]
slowaAgenci1 = []
slowaAgenci2 = []
slowaKillers = []
while len(slowaAgenci1) < agenci1:
    a = random.choice(cywile)
    slowaAgenci1.append(a)
    cywile.remove(a)
while len(slowaAgenci2) < agenci2:
    a = random.choice(cywile)
    slowaAgenci2.append(a)
    cywile.remove(a)
while len(slowaKillers) < killers:
    a = random.choice(cywile)
    slowaKillers.append(a)
    cywile.remove(a)
plagenci1 = slowaAgenci1[:]
plagenci1.sort()
liniaagenci1 = ', '.join(plagenci1)
plagenci2 = slowaAgenci2[:]
plagenci2.sort()
liniaagenci2 = ', '.join(plagenci2)
plkillers = slowaKillers[:]
plkillers.sort()
liniakillers = ', '.join(plkillers)
plcywile = cywile[:]
plcywile.sort()
liniacywile = ', '.join(plcywile)
plik = open('kapitans.txt', 'w')
try:
    if Iruch == 1:
        plik.write("Rozpoczyna drużyna 1\n")
    if Iruch == 2:
        plik.write("Rozpoczyna drużyna 2\n")
except:
    plik.write("Plansza nietypowa, nie wiadomo kto zaczyna\n")
plik.write("Hasła dla zespołu 1: ")
plik.write(liniaagenci1)
plik.write('\n')
plik.write("Hasła dla zespołu 2: ")
plik.write(liniaagenci2)
plik.write('\n')
plik.write("Zabójcy: ")
plik.write(liniakillers)
plik.write('\n')
plik.write("Cywile: ")
plik.write(liniacywile)
plik.write('\n')
plik.write('Powodzenia!')
#wydruk wszystkich grup, pomijany
'''
print ("ilosć agentów drużyny 1:", agenci1, slowaAgenci1)
print ("ilosć agentów drużyny 2:", agenci2, slowaAgenci2)
print ("ilosć zabójców:", killers, slowaKillers)
print ("ilość cywilów:", len(cywile), cywile)'''