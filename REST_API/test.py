import requests

BASE = 'http://127.0.0.1:5000/'

data = [{'name': 'Flask', 'views': 100,'likes': 150},
        {'name': 'OpenAI', 'views': 10000,'likes': 20000},
        {'name': 'Django', 'views': 1000,'likes': 10000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + 'video/4')
print(response.json())