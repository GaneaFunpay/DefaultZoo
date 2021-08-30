class Animal:

    def getInfo(self):
        print("Имя:", self.name)
        print("Тип животного:", self.breed)
        print("Количество лап:", self.paws)

    def getWaytomove(self):
        print("Способ передвежения:", self.move)
        # return self.move


class Cat(Animal):
    def __init__(self, name, breed="default cat", paws=4, move="ходьба"):
        self.name = name
        self.type = breed
        self.paws = paws
        self.move = move


class Dog(Animal):
    def __init__(self, name, breed="default cat", paws=4, move="ходьба"):
        self.name = name
        self.type = breed
        self.paws = paws
        self.move = move


class Fish(Animal):
    def __init__(self, name, breed="default fish", fins=3, move="плавание"):
        self.name = name
        self.type = breed
        self.fins = fins
        self.move = move

    def getInfo(self):
        print("Имя:", self.name)
        print("Тип животного:", self.breed)
        print("Количество плавников:", self.fins)


class Human(Animal):
    def __init__(self, name, hands=2, legs=2, move="ходьба"):
        self.name = name
        self.hands = hands
        self.legs = legs
        self.move = move

    def getInfo(self):
        print("Имя:", self.name)
        print("Количество рук:", self.hands)
        print("Количество ног:", self.legs)
