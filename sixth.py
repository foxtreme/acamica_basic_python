import csv


def shopping_cost(filename):
    """
    Compute the total of shopping details stored in a csv file
    with id, account, purchased_quantity, item_name, item_quantity,
    item_unit, item_price, category
    :param filename: string, the name of the file
    :return: tuple, account, total and total_items
    """
    account = None
    total = 0.0
    total_items = 0

    show_failure = lambda i, err, row: print(i, "reason: ", err, "\n--- row: ", row, end="\n\n")
    with open(filename, "r") as f:
        rows = csv.reader(f)
        next(f)
        for i, row in enumerate(rows):
            try:
                row[2] = int(row[2])
            except ValueError as err:
                show_failure(i, err, row)
                continue
            try:
                row[6] = float(row[6])
            except ValueError as err:
                show_failure(i, err, row)
                continue
            if account is None:
                account = row[1]
            total_items += row[2]
            total += row[2] * row[6]

    return account, total, total_items
