def get_lst_fib(_count):
    fib_lst = [1, 1]
    for num in range(_count - 2):
        fib_lst.append(fib_lst[num] + fib_lst[num + 1])
    print(fib_lst)


def get_last_fib_nmb(_nmb):
    fib_lst = [1, 1]
    for num in range(_nmb - 2):
        fib_lst[0], fib_lst[1] = fib_lst[1], fib_lst[0] + fib_lst[1]

    print(fib_lst[1])


number = 20
get_lst_fib(number)
get_last_fib_nmb(number)
