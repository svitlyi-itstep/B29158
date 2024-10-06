import requests
import random
page = random.randint(1, 7438)
pageSize = 1
url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
response = requests.get(url)
if response.ok:
    character = response.json()['data']
    print(character)
    print(character['name'])
    for film in character['films']:
        print(film)
else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')