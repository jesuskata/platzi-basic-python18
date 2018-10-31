import sys

clients = [
    {
        'name': 'pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Softwre engineer'
    },
    {
        'name': 'ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer'
    }
]

# Reusable functions
def _not_founded():
    return print('Client is not in the clients list')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')
    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_clients_data():
    return {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }


# Action functions
def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('The client you enter is already on the client\'s list. Please try again')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _not_founded()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_founded()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO VENTAS!')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_clients_data()
        create_client(client)
        list_clients()
    elif command == 'L':
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
    elif command == 'S':
        client_name = _get_client_name().lower()
        found = search_client(client_name.lower())

        if found:
            print(f'The client: {client_name.lower()} is in the client\'s list')
            list_clients()
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('Invalid command! Please try again')
