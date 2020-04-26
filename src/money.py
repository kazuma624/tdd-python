from abc import ABCMeta
from abc import abstractmethod

class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency

    def equals(self, obj):
        return (
            self._amount == obj._amount
            and type(self) == type(obj)
        )

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')

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


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
