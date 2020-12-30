import csv


class PurchasedItem(object):

    counter = 0

    def __init__(
            self,
            id,
            account,
            purchased_quantity,
            name,
            quantity,
            unit,
            price,
            category
    ):
        PurchasedItem.counter += 1
        self.id = id
        self.account = account
        self.purchased_quantity = purchased_quantity
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price = price
        self.category = category

    def subtotal(self):
        return self.purchased_quantity * self.price

    def change_price(self, price):
        self.price = price


def shopping_cost(filename):
    """
    Compute the total of shopping details stored in a csv file
    with id, account, purchased_quantity, item_name, item_quantity,
    item_unit, item_price, category
    :param filename: string, the name of the file
    :return: tuple, account, total and total_items
    """
    data = []
    with open(filename, "r") as f:
        rows = csv.reader(f)
        next(f)
        for i, row in enumerate(rows):
            row[2] = int(row[2])
            row[6] = float(row[6])
            item = PurchasedItem(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )
            data.append(item)

    return data
