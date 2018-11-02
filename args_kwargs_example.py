def test_value_args_kwargs(*args, **kwargs):
    print(type(args))
    print(args)
    print('*' * 50)
    print(type(kwargs))
    print(kwargs)


if __name__ == '__main__':
    test_value_args_kwargs('jesus', 'eloisa', family = 'Romero Camarillo', city = 'Huajuapan')