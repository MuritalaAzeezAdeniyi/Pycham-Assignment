import random

numbers_list = []
for _ in range(10):
    numbers = random.randint(1, 50)

    numbers_list.append(numbers)

print(numbers_list)


def find_length(numbers_list):
    count = 0
    for _ in numbers_list:
        count += 1

    return count


def sum_elements_at_even_positions(numbers_list):
    index = 0
    sum_even_positions = 0

    for index in range(0, len(numbers_list), 2):
        sum_even_positions += numbers_list[index]

    return sum_even_positions


def sum_elements_at_odd_positions(numbers_list):
    index = 0
    sum_odd_positions = 0

    for index in range(0, len(numbers_list), 2):
        sum_odd_positions += numbers_list[index]

    return sum_odd_positions


def multiply_elements_at_every_third_positions(numbers_list):
    index = 0
    multiply_elements = 0

    for index in range(0, len(numbers_list), 3):
        multiply_elements *= numbers_list[index]

    return multiply_elements


def average(numbers_list):
    sum_of_numbers = 0

    for index in range(len(numbers_list)):
        sum_of_numbers += numbers_list[index]

    average = sum_of_numbers / len(numbers_list)

    return average


def largest(numbers_list):
    max = numbers_list[0]

    for index in range(len(numbers_list)):

        if numbers_list[index] > max:
            max = numbers_list[index]

    return max


def smallest(numbers_list):
    min = numbers_list[0]

    for index in range(len(numbers_list)):

        if numbers_list[index] > min:

            min = numbers_list[index]
    return min

myList = [2, 8, 9, 7, 8, 3, 4, 6, 10, 11]
sum = 0
for even in myList:
    if even % 2 == 0:
        sum +=even
print(sum)

