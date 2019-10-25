# Задание 1 (Обязательное всем, кроме части со звёздочкой!!!!)
# Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
# •	Создаём книгу POST /books/, вы запоминаете его id.
# •	Проверяете, что она создалась и доступна по ссылке GET/books/[id]
# •	Проверяете, что она есть в списке книг по запросу GET /books/
# •	Изменяете данные этой книги методом PUT /books/[id]/
# •	Проверяете, что она изменилась и доступна по ссылке /books/[id]
# •	Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
# •	Удаляете эту книгу методом DELETE /books/[id].

import json
import requests

url = 'http://pulse-rest-testing.herokuapp.com/books'
r_before = requests.get(url)
r_before = json.loads(r_before.text)
book = {'title': 'Война и мир', 'author': 'Лев'}


#Заводим запись книги и проверяем создание
print(requests.post(url, book).status_code)

r_after = requests.get(url)
r_after = json.loads(r_after.text)
for i in r_after:
    if i['author'] =='Лев':
        z = i['id']
        z = str(url + '/' + str(z))
        if requests.get(z).status_code == 200:
            print("All is OK")


for i in r_after:
    for ii in r_before:
        if i['title'] != ii['title']:
            if i['title'] == 'Война и мир':
                z = 'Книга доступна'
print(z)


#•	Изменяете данные этой книги методом PUT /books/[id]/ и проверяем, что апдейт прошел успешно
for i in r_after:
    book_update = {'title': 'Война и мир и еще чет)))', 'author': 'Лев'}
    if i['author'] =='Лев':
        z = i['id']
        z = str(url + '/' + str(z))
        if requests.put(z, data=book_update).status_code == 200:
            print("Update is good")

#•	Все свои книги удаляем
for i in r_after:
    if i['author'] =='Лев':
        z = i['id']
        z = str(url + '/' + str(z))
        requests.delete(z)

