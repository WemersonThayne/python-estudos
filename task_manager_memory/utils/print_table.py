


# Extract attributes from objects
# getattr(item, attr):
# The getattr function is a built-in Python function that retrieves the value of an attribute from an object.
# It takes two arguments: the object (item in this case) and the attribute name (attr).
# So, getattr(item, attr) fetches the value of the attribute named attr from the object item
def _extract_attributes(data, attributes):
    return [
        [
            getattr(item, attr) if getattr(item, attr) is not None else ""
            for attr in attributes
        ]
        for item in data
    ]

# Calculate the maximum width of each column
def _calculate_column_widths(data, headers):
    combined = [headers] + data
    widths = [max(len(str(item)) for item in column) for column in zip(*combined)]
    return widths


# Print the table
def print_table(data, headers, attributes):
    # Extract attributes from data objects
    data_rows = _extract_attributes(data, attributes)

    widths = _calculate_column_widths(data_rows, headers)

    row_format = " | ".join(["{{:<{}}}".format(width) for width in widths])

    print(row_format.format(*headers))
    print("-+-".join(['-' * width for width in widths]))

    for row in data_rows:
        print(row_format.format(*row))
