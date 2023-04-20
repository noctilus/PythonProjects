def unique_in_order(sequence):
    sequence = list(sequence)
    result = list()
    if len(sequence) == 0:
        print(sequence)
        return

    else:
        result.append(sequence[0])
        for item in sequence:
            if item != result[-1]:
                result.append(item)
        print(result)
    return


unique_in_order('A')
