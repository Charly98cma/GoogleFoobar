def solution(s):
    if s.count("<") == 0: return 0
    l = [x.count('>') for x in s.split("<")][:-1]
    index = list(range(len(l), 0, -1))
    return sum([l[i]*index[i]*2 for i in range(len(l))])
