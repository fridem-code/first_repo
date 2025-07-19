from numpy import median, mean
def parse_input(input_data)->list:
    
    if not input_data.strip():
        raise ValueError("Ввод не должен быть пустым.")
    try:
        input_list = list(int(num) for num in input_data.split(' '))
    except ValueError:
        raise ValueError("Ошибка ввода. Вводить можно только целые числа.")
    return input_list


def classify_numbers(lst:list)->dict:
    group = {
        'Чётные': [],
        'Нечётные': [],
        'Отрицательные': []
    }

    for num in lst:
        if num < 0:
            group['Отрицательные'].append(num)
        elif num % 2 == 0:
            group['Чётные'].append(num)
        else:
            group['Нечётные'].append(num)
    
    return group


def print_stats(name, numbers):
    print(f'\n{name} числа ({len(numbers)}): {numbers}')
    if numbers:
        print(f'Минимальное: {min(numbers)}')
        print(f'Максимальное: {max(numbers)}')
        print(f'Среднее: {mean(numbers)}')
        print(f'Медиана: {median(numbers)}')
    else:
        print('Нет данных для отображения')



if __name__ == '__main__':
    try:
        # input_data = input("Введите список чисел: ")
        input_data = '5 -2 0 8 -7 9'
        lst = parse_input(input_data)
        result = classify_numbers(lst)

        # for name, numbers in result.items():
        #     print_stats(name, numbers)

        assert result['Чётные'] == [0, 8]
        assert result['Нечётные'] == [5, 9]
        assert result['Отрицательные'] == [-2, -7]

    except ValueError as e:
        print(e)