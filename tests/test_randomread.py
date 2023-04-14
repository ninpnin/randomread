from randomread import sample
import unittest

class Test(unittest.TestCase):

    def test_small(self):
        text = sample("tests/data.txt", 10)
        self.assertEqual(len(text.split()), 10)

    def test_large(self):
        text = sample("tests/data.txt", 1009, chunk_size=1111)
        self.assertEqual(len(text.split()), 1009)

    def test_different(self):
        text1 = sample("tests/data.txt", 100, chunk_size=100)
        text2 = sample("tests/data.txt", 100, chunk_size=100)
        self.assertNotEqual(text1, text2)


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
