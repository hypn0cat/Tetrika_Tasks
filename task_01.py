"""
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то
количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

Какова сложность вашего алгоритма?
O(N)
"""
import unittest


def first_zero(a):
    try:
        return a.index('0')
        # return a.find('0')  # 2-й вариант
        # return [i for i in range(len(a)) if a[i] == '0'][0]  # 3-й вариант
    except ValueError as e:
        return "Error: " + str(e)


class FirstZeroTest(unittest.TestCase):
    def test_first_zero(self):
        s1 = '00000001'
        s2 = '10000000'
        s3 = '11000000'
        s4 = '111111111111111111111111100000000'
        self.assertEqual(first_zero(s1),  0, 'wrong answer')
        self.assertEqual(first_zero(s2),  1, 'wrong answer')
        self.assertEqual(first_zero(s3),  2, 'wrong answer')
        self.assertEqual(first_zero(s4), 25, 'wrong answer')
        print('Test passed')


if __name__ == '__main__':
    unittest.main()


