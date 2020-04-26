import unittest

from src.money import Money
from src.money import Bank

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(
            Money.dollar(5).equals(Money.dollar(5))
        )
        self.assertFalse(
            Money.dollar(5).equals(Money.dollar(6))
        )
        self.assertFalse(
            Money.franc(5).equals(Money.dollar(5))
        )

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        my_sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(my_sum, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

if __name__ == '__main__':
    unittest.main()
