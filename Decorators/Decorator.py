class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Olá, meu nome é {self.name}")


class LoggerDecorator:
    def __init__(self, person):
        self.person = person

    def say_hello(self):
        print(f"[LOG] Chamando say_hello para {self.person.name}")
        self.person.say_hello()


# Cria um objeto Person
person = Person("João")

# Aplica o decorador ao objeto Person
person = LoggerDecorator(person)

# Chama o método say_hello
person.say_hello()
