import unittest
from ex_49.lexicon import lexicon

class TestBasicFunction(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

class Testex_49(unittest.TestCase):
    def test_directions(self):
        self.assertEqual(lexicon.scan("north"), [('direction', 'north')])

if __name__ == '__main__':
    unittest.main()
