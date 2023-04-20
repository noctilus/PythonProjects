def is_pangram(s):
    pangram_letters = set(map(chr, range(97, 123)))
    s_lower = s.lower()
    s_lower = set(s_lower)
    result = s_lower.intersection(pangram_letters)
    print(len(result))

    if len(result) != 24:
        return False
    else:
        return True


is_pangram("The quick, brown fox jumps over the lazy dog!")
