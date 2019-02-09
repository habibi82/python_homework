# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name):
        self._speed = speed
        self._color = color
        self._name = name
        self._speed = False

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print('Turning ', direction)


class SportCar:
    def __init__(self, speed, color, name):
        self._speed = speed
        self._color = color
        self._name = name
        self._speed = False

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print('Turning ', direction)
class  WorkCar:
    def __init__(self, speed, color, name):
        self._speed = speed
        self._color = color
        self._name = name
        self._speed = False

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print('Turning ', direction)
class PoliceCar:
    def __init__(self, speed, color, name):
        self._speed = speed
        self._color = color
        self._name = name
        self._speed = True

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print('Turning ', direction)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    def __init__(self, speed, color, name):
        self._speed = speed
        self._color = color
        self._name = name
        self._speed = True

    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print('Turning ', direction)



class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name):
        self.name = name
        self._health = 100
        self._damage = 0
        self._armor = 1.2


    def get_health(self):
        return self._health


    def get_damage(self):
        return self._damage


    def set_armor(self, armor):
        self._armor = armor

    def attack(self):
        self._health-=20
        print("Attacking...", self.name)
    def _harm(self):
        return self._damage/self._armor




class Player(Person):

    def __init__(self, name):
        super().__init__(name)

class Enemy(Person):

    def __init__(self, name):
        super().__init__(name)

class Game():

    def __init__(self):
        self.player = Player('Vanya')
        self.enemy = Enemy('Vasya')



    def do_game(self):
        while (self.player.get_health()>0 or self.enemy.get_health()>0):
             self.player.attack()
             self.enemy.attack()

        if self.player.get_health() <= 0:
                print('Is winner ', self.enemy.name)
        else:
            print('Is winner ', self.player.name)
# player = Player('Vanya')
# enemy = Enemy('Vasya')
game = Game().do_game()

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        print('AnimalToy was  created')

class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        print('CartoonToy was  created')
class ToyFactory:

    def __init__(self, toy_type):
        self.type = toy_type



    def _stuff_buying(self):
        print('Buying materials...')

    def _sewing(self):
        print('sewing...')

    def _coloring(self):
        print('Coloring...')

    def product(self):
        if self.type == 'AnimalToy':
            self._stuff_buying()
            self._sewing()
            self._coloring()
            toy =  AnimalToy('', '')
        if self.type == 'CartoonToy':
            self._stuff_buying()
            self._sewing()
            self._coloring()
            toy =  CartoonToy('', '')
        return toy

toy = ToyFactory('AnimalToy').product()
print(type(toy))

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка