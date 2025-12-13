# get user input 3D matrix
def get_matrix():
    try:
        matrix_3d = []
        print("Enter the numbers in a single line (separated by space): ")
        for _ in range(3):
            row = list(map(int, input().split()))
            if len(row) != 3:
                raise ValueError("Each row must have exactly 3 numbers.")
            matrix_3d.append(row)
        return sum_rows_col(matrix_3d)
    except Exception as e:
        print(f"Error: {e}")

#Sum of the values ​​in each column and row
def sum_rows_col(matrix_3d):
    try:
        print("Row sums:")
        row_count = 0
        for rows in matrix_3d:
            sum_row = sum(rows)
            row_count += 1
            print(f"Row {row_count}: {sum_row}")
        print("Column sums:")
        col_count = 0
        for idx in zip(*matrix_3d):
            col_count += 1
            print(f"Column {col_count}: {sum(idx)}")
    except Exception as e:
        print(f"Error: {e}")

# run the application
if __name__ == "__main__":
    get_matrix()
   