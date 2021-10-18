from math import floor, sqrt

memo = [[None for k in range(20+1)] for n in range(200+1)]

def q(n, k):
    if n == k == 1:
        return 1
    elif k == 0 and n > 0:
        return 0
    elif  n < k or k < 1:
        return 0
    elif memo[n][k] is None:
        memo[n][k] = q(n-k, k) + q(n-k, k-1)
    return memo[n][k]


def solution(n):
    maxS = floor(((8*n+1)**.5 -1)/2)
    return sum(q(n,k) for k in range(int(maxS + 1)))-1


def main():
    n = 2000
    print([solution(n) for n in range(1,n)])


if __name__ == "__main__":
    main()
