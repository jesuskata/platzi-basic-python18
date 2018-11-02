def test_value_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f'{key} == {value}')

    print(type(kwargs))


if __name__ == '__main__':
    test_value_kwargs(family1 = 'Romero', family2 = 'Camarillo')