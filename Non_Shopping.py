import time
# Start
print('Welcome to NON-SHOPPİNG!')

total = 0
basket = []
balance = 100
fruits = {
    'a': 'Banana',
    'b': 'Dragon Fruit',
    'c': 'Peach',
    'd': 'Orange'
}
# Adding fruits to the shopping basket

answer = 'yes'

while answer == 'yes':
    print('\nCurrent balance:', balance)

    choice = input(
        'Wicth fruit do you wanna add to your basket:\n'
        'a: Banana Price:10\n'
        'b: Dragon Fruit Price:25\n'
        'c: Peach Price:15\n'
        'd: Orange Price:20\n'
    ).lower()

    if choice == 'a':
        price = 10
        basket.append('Banana')

    elif choice == 'b':
        price = 25
        basket.append('Dragon Fruit')

    elif choice == 'c':
        price = 15
        basket.append('Peach')

    elif choice == 'd':
        price = 20
        basket.append('Orange')

    else:
        print('Please sellect an answer with a,b,c,d and dont use space bar.')
        print('Closing the program...')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('0')
        exit()

    # End of the purchase + score calculating
    total += price
    balance -= price

    print('Your Basket:', basket)
    print('Total spent:', total)
    print('New balance:', balance)

    answer = input('Do you want to add another fruit? (yes/no) ').lower()

print('\nShopping finished.')
print('Final basket:', basket)
print('Final balance:', balance)

fruit_count = len(basket)
score = fruit_count * balance

print('Fruit count:', fruit_count)
print('Score:', score)







