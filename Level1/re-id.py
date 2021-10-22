def solution(n):
    res_len = n + 5
    prime_seq = ""
    # Generate prime sequence
    for x in range(2, 30000):
        for y in range(2, x):
            if x % y == 0: break  # Not prime
        else:
            prime_seq += str(x)  # Found prime
        # Return when found sequence
        if len(prime_seq) >= res_len:
            return prime_seq[n:res_len]
