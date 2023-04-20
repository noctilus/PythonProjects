def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        print("4 6 loop")
        for digit in pin:
            try:
                print("try")
                int(digit)
            except ValueError:
                return ValueError
        return True
    return False


print(validate_pin("1.234"))
