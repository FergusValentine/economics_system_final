class Wallet:
    def __init__(self, money: float):
        self.money: float = money

    def add_money(self, money):
        self.money = max(self.money + money, 0)

    def get_money(self) -> float:
        return self.money