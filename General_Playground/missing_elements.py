# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# #NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE

# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

n = 10
entry_elements = [2, 3, 7, 4, 9]
full_list = list(range(1, n + 1))


def missing_elements():
    for x in entry_elements:
        full_list.remove(x)
    print(full_list)
# będzie szybciej ?
# set.difference() zamiast list?


missing_elements()
