user = {
    'name': 'Golem',
    'age':  5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)



"""

is_magic = False
is_expert = True

master_magician = "You are master magician" if is_magic and is_expert else "You need more training"
print(master_magician)

if is_magic and is_expert:
    print("You are master magician")
elif is_magic and not is_expert:
    print("You need more training")
elif is_expert and not is_magic:
    print("you NEED to be magic")
else:
    print("you are neither")

def user_input() :
    while True:
        u_input = input('Please input anything: ')
        if len(u_input) > 3:
            break
        print(f'Invalid input: {u_input} must be 4 characters or more')




is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are ok to drive')
else:
    print('You are not allowed!!!!')

# ternary operator in Python
# condition_if_true if  condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend and is_old else "not allowed to message"
print(can_message)



users = [
    {
        'name': "ja",
        'member': True,
        'cart': [1,2,3,4]
    },
    {
        'name': 'Moje',
        'member': False,
        'cart': [0, 'gas', 44, 'toy']
    }
]

print(users[1]['cart'][2])
print(users[0].get('name'))
print('cart' in users[0])
print('Moje' in users[1].values())
print(users[1].items())

users2 = users.copy()

users2[0].pop('member')
print(users2[0])
users2[1].update({'member': True})
print(users2[1])

sentence = ' '
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Lukas'])
another_way = ' '.join(['Hi', 'my', 'name', 'is', 'MOJE'])

print(new_sentence)
print(another_way)

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.append(new_friend[0])
# friends.extend(new_friend)
print(sorted(friends))

a,b,c, *remaining_of_list, h, n = [1,2,3,4,5,6,7,8,9,10]  # unpack 3 variables and remaing stays in "remaining" then last h assing last value
print(a, b, c)
print(remaining_of_list)
print(h)
print(n)


# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
basket.pop()
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
# 5. Count how many apples in the basket
print(basket.count('Apples'))
# 6. empty the basket
basket.clear()
print(basket)


cart = [
    'notebook',
    'glasses',
    'toy',
    'grapes'
]

print(cart[1][0:7:2])

matrix = [
    [1,2,3,4],
    ['a', 'b','c','d'],
    [[11,22,33,]]
]

print(matrix[2][0][2])
new_cart = cart[::] # copy of the cart list
new_cart.insert(2, 'clock')

new_cart.extend([122, 133])

print(new_cart)

#   removing

new_cart.pop()  # removes last item in the list .pop(2) -> removes whatever is on index 2
new_cart.remove(2)  # removes value 2




username = input('enter your username:')
password = input('enter your password:')

print(f'Hello {username}, your password {("*" * len(password))} is {len(password)} letters long. ')

birth_year = input('What year were you born?')
current_age = 2020 - int(birth_year)
print('You are ' + str(current_age) + ' old')

name = '0123456'
name = name + '7'

print(name)

name = "Lukas"
age = 33

print(f' hi {name}. you are {age} years old.')  # f at the beginning means formatted string
print(name[2])
print(name[2:5])
print(name[0:6:2])  # 3rd argument is step-over
print(name[:4])     # starts at 0 and go to 4
print(name[-2])     # go from back
print(name[::-1])   # this way we can iterate through the string backwards



weather = "It's sunny"
tomorow_weather = "\t its\'s \"kind of\" sunny \n Have a great day!"    # \ assumes char after is string. \t is tab. \n is new line
print(tomorow_weather)


long_string = '''
WOW
O O
---

'''
print(long_string)

value = 5
value -= 1
value += 4
value *= 2
print(value)

print(round(5.7589))

print(abs(-55894))

print(bin(723424))

a,b,c = 1,2,3
print(a)
print(c)



numbers = (1, 2, 2, 2, 3, 4, 5, 6.6, 6.9)  #  () is tupple. imutable!!!

numbers.count(2)    #returns 3 = total number of 2s in tupple
print(numbers.index(6.6))   # index on value 6.6




numbers = range(5, 10, 2)   # first argument is start value, 2nd arg is endin value, 3rd arg is step (by 2)
for number in numbers:
    print(number)

for number in range(5):
    print(number)


"

numbers = [1, 2, 3, 4, 5, 6.6, 6.9]
for item in numbers:
    if item % 2 == 0:
        print(item, " is even number")
    else: print('not even number ', item)



numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
numbers.insert(2, 2.5)
print(numbers)
numbers.remove(2.5)
print(4 in numbers)
print(len(numbers))



i = 1
while i <= 3:
    print(i * '*')  # this will print '*' times i
    i = i + 1

names = ["Lukas", "Mark", "Tania", "Sawyer", "Thaina"]
print(names[2])
print(names[-2])    # prints 2nd element from the end of array
names[1] = "Marky Mark"
print(names[1])
print(names[0:3])   # prints names from index 0 to 2 (exludes 3)



weight = int(input('enter your weight: '))
unit_type = input('(K)g or (L)bs: ')

if unit_type.upper() == "K":
    convert = weight / 0.45
    print("your weight in LB is: ", convert)
else:
    convert = weight * 0.45
    print('Your weight in KG is: ', convert)



if kilos_or_not == 0:
    print('your weight is: ', weight , 'kg')
else : print('your weight is: ', weight , 'lbs')




price = 52
print(price > 10 and price < 30)    # if both expressions are true => true
print(price > 10 or price < 30)    # one of the expression is tru => true
print(not price == 25)  # return opposite inverse value

if price > 20:
    print('not a good price')
elif price < 30:    # greter then 20 and lower then 30
    print('it is OK price')
else: print('NOT a good price')



print( 11 % 3)  # displays reminder
print( 11 / 3)  # simple division
print( 11 // 3) # integer
print( 11 * 3)  # multiply
print( 11 ** 3)  # 11 to power of 3

x = 5
x = x + 3
x += 3  # agmented assignment operator this is same as x = x + 3
print(x)




first_name = input('Enter first name: ')
last_name = input('enter your last name: ')
year_born = int(input('enter year you wore born: '))

age = 2020 - year_born

print('welcome ', first_name, last_name, ' you are ', age, ' old')


myString = 'this is my String For Testing'

print(myString.upper())
print(myString.find('i'))
print('My' in myString)
myString = myString.replace('m', 'M')
print('My' in myString)
# print(myString.replace('m', 'M'))
print(myString)


myList = [1,2,3,4,5,6,7]
count = 0
for num in myList:
    count = count + num

print(count)
"""