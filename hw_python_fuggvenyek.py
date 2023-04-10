""" 
1. Feladat - 3 pont

Készíts egy függvényt ami megtalál minden számot két tetszőleges érték között (pl 2000 és 3200 között) ami osztható 7-el, de nem osztható 5-el.
A bemeneti paraméterek keyword argument-ek legyenek (start, finish, oszthato, nem_oszthato)
A függvény gyűjtse ki egy listába a helyes számokat, melyet a végén kiír a képernyőre. 
Segítség: használd a range függvény-t és az append-et """

result_list: list = []

def find_numbers(start: int, finish: int, oszthato: int, nem_oszthato: int) :
    for i in range(start, finish+1):
        if i % oszthato == 0 and i % nem_oszthato != 0 :
            result_list.append(i)
        
find_numbers(10, 100, 7, 5)
print(result_list)


""" 
2. Feladat - 2 pont
Adott az alábbi lista (bemenet)
['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
Készíts egy függvényt ami megszámolja ebben a tömbben a Pistákat és az eredményt return-öli, amit a végén megjeleníthetsz print-el. """

# első megoldás:

nevek: list=['Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László', 'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista']
darab = 0

def szamol(keres, nevek):
    global darab
    for nev in nevek:
        if nev == keres:
            darab = darab + 1
    return darab

szamol('Pista', nevek)
print(darab)

# másik megoldás:

def szamol2(mit, miben):
    darab = miben.count(mit)
    return darab

print(szamol2('Pista', nevek))


"""
3. Feladat - 2 pont
Kérj be a felhasználótól egy számot az input függvény segítségével. Ez után próbáld meg a számot int függvény segítségével számmá alakítani. Sikeres konvertálás esetén végül készíts egy ciklust ami annyiszor fut le amekkora számot beírt a felhasználó, és annyiszor írja ki a képernyőre hogy Helló, de a sorokat is számozza (1től)!
pl.:
> input: 4
Helló!
Helló!
Helló!
Helló!
A függvény itt a print_hello(count) legyen, amely a kiírást végzi el, illetve a convert_to_number(text) ami egy számot ad vissza. """

count = 0
print('Mondj egy számot!')
text = input()
print(f'a megadott adat: {text}')

def convert_to_number(text):
    global count
    count = int(text)
    return count

convert_to_number(text)

def print_hello(count):
        c =0
        while c < count:
            c = c + 1
            print(f'{c} helló!')

print_hello(count)


""" 
4. Feladat - 3 pont
Használd az előző feladatban megírt convert_to_number fgv-t. A bekért szám itt most egy kör sugara legyen, a program pedig számolja ki a kör sugarából a kör területét és kerületét. 
A számításhoz használd ezeket a képleteket: https://www.calculat.org/hu/terulet-kerulet/kor.html
A kettő darab függvény itt a kör területének és kerületének a kiszámítására legyen elkészítve, melyben mindkét esetben a függvény az eredményt ne kiírja, hanem return-ölje, amit ezután te kiírhatsz a képernyőre.  """

import math 

def kerulet(count):
    kerulet = round(2*count*math.pi, 2)
    return kerulet

def terulet(count):
    terulet = round(pow(count,2)*math.pi, 2)
    return terulet

print(kerulet(count))
print(terulet(count))


""" 
5. Feladat - 5 pont
Adott az alábbi lista:
['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']
Készíts függvényt ami a neveket abc sorrendbe rendezi (sorted függvénnyel) majd a csoportot két részre osztja (megfelezi) és kiírja a képernyőre a két csoportot külön. Például így:
1. csoport:
Gaál András
Gaál Bernadett
Kovács Tamás
Kucsera Bálint
Ledán-Munteán Szabolcs
Lukács Dániel
2. csoport
Magyar Eszter
Mészáros Melinda
Németh Diána
Szamosi Judit
Telek Éva
Tóth Sára
Bővítsd a függvényt arra az esetre ha a nevek száma páratlan!
A függvénynek ne legyen visszatérési értéke, csak végezze el a kiírást. """

input_list: list=['Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter', 'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs', 'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás']

def grouping(list):
    count = len(list)/2
    if count % 2 == 0:
        t = int(count)
        sorted_list=sorted(list)
        group1 = sorted_list[:t]
        group2 = sorted_list[t:]
        print(f'1. csoport - {t} fő:')
        for item in group1:
            print(item)
        print(f'2. csoport - {t} fő:')
        for item in group2:
            print(item)
    else:
        t = int(count)+1    
        sorted_list=sorted(list)
        group1 = sorted_list[:t]
        group2 = sorted_list[t:]
        print(f'1. csoport - {t} fő:')
        for item in group1:
            print(item)
        print(f'2. csoport - {t-1} fő:')
        for item in group2:
            print(item)
grouping(input_list)

