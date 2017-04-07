import random

random_numbers = [random.randint(0,49) for num in range(20)]
print(random_numbers)

squared_list = [num ** 2 for num in random_numbers]
print(squared_list)