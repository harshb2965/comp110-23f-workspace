"""Dictionary related utility functions."""

__author__ = "730649407"

from csv import DictReader

# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    result: list[str] = []
    for row in table:
        result.append(row[key])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for col_name in table[0].keys():
        temp_list: list[str] = column_values(table, col_name)
        result[col_name] = temp_list
    return result

def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    