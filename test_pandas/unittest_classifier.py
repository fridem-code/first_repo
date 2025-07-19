import unittest
from test_3 import classify_numbers

class TestClassifier(unittest.TestCase):
    
    def test_classify_numbers_basic(self):
        data = [5, -2, 0, 8, -7, 9]
        result = classify_numbers(data)

        self.assertEqual(result['Чётные'], [0, 8])
        self.assertEqual(result['Нечётные'], [5, 9])
        self.assertEqual(result['Отрицательные'], [-2, -7])

    def test_classify_numbers_empty(self):
        result = classify_numbers([])
        self.assertEqual(result['Чётные'], [])
        self.assertEqual(result['Нечётные'], [])
        self.assertEqual(result['Отрицательные'], [])


if __name__ == '__main__':
    unittest.main()
