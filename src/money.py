class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, obj):
        dollar = obj
        # amount 属性の値同士が等しいかどうかを返す
        return self.amount == dollar.amount