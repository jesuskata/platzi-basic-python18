PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('The password is incorrect!')

    return wrapper


@password_required # Este es nuestro decorador puesto en práctica
def needs_password():
    print('The password is correct!')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@upper
def say_my_name(name):
    return f'Hello {name}'


if __name__ == '__main__':
    name = input('What is your name? ')
    print(say_my_name(name))
    # needs_password()
