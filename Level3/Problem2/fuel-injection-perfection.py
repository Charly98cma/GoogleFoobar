def solution(n):
    n = int(n)
    # Filter limits and basic cases
    if n < 2 or n > 10**309: return 0
    counter = 0
    while n > 1:
	print n
        if n % 2 == 0:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        counter += 1
    return counter

print solution(str(10**309-1))
