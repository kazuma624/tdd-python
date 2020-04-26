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
        self.assertFalse(
            money.Money.franc(5).equals(money.Money.dollar(5))
        )

    def test_currency(self):
        self.assertEqual('USD', money.Money.dollar(1).currency())
        self.assertEqual('CHF', money.Money.franc(1).currency())


if __name__ == '__main__':
    unittest.main()
