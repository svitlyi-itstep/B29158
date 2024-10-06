import requests

response = requests.get("https://www.whenisthenextmcufilm.com/api")
if response.ok:
    film = response.json()
    print(film)

    print('\n\nWhen is the next MCU film?')
    print(f"{film['title']} releases in {film['days_until']} days!")
    print(film['overview'])
    print(f"Release Date: {film['release_date']}")
    print(f"Production Type: {film['type']}")
    print(f"What`s afterwards? {film['following_production']['title']}")
else:
    print(f'{response.status_code}')
    