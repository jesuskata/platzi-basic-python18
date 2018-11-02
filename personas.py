class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')


if __name__ == '__main__':
    name = input('What is your name? ')
    age = int(input('What is your age? '))

    person = Person(name, age)

    print(f'Age: {person.age}')
    person.say_hello()