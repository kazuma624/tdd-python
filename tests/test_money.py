import unittest

from src.money import (
    Bank,
    Money,
    Sum,
)


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(5) == Money.dollar(5))

    def test_currency(self):
        self.assertEqual('USD', Money.dollar(1).currency())
        self.assertEqual('CHF', Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        my_sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(my_sum, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        my_sum = result
        self.assertEqual(five, my_sum.augend)
        self.assertEqual(five, my_sum.addend)

    def test_reduce_sum(self):
        my_sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(my_sum, 'USD')
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate('USD', 'USD'))

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        self.assertEqual(Money.dollar(10), result)


if __name__ == '__main__':
    unittest.main()
