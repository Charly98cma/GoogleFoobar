def le_bombs(a, b, n):
    """
    Calculates the next pair of bombs
    """
    n_times = a/b - 1
    if n_times == 0:
        a -= b
        n += 1
    else:
        a -= b*n_times
        n += n_times
    return a, b, n

def get_cycles(x, y, n = 0):
    """
    Recursive function to finds the solution
    """
    if x == 1 and y == 1: return n
    if x == y: return "impossible"
    return get_cycles(*le_bombs(max(x,y), min(x,y), n))

def solution(x, y):
    x, y = int(x), int(y)
    if x < 1 or x > 10**50 or y < 1 or y > 10**50 or x == y:
        return "impossible"
    return str(get_cycles(x, y))

print(solution('2', '1'))
print(solution('4', '7'))
