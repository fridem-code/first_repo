from numpy import mean
input_list = list(int(num) for num in input('Введите список чисел: ').split(' '))

print(f'Максимум: {max(input_list)}')
print(f'Минимум: {min(input_list)}')
print(f'Среднее: {round(mean(input_list), 2)}')
print(f'Числа больше среднего: {[i for i in input_list if i > mean(input_list)]}')