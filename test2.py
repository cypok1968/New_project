from requests import get, post, put, delete

# print(get('http://localhost:5000/api/v2/news').json())
# print(get('http://localhost:5000/api/v2/news/1').json())
# print(get('http://localhost:5000/api/news/1000').json())
# print(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/v2/news', json={}).json())
# print(post('http://localhost:5000/api/v2/news', json={'title': 'Заголовок'}).json())
print(post('http://localhost:5000/api/v2/news',
           json={
               'title': 'Заголовок2 через API2',
               'content': 'Новость2 через API',
               'user_id': 2,
               'is_private': 0,
           }).json())

# print(delete('http://localhost:5000/api/news/500').json())
# print(delete('http://localhost:5000/api/news/4').json())

# print(put('http://localhost:5000/api/news/1', json={}).json())
# print(put('http://localhost:5000/api/news/1', json={'title': 'Изменён'}).json())
