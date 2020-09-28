def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, [1,2,3])))

my_list = [1, 2, 3, 4, 5, 6, 7]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))