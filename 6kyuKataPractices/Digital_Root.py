def digital_root(n):
    while n > 9:
        n = sum(map(int,str(n)))
    return n
