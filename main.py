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
    return print('Client is not in the client\'s list')


def _get_client_field(field_name, message='What is the client {}? '):
    field = None

    while not field:
        field = input(message.format(field_name))
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


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _not_founded()


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del client[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
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
        list_clients()
        client_id = int(_get_client_field('id'))
        updated_client = _get_clients_data()
        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name.lower())

        if found:
            print(f'The client: {client_name.lower()} is in the client\'s list')
            list_clients()
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('Invalid command! Please try again')
