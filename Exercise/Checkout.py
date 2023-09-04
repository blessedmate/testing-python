class Checkout:
    class Discount:
        def __init__(self, amount, price):
            self.amount = amount
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items_count = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items_count:
            self.items_count[item] += 1
        else:
            self.items_count[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items_count.items():
            # Check if item is in discounts dict
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            # Check if items count is enough for a discount
            if cnt >= discount.amount:
                total += self.calculate_item_total_with_discounts(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculate_item_total_with_discounts(self, item, cnt, discount):
        total = 0
        # Calculate the amount of discounts to apply
        discounts_num = cnt / discount.amount
        total += discounts_num * discount.price
        # Add the remaining items with a full price
        remaining = cnt % discount.amount
        total += remaining * self.prices[item]
        return total

    def add_discount(self, item, amount, price):
        discount = self.Discount(amount, price)
        self.discounts[item] = discount
