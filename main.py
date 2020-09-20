
weather = "It's sunny"
tomorow_weather = "\t its\'s \"kind of\" sunny \n Have a great day!"    # \ assumes char after is string. \t is tab. \n is new line
print(tomorow_weather)

"""

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