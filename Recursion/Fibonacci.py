
def loop_fibonacci(n):
    if n < 2:
        print("get out under of age 1")
        return -1

    n_0 = 0
    n_1 = 1
    new_n = None
    print(n_0)
    print(n_1)

    for e in range(n-1):
        new_n = n_0 + n_1
        n_0 = n_1
        n_1 = new_n

        print(new_n)

    return new_n


def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    else:
        print("error wtf")
        return -1
