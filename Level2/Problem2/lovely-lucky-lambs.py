from itertools import count


def stingy(n):
    """
    Fibonacci numbers until the sum is greater
    or equals to the number os LAMBs.
    """
    pointer, accum = 0, 1
    for i in count():
        if n <= 0:
            break
        pointer, accum = accum, pointer+accum
        n -= accum
    return i


def generous(n):
    """
    Sequence of power 2 numbers until all LAMBs
    are assigned.

    Special case: the remaining LAMBs are less that
    the next power of 2, but greater that the sum of
    the pay of the two last subordinates.
    """
    sum_seq = 1
    seq = []
    for i in count():
        if sum_seq > n:
            break
        seq.append(sum_seq)
        sum_seq <<= 1
    seq = seq[:-1]
    return i if n-sum(seq) > sum(seq[-2:]) else i-1


def solution(total_lambs):
    if total_lambs < 2 or total_lambs >= 10**9:
        return 0
    return stingy(total_lambs) - generous(total_lambs)
