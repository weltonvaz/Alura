from animal import Animal, Cachorro, Gato

class Main(Animal):
    def __init__(self, animal):
        animal.Fala()

Main(Gato())