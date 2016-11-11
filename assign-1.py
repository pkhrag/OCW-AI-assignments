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
z = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))


def depth(exp, count):
    if not isinstance(exp, (list, tuple)):
        return 0
    dep = 1
    for i in range(len(exp)):
        if isinstance(exp[i], (list, tuple)):
            dep = max(1 + depth(exp[i], count), dep)
    return dep

# print(depth(y, 0))


def tree_ref(tree, exp, ptr):
    if ptr >= len(exp):
        return tree
    return tree_ref(tree[exp[ptr]], exp, ptr + 1)


# print(tree_ref(z, (0,0), 0))
