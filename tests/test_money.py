from src import money
import unittest


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        # Dollar クラスの変数を宣言
        five = money.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertTrue(
            money.Dollar(5).equals(money.Dollar(5))
        )
        self.assertFalse(
            money.Dollar(5).equals(money.Dollar(6))
        )


if __name__ == '__main__':
    unittest.main()
