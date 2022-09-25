"""ANSTA zadanie przed rozmową"""
# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

LOWER_LIMIT = "79-900"
UPPER_LIMIT = "80-155"


def generator():
    """reqd"""
    lower_int = int(LOWER_LIMIT.replace("-", ""))
    upper_int = int(UPPER_LIMIT.replace("-", ""))

    for i in range(lower_int, upper_int - 1):
        i += 1
        # not sure if .format would be better ?
        print(str(i)[slice(0, 2)] + "-" + str(i)[slice(2, 5)])


generator()
