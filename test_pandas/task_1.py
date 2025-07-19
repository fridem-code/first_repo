

def sum_of_even(lst:list):
    return sum(num for num in lst if num % 2 == 0)

lst_input = [int(i) for i in (input(' Введите числа через пробел: ').split(' '))]
print(sum_of_even(lst_input))