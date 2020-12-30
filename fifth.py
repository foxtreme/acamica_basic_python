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

    with open(filename, "r") as f:
        rows = csv.reader(f)
        next(f)
        for i, row in enumerate(rows):
            row[2] = int(row[2])
            row[6] = float(row[6])

            if account is None:
                account = row[1]
            total_items += row[2]
            total += row[2] * row[6]
    return account, total, total_items


def add_numbers(*numbers):
    """
    Returns the sum of numbers
    :param numbers: list of numbers
    :return: int, the sum of numbers
    """
    result = 0
    for number in numbers:
        result += number
    return result


def func(**kwargs):
    print(kwargs)


def func_2(*args, **kwargs):
    print(args)
    print(kwargs)
