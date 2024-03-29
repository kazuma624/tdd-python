from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def plus(addend):
        pass

    @abstractmethod
    def reduce(bank, to):
        pass

    @abstractmethod
    def times(multiplier):
        pass


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    def currency(self):
        return self._currency

    def __eq__(self, money):
        """
        Java で equals メソッドをオーバーライドしたことに相当
        演算子 == をオーバーライドする
        """
        if not isinstance(money, Money):
            return NotImplemented
        return (
            self._amount == money._amount
            and self.currency() == money.currency()
        )

    def __str__(self):
        return f'{self._amount} {self._currency}'

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Bank:
    __rates = dict()

    def reduce(self, source, to):
        return source.reduce(self, to)

    def add_rate(self, _from, to, rate):
        self.__rates[Pair(_from, to)] = rate

    def rate(self, _from, to):
        if _from == to:
            return 1

        return self.__rates.get(Pair(_from, to))


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = (self.augend.reduce(bank, to)._amount
                    + self.addend.reduce(bank, to)._amount)
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(
            self.augend.times(multiplier), self.addend.times(multiplier)
        )


class Pair:
    def __init__(self, _from, to):
        self.__from = _from
        self.__to = to

    def __eq__(self, pair):
        """
        Java で equals メソッドをオーバーライドしたことに相当
        演算子 == をオーバーライドする
        """
        if not isinstance(pair, Pair):
            return NotImplemented
        return self.__from == pair.__from and self.__to == pair.__to

    def __hash__(self):
        """
        Java で hashCode メソッドをオーバーライドしたことに相当
        """
        return 0
