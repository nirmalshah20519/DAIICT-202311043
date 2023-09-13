def PascalTriangle(n):
    pascal_triangle = []
    for i in range(n):
        row = [1]
        if pascal_triangle:
            last_row = pascal_triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        pascal_triangle.append(row)
    return pascal_triangle