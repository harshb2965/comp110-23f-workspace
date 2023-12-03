"""Working with csv data."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_val(table: list[dict[str, str]], header: str) -> list[str]:
    """Return values in a table of columns under a specific header."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result