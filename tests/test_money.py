from src import money
import unittest


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        # Dollar クラスの変数を宣言
        five = money.Dollar(5)
        self.assertEqual(money.Dollar(10), five.times(2))
        self.assertEqual(money.Dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(
            money.Dollar(5).equals(money.Dollar(5))
        )
        self.assertFalse(
            money.Dollar(5).equals(money.Dollar(6))
        )
        self.assertTrue(
            money.Franc(5).equals(money.Franc(5))
        )
        self.assertFalse(
            money.Franc(5).equals(money.Franc(6))
        )
        self.assertFalse(
            money.Franc(5).equals(money.Dollar(5))
        )

    def test_franc_multiplication(self):
        # Franc クラスの変数を宣言
        five = money.Franc(5)
        self.assertEqual(money.Franc(10), five.times(2))
        self.assertEqual(money.Franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
