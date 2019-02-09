# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def my_function(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def my_max(a,b,c):
    my_max =0;
    if a > b:
        my_max = max(a, c)
    else:
        my_max = max(b, c)
    return my_max
print(my_max(2,5,6))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
def my_str_function(*args):
    max_len=0
    string = ''
    for arg in args:
        if len(arg) > max_len:
            max_len = len(arg)
            string = arg
    return string
print(my_str_function('dfgg', 'sdfsdf', 'sdfljvhb'))

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['вася', 'коля', 'петя']
salaries = [200000, 300000, 5000000]
file = open("salary.txt", 'r+', 100, 'utf-8')

for name , salary in zip(names, salaries):
    if salary < 500000:
        file.write('{} - {}'.format(name, salary)+'\n')


for line in file:
    print(line.upper(), end='')

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
player_name = input("введите имя игрока")
enemy_name = input('введите имя противника')

player = {'name': player_name, 'health': 100, 'damage':20, 'armor': 1.2}
enemy = {'name': enemy_name, 'health': 200, 'damage':100, 'armor': 1.2}

def attack(person1, person2):
    person2['health']=person2['health'] - person1['damage']
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

def harm(person):
    return person['damage']/person['armor']

attack(player, enemy)
print(player, enemy)

# player_file =  open(player_name+'.txt', 'w')
# enemy_file =  open(enemy_name+'.txt', 'w')
with open (player_name+'.txt', 'w') as player_out:
    for key, value in player.items():
        player_out.write('{}:{}\n'.format(key, value))
with open (enemy_name+'.txt', 'w') as enemy_out:
    for key, value in enemy.items():
        enemy_out.write('{}:{}\n'.format(key, value))


def game(player_name, enemy_name):
    with open(player_name+'.txt', 'r') as player_inp:
        for i in player_inp.readlines():
            key, value = i.strip().split(':')
            player[key]=value
    with open(enemy_name+'.txt', 'r') as enemy_inp:
        for i in enemy_inp.readlines():
            key, value = i.strip().split(':')
            enemy[key]=value


    while int(player['health'])  <=0 or int(enemy['health'])   <=0:
        attack(player, enemy)
        attack(enemy, player)

    if int(player['health'])  <=0 :
        print(enemy['name'], enemy['health'])
    else:
        print(player['name'], player['health'])
game(player_name, enemy_name)

