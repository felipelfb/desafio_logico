import unittest
from count_chars import count_running_letters, number_of_characters

class CountTestCase(unittest.TestCase):

    def test_running_letters(self):
        result1 = '5a4b6c7a'
        result2 = '12a'
        result3 = '1f1e1l1i1p1e'

        self.assertEqual(
            count_running_letters('aaaaabbbbccccccaaaaaaa'), result1
            )
        self.assertEqual(
            count_running_letters('aaaaaaaaaaaa'), result2
        )
        self.assertEqual(
            count_running_letters('felipe'), result3
        )
    
    def test_number_of_characters(self):
        phrase1 = 'teste conaz'
        phrase2 = 'The quick brown fox jumps over the lazy dog'

        result1 = number_of_characters(phrase1)
        result2 = number_of_characters(phrase2)

        self.assertEqual(result1['e'], 2)
        self.assertEqual(result1[' '], 1)
        self.assertEqual(result1['t'], 2)
        self.assertEqual(result1['a'], 1)

        self.assertEqual(result2['o'], 4)
        self.assertEqual(result2['u'], 2)
        self.assertEqual(result2['e'], 3)

if __name__ == '__main__':
    unittest.main()
