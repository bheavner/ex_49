from unittest import TestCase
from ex_49.lexicon import scan

class TestBasicFunction(TestCase):
    def test(self):
        self.assertTrue(True)

class Testex_49(TestCase):
    def test_directions(self):
        self.assertEqual(scan("north"), [('direction', 'north')])

if __name__ == '__main__':
    unittest.main()
