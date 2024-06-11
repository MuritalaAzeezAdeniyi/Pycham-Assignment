def That_take_a_list_and_return(even):
    listnum = []
    for number in range(50):
        listnum.append(number)
        if number % 2 == 0:
                 return even



def even_list(sh):
    for number in sh:
        if number % 2== 0 :
            even_numbers.append(number)
            return even_numbers
        numbers = list(range(1,51))
        print(even_list(number))

def even_list2(numberz):
    return [number for number in numberz if number % 2 == 0]
nums =(range(1,51))
print(nums)
nums = (even_list2(nums))
print(nums)