from test_3 import classify_numbers, parse_input

data = '5 -2 0 8 -7 9'
data = parse_input(data)
result = classify_numbers(data)
assert result['Чётные'] == [0, 8]
assert result['Нечётные'] == [5, 9]
assert result['Отрицательные'] == [-2, -7]

data = []
result = classify_numbers(data)
assert result['Чётные'] == []
assert result['Нечётные'] == []
assert result['Отрицательные'] == []

data = [3, 5, 2, 1, 7, -5, -4, 9]
result = classify_numbers(data)
assert result['Чётные'] == [2]
assert result['Нечётные'] == [3, 5, 1, 7, 9]
assert result['Отрицательные'] == [-5, -4]