import csv


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
            record = {
                'id': row[0],
                'account': row[1],
                'purchased_quantity': row[2],
                'item_name': row[3],
                'item_quantity': row[4],
                'item_unit': row[5],
                'item_price': row[6],
                'category': row[7],
            }
            data.append(record)

    return data
