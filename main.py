#########  DECORATORS   ################

my_list = []

my_list2 = [char for char in 'hello']

my_list3 = [number for number in range(0, 100)]

my_list4 = [number**2 for number in range(0, 100) if number %2 == 0]

print(my_list2)
print(my_list4)
# same as below function but using decorators
for char in 'hello':
    my_list.append(char)

print(my_list)
#   set is same as List just change brackets
my_list2set = {char for char in 'hello'}

simple_dic = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k,v in simple_dic.items()
           if v%2==0}
print(my_dict)

my_t = {num:num*2 for num in [1,2,3]}
print(my_t)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


duplicates2= set([x for x in some_list if some_list.count(x) > 1])
print(f'duplicates2 :', duplicates2)

'''


#####  LAMBDA functions
from functools import reduce

my_list = [1,2,3,4,5]

print(list(map(lambda item: item*2, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))

another_list = [5,4,3]

print(list(map(lambda  item: item*item, another_list)))

# list sorting by 2nd item
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda number: number[1])
print(a)

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalized(item):
    return item.upper()

print(list(map(capitalized, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers[::-1])))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score_above50(item):
    return item > 50

print(list(filter(score_above50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def acumulator(accumultate, item):
    return accumultate + item

print(reduce(acumulator, (scores + my_numbers), 0))



def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1,2,3])))

my_list = [1, 2, 3, 4, 5, 6, 7]
your_list = [10, 11, 12, 13]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list)))



# first arg is function, 2nd are data, 3rd is starting value. If not defind starts from 0
print(reduce(acumulator, my_list, 100))

'''