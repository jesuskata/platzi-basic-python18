def test_value_args(n_arg, *args):
    print(f'First normal value: {n_arg}')

    for arg in args:
        print(f'This is one of the *args values: {arg}')

    print(type(args)) # tuple
    print(type(n_arg)) # str


if __name__ == '__main__':
    test_value_args('jesus', 'eloisa', 'tiana', 'aleisa', 'jana')