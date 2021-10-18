def solution(n):
    res_len = n + 5
    prime_seq = ""
    # Generate prime sequence
    for x in range(2, 1000000):
        for y in range(2, x):
            if x % y == 0: break
        else:
            prime_seq += str(x)
            # Return if found sequence
        if len(prime_seq) >= res_len:
            return prime_seq[n:res_len]

print(solution(300))
