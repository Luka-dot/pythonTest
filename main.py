class SuperList(list):
  def __len__(self):
    return 1000

super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Yoyo',
        'has_pets': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)   #connects to supercalss
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left {self.num_arrows}')

wizard1 = Wizard('Moje', 44, 'moje@gm.com')
print(wizard1.email)

"""

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

#3 Instantiate the Pet class with all your cats
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left {self.num_arrows}')


archer1 = Archer('Tonda', 7)
wizard1 = Wizard('Rincewind', -1)
print(archer1.attack())
print(isinstance(archer1, Archer))
print(isinstance(archer1, User))

def player_attack(char):
    char.attack()

player_attack(wizard1)


class PlayerCharacter:
    # class object attribute
    membership = True
    def __init__(self, name='anonimus', age=0):
     #   if (age >= 18):
            self.name = name
            self.age = age
    #    else:
     #       print('You are not old enough')

    @classmethod
    def adding_things(clscls, num1, num2):
        return num1 + num2

    def shout(self):
        if (self.age >= 18):
            print(f' My Name Is {self.name}')
        else:
            print(f'Im {self.name}, but im to yong!')
        return

    def magic_eight(self):
        return 8

    def specialAbility(self):
        attack = 55
        return attack

player1 = PlayerCharacter("Morti")
player2 = PlayerCharacter("Nori", 23)

print(player2.adding_things(5,5))
# @classmetod can be called even without creating class copy
print(PlayerCharacter.adding_things(3, 30))

print(player2.name)
player1.shout()
# print(player1.magic_eight())
# print(player2.specialAbility())


#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Fluffy', 4)
cat2 = Cat('Bella', 3)
cat3 = Cat('Moon', 6)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")




def highest_even_number(list):
    highest_number = 0
    for number in list:
        if (number % 2 == 0) and number > highest_number:
            highest_number = number
    return highest_number


print(highest_even_number([10, 2, 3, 4, 5, 0, 11]))


# Scope - what variables do I have access to?

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()



def checkDriverAge(age=0):
#    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(18)

#   *args, **kwargs-> key words arguments

def super_func(*args, **kwargs):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

def super_func2(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func2(1,2,3,4,5, num1=5, num2=10))


def say_hello(name='Darth Vader', emoji='\U0001f600'):
    print(f'Hello {name}  {emoji}')

say_hello('Me')

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for a in picture:
    line = ''
    for symbol in a:
        if symbol == 0:
            line = line + ' '
        elif symbol == 1:
            line = line + '*'
    print(line)
    line = ''

for row in picture:
    for pixel in row:
        if (pixel ==1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
for line in picture:
    while i < len(line):
        if line[i] == 0:
            print('.')
            i += 1
        elif line[i] == 1:
            print('*')
            i += 1

"""

"""

for i, char in enumerate('Hellooo'):
    print(i, char)

for a, char in enumerate(list(range(100))):
   if char == 50:
       print(a, " : ", char)

my_list = [1,2,3,4,5,6,7,8,9,10]

sum= 0

for item in my_list:
    sum = sum + item

print(sum)



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
