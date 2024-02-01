def generate_pascals_triangle(rows):
    triangle = []

    for i in range(rows):
        row = [1]  # The first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Calculate the elements for the current row
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle


def display_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))


if __name__ == "__main__":
    num_rows = 5  # Replace with the number of rows you want to generate
    pascals_triangle = generate_pascals_triangle(num_rows)
    display_pascals_triangle(pascals_triangle)
