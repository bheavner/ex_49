from unittest import TestCase
#from ex_49.lexicon import scan
from ex_49 import lexicon

class TestBasicFunction(TestCase):
    def test(self):
        self.assertTrue(True)

class Testex_49(TestCase):
    def test_directions(self):
        self.assertEqual(lexicon.scan("north"), [('direction', 'north')])
        result = lexicon.scan("north south east")
        self.assertEqual(result, [('direction', 'north'),
                                  ('direction', 'south'),
                                  ('direction', 'east')])

if __name__ == '__main__':
    unittest.main()
