import unittest
import main



class TestSumTask(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(main.sum(1,2), 3)
        
if __name__ == '__main__':
    unittest.main()