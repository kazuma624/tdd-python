from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(to):
        pass


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, to):
        return self

    def currency(self):
        return self._currency

    def equals(self, money):
        return (
            self._amount == money._amount
            and self.currency() == money.currency()
        )

    def __str__(self):
        return self._amount + ' ' + self._currency

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')

    def __eq__(self, obj):
        if not isinstance(obj, Money):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self._amount == obj._amount

    def __lt__(self, obj):
        if not isinstance(obj, Money):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self._amount < obj._amount

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __le__(self, obj):
        return self.__lt__(obj) or self.__eq__(obj)

    def __gt__(self, obj):
        return not self.__le__(obj)

    def __ge__(self, obj):
        return not self.__lt__(obj)


class Bank:
    def reduce(self, source, to):
        return source.reduce(to)


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)
