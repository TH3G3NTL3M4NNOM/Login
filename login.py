while True:
    name = input("Enter your name please: ")
    if 'sora' in name:
        print("Access Denied!")
    else:
        print(f'{name}, Welcome to my online store!')
        break

while True:
    try:
        age = int(input(f'{name} Enter your age please: '))
        if age > 100:
            print(f'{name}, You are too old to be here! ')
        elif age < 10:
            print(f'{name}, You are too young to be here! ')
        else:
            print(f'{name}, Please choose an item from the list! ')
            break
    except ValueError:
        print("Enter a number on the input")

products_list = ['apple', 'computer']
print(*products_list)

while True:
    chosen_product = input(f'{name}, Enter a product from the list: ')
    if 'apple' in chosen_product:
        print(f'{name}, This apple could be yours, Give me an address')
        break
    if 'computer' in chosen_product:
        print(f'{name}, This computer could be yours, give me an address')
        break

while True:
    try:
        add = input(f'{name}, Enter an address please: ')
        if 'apple' in chosen_product:
            print(f'{name} This apple is yours! will be delivered to ' + add)
            break
        elif 'computer' in chosen_product:
            print(f'{name}, This computer is yours! will be delivered to ' + add)
            break
    except ValueError:
        print("Enter a valid add")
        