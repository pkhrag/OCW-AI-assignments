def cube(n):
    return n**3


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def count_pattern(pattern, list):
    return sum(1 for x in range(len(list)) if list[x:x + len(pattern)] == pattern)


x = [[1, 2], 1, 2, 3]
y = ('+', ('expt', 'x', 2), ('expt', 'y', 2))


def depth(exp, count):
    if not isinstance(exp, (list, tuple)):
        return 0
    dep = 1
    for i in range(len(exp)):
        if isinstance(exp[i], (list, tuple)):
            dep = max(1 + depth(exp[i], count), dep)
    return dep

# print(depth(y, 0))
