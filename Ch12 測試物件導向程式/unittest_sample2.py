import unittest

class CheckNumbers(unittest.TestCase):
    def test_int_float(self) -> None:
        self.assertEqual(1, 1.0)
        
    def test_str_float(self) -> None:
        self.assertEqual("1", 1.0)
        
if __name__ == "__main__":
    unittest.main()