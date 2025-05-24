class Inventory:
    def __init__(self, product_name: str, opening_stock: int = 0):
        self.product_name = product_name
        self.opening_stock = opening_stock
        self.total_bought = 0
        self.total_sold = 0

    def add_stock(self, quantity: int):
        if quantity < 0:
            print("Quantity bought cannot be negative.")
            return
        self.total_bought += quantity

    def sell_stock(self, quantity: int):
        if quantity < 0:
            print("Quantity sold cannot be negative.")
            return
        if quantity > self.available_stock():
            print(f"Insufficient stock available. Only {self.available_stock()} items in stock.")
            return
        self.total_sold += quantity

    def available_stock(self):
        return self.opening_stock + self.total_bought - self.total_sold

    def __str__(self):
        return (
            f"Inventory Summary\n"
            f"------------------\n"
            f"Product Name     : {self.product_name}\n"
            f"Opening Stock    : {self.opening_stock}\n"
            f"Total Bought     : {self.total_bought}\n"
            f"Total Sold       : {self.total_sold}\n"
            f"Available Stock  : {self.available_stock()}"
        )


if __name__ == "__main__":
    item = Inventory("Harpic", 50)
    item.add_stock(150)
    item.sell_stock(600)

    print(item)
