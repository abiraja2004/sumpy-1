
from math import log10


def common_words(s1, s2):

    s1 = s1.split()
    s2 = s2.split()
    l_s1 = len(s1)
    l_s2 = len(s2)
    assert l_s1 != 0
    assert l_s2 != 0

    shortest = s1 if l_s1 < l_s2 else s2
    den = log10(l_s1) + log10(l_s2)
    comm_words = 0
    for word in shortest:
        if word in s1 and word in s2:
            comm_words = comm_words +1

    return comm_words / den

