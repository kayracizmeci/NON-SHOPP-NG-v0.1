

import time

print('--*NON-SHOPPİNG*--')

time.sleep(2)

shopping_list = []
test_list = []
print('SYSTEM:We need to run a quick test on our systems.')

test_item = input('Please add apple to your shopping list. ')

test_item = test_item.lower()

if test_item == 'apple':
    print('No mistakes typing apple.')
else:
    print('Please type apple correctly next time!')

time.sleep(3)

test_list.append(test_item)

print('shopping list:', test_list)

test_list.clear()

print(test_list)

time.sleep(2)

print('Tests are finished with 0 mistakes.')

print('--*NON-SHOPPİNG*--')

print('BALANCE:100')

balance = 100

first_purchase = input('Please sellect the fruit that you gonna buy first. Price and list of things you can buy:BANANA:15 MN CHERRY:10 MN APPLE:20 MN ORANGE:20 MN CUCUMBER 20 MN POTATO MN 50').upper()

if first_purchase == "BANANA":
    price = 15
elif first_purchase == "CHERRY":
    price = 10
elif first_purchase == "APPLE":
    price = 20
elif first_purchase == "ORANGE":
    price = 20
elif first_purchase == "CUCUMBER":
    price = 20
elif first_purchase == "POTATO":
    price = 50
else:
    print("Invalid item!")
    price = 0

if price > 0:
    balance -= price
    print("Purchase successful. New balance:", balance)


















