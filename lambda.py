def square(a1):
    result = a1**3
    return result
my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

