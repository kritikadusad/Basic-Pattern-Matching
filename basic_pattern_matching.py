def naive(p, t):
    """ Returns a list of indeces of chars in given word
    matching given text.
    p is the pattern
    t is the given text
    Example:
    >>> naive("ATGC", "AATGCTTTATGC")
    [1, 8]

    """
    occurences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i + j] != p[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences


def naive_2mm(p, t):
    """
    Returns a list of indeces of chars in given word
    matching given text. This function can take upto
    2 mismatches.
    p is the pattern
    t is the given text
    Example:
    >>> naive_2mm("ATGC", "AAAGCTTTTATCC")
    [1, 9]

    """
    occurences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        error = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                error += 1
                if error > 2:
                    match = False
                    break
        if match:
            occurences.append(i)
    return occurences


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\nAll tests have passed.\n")
