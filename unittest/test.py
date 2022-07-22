import unittest
import main

class TestMain(unittest.TestCase):

    def test1(self):
        test = 4
        answer = 4
        result = main.guess(test, answer)
        self.assertTrue(result)

    def test2(self):
        result = main.guess(9, 4)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
