class Dollar:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def equals(self, obj):
        dollar = obj
        # amount 属性の値同士が等しいかどうかを返す
        return self.__amount == dollar.__amount

    def __eq__(self, obj):
        if not isinstance(obj, Dollar):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self.__amount == obj.__amount

    def __lt__(self, obj):
        if not isinstance(obj, Dollar):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self.__amount < obj.__amount

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __le__(self, obj):
        return self.__lt__(obj) or self.__eq__(obj)

    def __gt__(self, obj):
        return not self.__le__(obj)

    def __ge__(self, obj):
        return not self.__lt__(obj)

class Franc:
    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def equals(self, obj):
        franc = obj
        # amount 属性の値同士が等しいかどうかを返す
        return self.__amount == franc.__amount

    def __eq__(self, obj):
        if not isinstance(obj, Franc):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self.__amount == obj.__amount

    def __lt__(self, obj):
        if not isinstance(obj, Franc):
            # 特殊な二項演算のメソッドが他の型に対して演算が実装されていない
            return NotImplemented
        return self.__amount < obj.__amount

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def __le__(self, obj):
        return self.__lt__(obj) or self.__eq__(obj)

    def __gt__(self, obj):
        return not self.__le__(obj)

    def __ge__(self, obj):
        return not self.__lt__(obj)
