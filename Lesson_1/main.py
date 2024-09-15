print('Hello world!')
while True:
    a = input('Введіть повідомлення: ')
    if not a:
        print('Ви нічого не ввели!')
    else:
        print('Ви ввели:', a)
        break

while True:
    age = input('Введіть свій вік: ')

    if not age:
        print('Ви нічого не ввели!')
    else:
        if int(age) < 18:
            print('Неповнолітній')
        else:
            print('Повнолітній')
        break


print("HELLO WORLD!")