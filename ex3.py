# Задание 3
# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в тексте


file_read = open("zadanie3.txt", 'r')
file_write = open("zadanie3_out.txt", "w", encoding="utf-8")
z = {}
a = []


line = file_read.readlines()
print(type(line))
for i in line:
    j_razbitie_na_slova = i.split()

# Очищаю от знаков припинания, перевожу все в нижний регистр, проверяю на длину
    for j in j_razbitie_na_slova:
        j = j.strip('-,!.():; #"–')
        j = j.lower()
        if len(j) > 1:
            #print(type(j))
            a.append(j)

a = sorted(a)
b = sorted(set(a))
print(b)

for i in b:
    k = a.count(i)
    z = {'word': i, 'count': k}
    print(z['word'], z['count'], file=file_write)

#Считаю количество повторов слов






file_read.close()
file_write.close()
# #


     # for j in i:
    #     print(j, sep=' ', end=' ')
#
#
# with open(r'zadanie3.txt', 'r') as s_file:
#     words = [word for line in s_file for word in line.split()]
#     print(type(words))