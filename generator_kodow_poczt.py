# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


lower_limit = "79-900"
upper_limit = "79-903"


def generator(lower_limit, upper_limit):
    lower_int = int(lower_limit.replace("-", ""))
    upper_int = int(upper_limit.replace("-", ""))

    for i in range(lower_int, upper_int - 1):
        i += 1
        print(i)


generator("79-900", "79-905")
