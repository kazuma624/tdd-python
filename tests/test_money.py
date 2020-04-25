from src import money
import unittest


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        # Dollar クラスの宣言
        five = money.Dollar(5)
        # times メソッドの使用
        five.times(2)
        # 結果は 10 に等しいはず
        self.assertEqual(10, five.amount)


if __name__ == '__main__':
    unittest.main()
