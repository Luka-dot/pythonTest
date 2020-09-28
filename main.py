from functools import reduce

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1,2,3])))

my_list = [1, 2, 3, 4, 5, 6, 7]
your_list = [10, 11, 12, 13]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list)))

def acumulator(accumultate, item):
    return accumultate + item

print(reduce(acumulator, my_list, 100))