from requests import get, post, put, delete

# print(get('http://localhost:5000/api/news').json())
# print(get('http://localhost:5000/api/news/1').json())
# print(get('http://localhost:5000/api/news/1000').json())
# print(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/news', json={}).json())
# print(post('http://localhost:5000/api/news', json={'title': 'Заголовок'}).json())
# print(post('http://localhost:5000/api/news',
#            json={
#                'title': 'Заголовок через API',
#                'content': 'Заголовок через API',
#                'user_id': 1,
#                'is_private': 0,
#            }).json())

print(delete('http://localhost:5000/api/news/500').json())
print(delete('http://localhost:5000/api/news/4').json())
