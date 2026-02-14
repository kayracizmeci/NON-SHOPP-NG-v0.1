import time

# Fruit Class
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Fruit Dictionary for easy access.
fruits_menu = {
    'a': Fruit('Banana', 20),
    'b': Fruit('Dragon Fruit', 25),
    'c': Fruit('Peach', 15),
    'd': Fruit('Orange', 20),
    'e': Fruit('Strawberry', 30)
}

total = 0
basket = []
balance = 100

print('Welcome to NON-SHOPPING!')

while True:
    print(f'\nCurrent balance: {balance}')
    for key, fruits in fruits_menu.items(): # For not typing new fruits every time to the print.
        print(f'{key}: {fruits.name} Price: {fruits.price}')

    choice = input('Which fruit? (a/b/c/d/e): ')

    while choice not in fruits_menu:
        print('\nInvalid choice! Please answer with a/b/c/d/e.')
        choice = input('Which fruit? (a/b/c/d/e): ').lower()

    fruit = fruits_menu[choice]

    if balance > fruit.price or balance == fruit.price:
        basket.append(fruit.name)
        balance -= fruit.price
        total += fruit.price
        print(f'Added {fruit.name} to basket.')
    else:
        print('\nInsufficient balance!')

    print(f'Your Basket: {basket}')
    print(f'Total spent: {total}')

    while True:
        leave_choice = input('\nAdd another fruit? (y/n): ').lower()
        if leave_choice == 'y':
            break
        elif leave_choice == 'n':
            print('\n--- Final Result ---')
            print(f'Basket: {basket} Score: {len(basket) * balance}')
            time.sleep(1)
            print('Shutting down...')
            time.sleep(2)
            exit()
        else:
            print('Invalid choice! Please answer with y/n.')












