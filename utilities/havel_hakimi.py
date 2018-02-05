def recursive_check_hh_theorem(degree_sequence):
    """
    Havel Hakimi Theorem
    :param degree_sequence:
    :return:

    >>> recursive_check_hh_theorem([2,3,2,3])
    True

    >>> recursive_check_hh_theorem([2,2,2,2,2,2])
    True

    >>> recursive_check_hh_theorem([])
    False

    >>> recursive_check_hh_theorem([3,3,2,3])
    False
    """
    if len(degree_sequence) == 0:
        return False

    if not any(degree_sequence):
        # sequence consists only of zeros return true
        return True

    s = sorted(degree_sequence)[:-1]
    sprime = [d - 1 for d in s if d > 0]
    return recursive_check_hh_theorem(sprime)


def iterative_check_hh_theorem(degree_sequence):
    """
    Havel Hakimi Theorem (iterative version)
    :param degree_sequence:
    :return:

    >>> iterative_check_hh_theorem([2,3,2,3])
    True

    >>> iterative_check_hh_theorem([2,2,2,2,2,2])
    True

    >>> iterative_check_hh_theorem([])
    False

    >>> iterative_check_hh_theorem([3,3,2,3])
    False
    """
    while any(degree_sequence) and len(degree_sequence) > 1:
        degree_sequence = [d - 1 for d in sorted(degree_sequence)[:-1] if d > 0]

    if len(degree_sequence) == 0:
        return False

    if not any(degree_sequence):
        # sequence consists only of zeros return true
        return True
    else:
        raise Exception('The resulting degree sequence is neither empty nor full of zeros! {}'.format(degree_sequence))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
