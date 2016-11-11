def cube(n):
    return n**3


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def count_pattern(pattern, list):
    for x in list:
        if pattern[0] is x:
        	