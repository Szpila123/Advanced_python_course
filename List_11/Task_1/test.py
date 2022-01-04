import unittest
import math

import sqrt
import cryptarithm


class TestCryptharithm(unittest.TestCase):

    correct = [
        ('send', 'more', 'money'),
        ('abcd', 'efgb', 'efcbh'),
        ('number', 'number', 'puzzle'),
        ('coca', 'cola', 'oasis')
    ]

    invalid_input = [
        ('sadf', 'lkjh', 'zxcv'),
        ('123', 'asdf', 'asdf'),
        ('#!,', 'sadf', 'sdfa'),
        ('dsf', 'asd', '')
    ]

    no_solution = [
        ('asd', 'asd', 'asd'),
        ('mother', 'father', 'child'),
        ('three', 'three', 'one')
    ]

    def test_correct(self):
        """Checks if function resolves cryptharithms correctly"""
        for words in self.correct:
            with self.subTest(words=words):
                mapping = cryptarithm.solve_cryptarithm(*words)

                sum_words = sum(self.map_str_to_int(words[i], mapping) for i in range(2))
                sum_result = self.map_str_to_int(words[2], mapping)

                self.assertEqual(sum_words, sum_result)

    def map_str_to_int(self, word: str, mapping: dict[str, int]) -> int:
        '''Change word to number accoring to mapping'''
        return int(''.join([str(mapping[x]) for x in word]))

    def test_invalid_input(self):
        """Checks if invalid input will be recognized"""
        for words in self.invalid_input:
            with self.subTest(words=words):
                self.assertFalse(cryptarithm.check_input(*words), 'Input should be invalid')

    def test_nosolution(self):
        """Checks if cryptharitms with no soulution return empty mapping"""
        for words in self.no_solution:
            with self.subTest(words=words):
                self.assertEqual(cryptarithm.solve_cryptarithm(*words), {}, 'There should be no solution')


class TestSquareRoot(unittest.TestCase):

    correct_int = range(100)
    correct_float = [0.5, 1.55, 2.33, 1.44, 10.33]
    incorrect = range(-1, -10)

    def test_correct_int(self):
        """Checks if square root is counted for integers"""
        for number in self.correct_int:
            with self.subTest(number=number):
                self.assertEqual(sqrt.sqrt(number), math.floor(math.sqrt(number)), 'Result invalid')

    def test_correct_float(self):
        """Checks if square root is counted for floats"""
        for number in self.correct_float:
            with self.subTest(number=number):
                self.assertEqual(sqrt.sqrt(number), math.floor(math.sqrt(number)), 'Result invalid')

    def test_invalid(self):
        """Checks if on invalid input error is raised"""
        for number in self.incorrect:
            with self.subTest(number=number):
                self.assertRaises(ArithmeticError, sqrt.sqrt, number)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCryptharithm('test_correct'))
    suite.addTest(TestCryptharithm('test_invalid_input'))
    suite.addTest(TestCryptharithm('test_nosolution'))
    suite.addTest(TestSquareRoot('test_correct_int'))
    suite.addTest(TestSquareRoot('test_correct_float'))
    suite.addTest(TestSquareRoot('test_invalid'))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=3).run(suite())
