import time
from time import sleep
"""a = "a10b2c3e10b4g7"


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def ffd(a):
    res = ''
    i = 0
    length = len(a)
    isEnd = False
    while i < len(a):
        for j,itemj in enumerate(a):
            if not is_number(itemj) or j == len(a)-1:
                if j != len(a)-1:
                    s = a[i:j]
                else:
                    s = a[0:len(a)]
                    isEnd = True
                if s != '':
                    if isEnd == False:
                        for k in range(int(s[1:len(s)])):
                            res = res + s[0:1]
                        a = a[j:length]
                        i = -1
                        break
                    else:
                        for k in range(int(s[1:len(s)])):
                            res = res + s[0:1]
                        return res
        i+=1


with open('C:/Users/Вячеслав/PycharmProjects/TestWeatherBot/testBd.txt') as inf:
    for line in inf:
        result = ffd(line)
with open('C:/Users/Вячеслав/PycharmProjects/TestWeatherBot/testBdOut.txt', 'w') as ouf:
    ouf.write(result)
"""



"""list_of_string = []
massive = []
massivetmp = []
str1 = ''
i_max = 0
j_max = 0
string = input()
if string == 'end':
    print('')
else:
    while string != "end":
        list_of_string.append(string)
        string = input()

    # print(list_of_string)

    for i, item in enumerate(list_of_string):
        massive.append(item.split())
        massivetmp.append(item.split())

    for i in range(len(massive)):
        for j in range(len(massive)):
            if j > j_max:
                j_max = j
        if i > i_max:
            i_max = i

    for i in range(len(massive)):
        for j in range(len(massive)):
            if i - 1 == -1:
                a = int(massive[i_max][j])
            else:
                a = int(massive[i - 1][j])
            if i + 1 == len(massive):
                b = int(massive[0][j])
            else:
                b = int(massive[i + 1][j])

            if j - 1 == -1:
                c = int(massive[i][j_max])
            else:
                c = int(massive[i][j - 1])
            if j + 1 == len(massive):
                d = int(massive[i][0])
            else:
                d = int(massive[i][j + 1])
            massivetmp[i][j] = int(a + b + c + d)

    # print(massivetmp)

    for i in range(len(massivetmp)):
        for j in range(len(massivetmp)):
            str1 = str1 + ' ' + str(massivetmp[i][j])
        str1 = str1 + '\n'
    print(str1)"""

"""d = {}
input_string = 'aabbgccdefddf'
for i, item in enumerate(input_string):
    here_more_then_one = False
    for j, itemj in enumerate(input_string):
        if j != i:
            if item == itemj:
                here_more_then_one = True
                break
    if not here_more_then_one:
        d.update({item:i})

for key, value in d.items():
    if min(d[key] for key in d) == value:
        print(key)"""

"""Написать декоратор, который принимает два параметра:
1. Количество секунд
2. Количество попыток
Декоратор вызывает функцию указанное число раз и ждет указанное время между каждым вызовом функции."""


"""def print_in_time(f, secs, count):
    def wrapper():
        for i in range(count):
            print('Идет выполнение функции {0}-й раз'.format(i+1))
            f()
            print('Ждем {0} секунд до следующего вызова функции\n'.format(secs))
            time.sleep(secs)
    return wrapper


def func():
    print("Выполнение функции")


func = print_in_time(func,3,10)
func()"""


"""def f(x):
    return x*2

d = {}
k = []
n = int(input())
for i in range(n):
    k.append(int(input()))
s = set(k)
for i,item in enumerate(s):
    d.update({item:f(item)})

for i,item in enumerate(k):
    for key,value in d.items():
        if item == key:
            print(value)"""


class User_comments:
    def __init__(self, user_id, comment_id):
        self._user_id = user_id
        self._comment_id=comment_id

    def print_user_id(self):
        return int(self._user_id)

    def print_comment_id(self):
        return int(self._comment_id)

users =[
    User_comments(1,1),
    User_comments(2,2),
    User_comments(1,9),
    User_comments(3,3),
    User_comments(4,4),
    User_comments(5,5),
    User_comments(1,6),
    User_comments(2,10),
    User_comments(1,7),
    User_comments(2,8),
    User_comments(1,11),
    User_comments(2,12),
    User_comments(1,13),
    User_comments(3,14),
    User_comments(4,15),
    User_comments(5,16),
    User_comments(1,17),
    User_comments(2,18),
    User_comments(1,19),
    User_comments(2,20),
    User_comments(1,21),
    User_comments(2,22),
    User_comments(1,23),
    User_comments(3,24),
    User_comments(4,25),
    User_comments(5,26),
    User_comments(1,27),
    User_comments(2,28),
    User_comments(1,29),
    User_comments(2,20),
    User_comments(1,31),
    User_comments(2,32),
    User_comments(1,33),
    User_comments(3,34),
    User_comments(4,35),
    User_comments(5,36),
    User_comments(1,37),
    User_comments(2,38),
    User_comments(1,39),
    User_comments(2,40),
]

d = {}

for i,item in enumerate(users):
    needUpdate = True
    comment_count = 0
    k = item.print_user_id()
    c = item.print_comment_id()
    if d == {}:
        d.update({k:1})
    else:
        for key, value in d.items():
            if key == k:
                needUpdate = False
    if needUpdate == True:
        d.update({k: 1})

        for j, itemj in enumerate(users):
            k1 = itemj.print_user_id()
            c1 = itemj.print_comment_id()
            if c1 != c and k == k1 and needUpdate == True:
                comment_count = 1
                for key,value in d.items():
                    if key == k:
                        comment_count = value + 1
                d.update({k:comment_count})

for key, value in d.items():
    if value > 10:
        print("Пользователь, имеющий id {0} оставил {1} сообщений".format(key, value))
"""Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the"""

"""s = set()
c = set()
tmp = []
tmp1 = []
check_list = []
list_for_check=[]
n = int(input())
for i in range(n):
    right_str = str(input())
    right_str = right_str.lower()
    l = list(map(str, right_str.split()))
    check_list.append(l)
k = int(input())
for j in range(k):
    to_check_str = str(input())
    to_check_str = to_check_str.lower()
    l = list(map(str,to_check_str.split()))
    list_for_check.append(l)

for i,item in enumerate(list_for_check):
    for j,itemj in enumerate(item):
        tmp.append(itemj)
tmp = set(tmp)

for i,item in enumerate(check_list):
    for j,itemj in enumerate(item):
        tmp1.append(itemj)
tmp1 = set(tmp1)

for i,item in enumerate(tmp):
    if item not in tmp1:
        print(item)"""

"""l = []
d = {}
n = int(input())
for i in range(n):
    string = str(input())
    l = list(map(str, string.split()))
    d.update({l[0]:int(l[1])})

for key,value in d.items():
    if key == 'север':
        verx = value
    if key == 'юг':
        niz = value
    if key == 'запад':
        sleva = value
    if key == 'восток':
        sprava = value

print(sprava - sleva, verx - niz)"""
