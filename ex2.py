# Задания из класса про работу с файлами на слайдах 4, 8, 9, 10:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
# (кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
# 2. А теперь воспользуйтесь менеджером контекста для файлов (with … as).


def song(a = 3, b = 3, c = 0):
    p = ("-".join(["la"] * b) + '\n') * a
    if c:
        return p[:-1] + '!'
    else:
        return p[:-1] + '.'

d = song()


with open("song_type1.txt", "w") as myfile:
    myfile.write(d)
myfile.close()


f = open("ex1.txt", 'r', encoding="UTF-8")
z = open("Secondfile.txt", 'w', encoding='UTF-8')
for line in f:
    print(line.rstrip(), file=z)
    if not line:
        break
f.close()
z.close()


testfile = open("ex1.txt", encoding="UTF-8")
for line in testfile:
    print(line.rstrip('\n') + "!")



ff1 = open("ex1.txt", 'r', encoding="UTF-8")
zz1 = open("Thirdfile.txt", 'w', encoding='UTF-8')
n = 0
for line in ff1:

    print(line.rstrip() + '       ' + "Number: строка из файла" + ' ' + "ex1.txt  №" + ' ',  n, file=zz1)
    n += 1
    if not line:
        break
ff1.close()
zz1.close()
