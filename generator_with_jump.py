# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


from decimal import *

start = Decimal(2)
end = Decimal(5.5)
stepping = Decimal(0.5)


# result = start+stepping


def generator():
    result = start
    while result < end + stepping:
        print(result)
        result += stepping
