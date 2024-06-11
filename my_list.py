import random
def random_number():
    random.seed(3)
    numbers_list = []
    for _ in range(10):
        numbers = random.randint(1, 50)
        numbers_list.append(numbers)
    return numbers_list

print(random_number())
x = random_number()

def find_length(numbers_list):
    count = 0
    for _ in numbers_list:
        count += 1

    return count
print(find_length(x))



def sum_elements_at_even_positions(numbers_list):
    index = 0
    sum_even_positions = 0

    for index in range(0, len(numbers_list), 2):
        sum_even_positions += numbers_list[index]

    return sum_even_positions
    print(sum_elements_at_even_positions(x))

def sum_elements_at_odd_positions(numbers_list):
    index = 0
    sum_odd_positions = 0

    for index in range(0, len(numbers_list), 2):
        if index % 2 != 0:
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
def count_string(number_list):
    num = []
    for element in number_list:
        if len(element) < 2:
            if element[0] == element[len(element)]:
                num = element
    return num

def numbers_of(number):
    list_of_num = [2,3,4,5,6,7,8,9,]
    return list_of_num
    print(list_of_num)

def duplication_number(num):
    duplicate_list = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    print(f"the duplication list is{duplicate_list}")

def eliminate():
 my_list = list(set())
print(f" the dublicate eliminate list is{my_list}")

def sum_third_sector(last):
    return sum(last[2::3])
print(sum_third_sector())


def sum_first_middle_and_late(number):
    if len(number) == 1:
        return number[0]
    elif len(number) == 2:
        return sum(number)
    else:
        middle_index = len(number)//2
        if len(number) % 2 == 0:
            middle_index = (number[middle_index -1] + number[middle_index])/2
        else:
            middle_index = number[middle_index]
            return number + middle_index + number[-1]

def convert_list_to_set(num_list):
    num_list = []
    for i in range(10):
       num = int(input("Enter a number: "))
    	num_list.append(num)
          num_set = set(num_list)


def sum_collection(num_set):
    return sum(num_set)

def remove_item(num_set, num):
    if num in num_set:
        num_set.remove(num)
        return num
    else:
        return None

def find_intersection(set1, set2):
    return set1 & set2

def find_union(set1, set2):
    return set1 | set2

def is_subset(set1, set2):
    return set1.issubset(set2)

set1 = {1, 2, 3}
set1.clear()
print(set1)





