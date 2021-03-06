def do_twice(f, v):
    f(v)
    f(v)


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


def print_twice(s):
    print(s)


do_twice(print_twice, 'do twice')
do_four(print_twice, 'do four')
