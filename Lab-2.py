#  вариант 2
import csv
import os
from time import sleep

RED = '\u001b[41m'
GREEN = '\u001b[42m'
BLUE = "\u001b[44m"
WHITE = '\u001b[47m'
BLACK = "\u001b[40m"
END = '\u001b[0m'

# задание 1
print('Задание 1:')


def flag_ban():
    print(GREEN + ' ' * 40 + END)
    for i in range(3):
        print(GREEN + '  ' * (6 - i * 2) + RED + '  ' * (2 + 2 * i) + RED + '  ' * (2 + 2 * i) + GREEN + '  ' * ((6 - 2 * i) + 4) + END)

    for i in range(3):
        print(GREEN + '  ' * (4 + 2 * i) + RED + '  ' * (4 - 2 * i) + RED + '  ' * (4 - i * 2) + GREEN + '  ' * ((4 + 2 * i) + 4) + END)


flag_ban()
print()

print('Задание 2:')
#  задание 2
n = 10


def uzor():
    for k in range(1):
        print((BLACK + '  ' * (5) + WHITE + '  ' * (3) + END) * n)
        print((BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + END) * n)
        print((BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (3) + WHITE + '  ' * (3) + END) * n)
        print((BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (5) + END) * n)
        print((BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (6) + END) * n)


uzor()
print()

print('Задание 3:')
# задание 3


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = 2 * i + 3


step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
print()

print('Задание 4:')
# задание 4
with open('books.csv', 'r') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    big = 0
    small = 0
    z = -1
    for row in list(books)[1:]:
        year = row[6][:4]

        if int(year) <= 2015:
            small += 1
        else:
            big += 1

summa = small + big
a = small * 100 // summa
b = big * 100 // summa + 1

print("До 2015    " + BLUE + '  ' * a + END + ' ' + str(a) + '%')
print()
print("После 2015 " + BLUE + '  ' * b + END + ' ' + str(b) + '%')
print()

#  доп задание
t = 0.5
os.system('cls')
print(WHITE + '  ' * 5 + BLUE + '  ' * 5 + RED + '  ' * 5 + END)
sleep(t)
os.system('cls')
print(RED + '  ' * 3 + WHITE + '  ' * 5 + BLUE + '  ' * 5 + RED + '  ' * 2 + END)
sleep(t)
os.system('cls')
print(RED + '  ' * 5 + WHITE + '  ' * 5 + BLUE + '  ' * 5 + RED + '  ' * 0 + END)
sleep(t)
os.system('cls')
print(BLUE + '  ' * 3 + RED + '  ' * 5 + WHITE + '  ' * 5 + BLUE + '  ' * 2 + END)
sleep(t)
os.system('cls')
print(BLUE + '  ' * 5 + RED + '  ' * 5 + WHITE + '  ' * 5 + END)
sleep(t)
os.system('cls')
print(WHITE + '  ' * 3 + BLUE + '  ' * 5 + RED + '  ' * 5 + WHITE + '  ' * 2 + END)
sleep(t)
os.system('cls')
print(WHITE + '  ' * 5 + BLUE + '  ' * 5 + RED + '  ' * 5 + END)
sleep(t)
os.system('pause')