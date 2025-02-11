# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def info(name, age, city):
    print(name + ', ', age + ' год(а), проживает в городе', city)


info('Тимур', '11', 'Москва')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def big_num(a, b, c):
    print(max(a, b, c))


big_num(1, 2, 3)


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def bigstr(*st):
    print(max(*st, key=len))


bigstr('123', '1234', '12345', '1', '123456', '12')
