from unittest import TestCase
#from ex_49.lexicon import scan
from ex_49 import lexicon

class TestTests(TestCase):
    def test_tests(self):
        self.assertTrue(True)

class Testex_49(TestCase):
    def test_directions(self):
        self.assertEqual(lexicon.scan('north'), [('direction', 'north')])

        result = lexicon.scan('north south east')
        self.assertEqual(result, [('direction', 'north'),
                                  ('direction', 'south'),
                                  ('direction', 'east')])

    def test_verbs(self):
        self.assertEqual(lexicon.scan('go'), [('verb', 'go')])

        result = lexicon.scan('go kill eat')
        self.assertEqual(result, [('verb', 'go'),
                                  ('verb', 'kill'),
                                  ('verb', 'eat')])

    def test_stops(self):
        self.assertEqual(lexicon.scan('the'), [('stop', 'the')])

        result = lexicon.scan('the in of')
        self.assertEqual(result, [('stop', 'the'),
                                  ('stop', 'in'),
                                  ('stop', 'of')])

    def test_nounts(self):
        self.assertEqual(lexicon.scan('bear'), [('noun', 'bear')])


if __name__ == '__main__':
    unittest.main()
