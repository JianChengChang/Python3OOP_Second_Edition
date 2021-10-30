from stats import StatsList
import unittest

class TestValidInputs(unittest.TestCase):
    def setUp(self) -> None:
        '''測試初始化'''
        self.stats = StatsList([1,2,2,3,3,4])
    
    def test_mean(self):
        '''測試平均值是否等於 2.5'''
        self.assertEqual(self.stats.mean(), 2.5)
    
    def test_median(self):
        '''測試中位數是否等於 2.5 增加 4 之後是否等於 3'''
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)
    
    def test_mode(self):
        '''測試眾數是否為 [2,3], 移除一個2後, 眾數是否為 [3]'''
        self.assertEqual(self.stats.mode(), [2,3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])

if __name__ == "__main__":
    unittest.main()