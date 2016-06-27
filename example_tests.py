import unittest

class ExampleTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_fizzes(self):
        result = (%3)
        self.assertEqual(6, result)


if __name__ == "__main__":
    unittest.main()