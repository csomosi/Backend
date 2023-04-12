""" 1. Feladat - 5 pont
készíts egy programot ami egy 4x5ös mátrix minden elemét összegzi. pl: (az eredmény: 50) """

m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

def summarize_matrix(matrix):
    sumtotal = 0
    for item in matrix:
        sum = 0
        for inneritem in item:
            sum = sum + inneritem
        sumtotal = sumtotal + sum
    return sumtotal



print(summarize_matrix(m))


""" 2. Feladat - 5 pont
Készíts programot ami az alábbi autókat tartalmazó tömböt megvizsgálja és kiírja azoknak az autóknak a típusát amelyeknél az utasok száma túl nagy. Ehhez a passengerQty és a passengers property-ket kell felhasználnod.
pl kimenet:
a(z) Kia típusú autóban túl sok az utas
a(z) Opel típusú autóban túl sok az utas """

cars = [
    {"price": 1549,
     "passengerQty": 4,
     "currency": "EUR",
     "type": "Kia",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"]},
    {"price": 1954,
     "passengerQty": 5,
     "currency": "EUR",
     "type": "Suzuki",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"]},
    {"price": 2544,
     "passengerQty": 5,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"]},
    {"price": 2544,
     "passengerQty": 2,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"]},
    {"price": 9542,
     "passengerQty": 4,
     "currency": "USD",
     "type": "Ford",
     "transmission": "automatic",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"]},]

def warning(cars: list):
    """
    examines the input list wheather the number of passangers exeeds the paseengerQty of a list item
    input: a list containing set items. Set contains all data of a car
    output: a warning string for each item failing the condition
    """
    for car in cars:
        type = car['type']
        if len(car['passengers']) > car['passengerQty']:
            print(f'a(z) {type} típusú autóban túl sok az utas')

warning(cars)


""" 3. Feladat - 5 pont
Az előző cars tömbben váltsd át az autók árát euróból usd-be, és listázd ki az eredményt de csak az autó neve és ára legyen kiírva (és a pénznem) figyelj rá hogy átváltáskor nem csak a price-ot kell módosítani hanem a currency-t is. Az átváltáshoz nem kell lekérdezned az aktuális árfolyamot kódból, egyszerű konstans értékkel számolj."""

FXrate = 1.1

def FXconvert(cars):
    for car in cars:
        type = car['type']
        ccy = 'USD'
        if car['currency'] == "USD":
            usdprice = car['price'] 
            print(f'A {type} nevű autó ára: {usdprice} {ccy}')
        else:
            usdprice = int(car['price'] * FXrate)
            print(f'A {type} nevű autó ára: {usdprice} {ccy}')

FXconvert(cars)

""" 4. Feladat - 5 pont
Az alábbi két tömbből készítsd el a lenti kimenetet:
Kimenet:
John eats Japanese
John eats American
John eats Mexican
John eats French
Marissa eats Japanese
Marissa eats American
Marissa eats Mexican
Marissa eats French
.... a többi névre is """

persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

def who_eat_where(p: list, r: list):
    for p_name in p:
        for r_name in r:
            print(f'{p_name} eats {r_name}')
        
who_eat_where(persons, restaurants)


""" 5. Feladat - 5 pont

Alakítsd át az alábbi tömböt úgy, hogy minden belső listába egy harmadik elemet raksz, ami az előző két szám összegét tárolja
kimenet:  
[[4, 5, 9], [7, 4, 11], [2, 5, 7], [9, 4, 13]] """

my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

def append_sum(number_pairs: list) -> list:
    for item in number_pairs:
        sum = item[0] + item[1]
        item.append(sum)

append_sum(my_list)

print(my_list)
