# (1), тебе нужен файл .gitignore, запиши туда свой венв чтоб он не отсылался на гитхаб и вообще не отслеживался
# (2), нужно сделать комманду pip3 freeze > requirements.txt
# (3), для инита юзай **kwargs
# (4), нужна валидация на входные данные


# нужен базовый инит
from time import sleep


class Animal:
    def __init__(self, name, move):
        self.move = move
        self.name = name

    def get_info(self):
        print("Имя:", self.name)
        print("Тип животного:", self.breed)
        print("Количество лап:", self.paws)

    def _get_move_mode(self) -> str:
        return self.move

    def get_move_mode(self):
        print("Способ передвижения:", self._get_move_mode())


class Cat(Animal):
    def __init__(self, name, breed="default cat", paws=4, move="ходьба"):
        self.breed = breed
        self.paws = paws
        super().__init__(name=name, move=move)

    def _get_move_mode(self) -> str:
        for i in range(5):
            print('im sleeping... Zzz')
            sleep(1)
        print('мяу')
        return super()._get_move_mode()


class Dog(Animal):
    def __init__(self, name, breed="default cat", paws=4, move="ходьба"):
        self.breed = breed
        self.paws = paws
        super().__init__(name=name, move=move)


class Fish(Animal):
    def __init__(self, name, fins=3, move="плавание"):
        self.fins = fins
        super().__init__(name=name, move=move)

    def get_info(self):
        print("Имя:", self.name)
        print("Количество плавников:", self.fins)


class Human(Animal):
    def __init__(self, name, hands=2, legs=2, move="ходьба"):
        self.hands = hands
        self.legs = legs
        super().__init__(name=name, move=move)

    def get_info(self):
        print("Имя:", self.name)
        print("Количество рук:", self.hands)
        print("Количество ног:", self.legs)


a = Cat('kitty')
a.get_info()
a.get_move_mode()
