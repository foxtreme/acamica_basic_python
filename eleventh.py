import sys
from abc import ABC, abstractmethod


def print_table(objects, attributes_names, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Formatter must be a TableFormatter")
    formatter.headings(attributes_names)
    for obj in objects:
        row_values = [str(getattr(obj, attr_name)) for attr_name in attributes_names]
        formatter.row(row_values)


class TableFormatter(ABC):

    def __init__(self, outfile=None):
        if outfile is None:
            outfile = sys.stdout
        self.outfile = outfile

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, row_values):
        pass


class TextTableFormatter(TableFormatter):

    def __init__(self, width=10):
        self.width = width

    def headings(self, headers):
        for header in headers:
            print("{:>{}s}".format(header, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)

    def row(self, row_values):
        for value in row_values:
            print(":>{}s".format(value, self.width), end=" ", file=self.outfile)


class CSVTableFormatter(TableFormatter):

    def headings(self, headers):
        print(",".join(headers))

    def row(self, row_values):
        print(",".join(row_values))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="", file=self.outfile)
        for header in headers:
            print("<th>{}</th>".format(header), end="", file=self.outfile)
        print("</tr>", file=self.outfile)

    def row(self, row_values):
        print("<tr>", end="")
        for value in row_values:
            print("<td>{}</td>".format(value), end="", file=self.outfile)
        print("</tr>", file=self.outfile)


class CustomTableFormatter(object):
    pass


class AnotherTableFormatter(TableFormatter):
    pass
