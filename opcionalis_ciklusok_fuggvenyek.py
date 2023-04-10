
""" 1. Feladat - 3 pont
készíts egy programot ami az alábbi listában eldönti az összes elemről hogy osztható e kettővel vagy nem """

nums = [3,4,9,6,2]

def divider(nums):
    for item in nums:
        if item % 2 == 0:
            print(f'{item} osztható')
        else:
            print(f'{item} nem osztható')

divider(nums)


""" 2. Feladat - 2 pont
készíts egy programot ami kiírja a lista összes elemét de úgy hogy az indexét is pl. ebből: """

players = ['Peter', 'Kate', 'John']

def numbered_list(list):
    i = 1
    for item in list:
        print(f'{i}. {item}')
        i += 1

numbered_list(players)

""" 3. Feladat - 5 pont
Készíts egy függvényt ami megvizsgálja egy elem összes típusát, és kigyűjti őket egy új listába. pl. ebből a listából: """

x = ('', 4, True)
a = []

def type_of_data(x):
    for item in x:
        if type(item) is int:
            a.append('integer')
        elif type(item) is bool:
            a.append('boolean')
        elif type(item) is str:
            a.append('string')
        else:
            a.append('other type')

type_of_data(x)

print(a)

