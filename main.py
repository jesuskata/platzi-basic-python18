clients = 'pablo,ricardo,'

# Reusable functions
def _add_comma():
    global clients

    clients += ','


def _not_founded():
    return print('Client is not in the clients list')


def _get_client_name():
    return input('What is the client name? ')


# Action functions
def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('The client you enter is already on the client\'s list. Please try again')


def list_clients():
    global clients

    print(clients)


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        _not_founded()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        _not_founded()


def _print_welcome():
    print('WELCOME TO VENTAS!')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name.lower(), updated_client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name.lower())
        list_clients()
    else:
        print('Invalid command! Please try again')