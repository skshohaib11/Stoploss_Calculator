
class Trade_checkpoints:
    def __init__(self, Buy_Price, Quantity):
        self.Buy_Price = Buy_Price
        self.Quantity = Quantity
        self.invested_amount = self.Buy_Price * self.Quantity

    def loss_details(self):
        points = [5, 10, 15, 20, 25, 30]
        for i in points:
            stop_loss = self.Buy_Price - i
            target = self.Buy_Price + 30
            loss_percentage = round(((i / self.Buy_Price) * 100), 2)
            loss_amount = round((loss_percentage / 100) * self.invested_amount)
            print(f"Points: {i} -----> Target: {target} -----> stop loss: {stop_loss} -----> Loss Percentage: {loss_percentage} -----> Loss Amount: {loss_amount}")

    def amount_invested(self):
        print(f"Amount Invested = {self.invested_amount}")
        

trade = Trade_checkpoints(307, 30)
trade.amount_invested()
trade.loss_details()