import unittest

from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase):
    def test_en2fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_fr2en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()