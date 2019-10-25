# Второй скрипт:
# •	тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с книгой, которая уже должна существовать.
# Создайте книгу заранее в этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то другой может удалить.
import json
import requests

url = 'http://pulse-rest-testing.herokuapp.com/books'
url2 = 'http://pulse-rest-testing.herokuapp.com'

create_book = requests.post(url, json={'author': 'Lev', 'title': 'War'})
create_book_id = create_book.json()

book_url = url + '/' + str(create_book_id['id'])

role_setup = requests.post(url2 + "/roles", json={'name': 'Lev', 'type': 'Художественная литература', 'level': 3, 'book': book_url})
all11 = url2 + "/roles"








# for i in role_setup_answer_all:
# role_setup_answer_all = requests.get(all11)
# role_setup_answer_all = json.loads(role_setup_answer_all.text)
#     if i['name'] == 'Lev':
#         z = i['id']
#         z = str(all11 + '/' + str(z))
#         requests.delete(z)


