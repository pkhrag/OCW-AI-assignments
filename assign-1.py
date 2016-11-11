def cube(n):
    return n**3


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def count_pattern(pattern, list):
    return sum(1 for x in range(len(list)) if list[x:x + len(pattern)] == pattern)
