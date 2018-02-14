
import unittest

class SampleTest(unittest.TestCase):

    def test_example(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()



