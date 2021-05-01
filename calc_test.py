import unittest
import calc


class test_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 4), 7)
        #self.assertNotEqual(calc.add(4, 5),9)

    def test_sub(self):
        self.assertEqual(calc.sub(3, 4), -1)
        #self.assertNotEqual(calc.sub(123123, 123), 0)

    def test_mult(self):
        self.assertEqual(calc.mult(3, 8), 24)
        #self.assertNotEqual(calc.mult(4, 4), 16)

    def test_div(self):
        self.assertEqual(calc.div(12, 3), 4)
        #self.assertNotEqual(calc.div(14, 2), 4) 


if __name__ == '__main__':
    unittest.main()
