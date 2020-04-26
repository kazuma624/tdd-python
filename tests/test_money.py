from src import money
import unittest


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = money.Money.dollar(5)
        self.assertEqual(money.Money.dollar(10), five.times(2))
        self.assertEqual(money.Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(
            money.Money.dollar(5).equals(money.Money.dollar(5))
        )
        self.assertFalse(
            money.Money.dollar(5).equals(money.Money.dollar(6))
        )
        self.assertTrue(
            money.Money.franc(5).equals(money.Money.franc(5))
        )
        self.assertFalse(
            money.Money.franc(5).equals(money.Money.franc(6))
        )
        self.assertFalse(
            money.Money.franc(5).equals(money.Money.dollar(5))
        )

    def test_franc_multiplication(self):
        five = money.Money.franc(5)
        self.assertEqual(money.Money.franc(10), five.times(2))
        self.assertEqual(money.Money.franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
