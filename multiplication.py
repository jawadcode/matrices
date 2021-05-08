def main():
    print("Matrix operations:\n\n")

    height_a = int(input("height of A: "))
    width_a = int(input("width of A: "))

    print(
        "\nPlease input matrix A with the elements separated by spaces and the rows separated by a new line:"
    )

    A = input_matrix(height_a)
    validate_matrix(height_a, width_a, A)

    height_b = int(input("\nheight of B: "))
    width_b = int(input("width of B: "))
    if width_a != height_b:
        print("The width of matrix A must be equal to the height of matrix B")

    print(
        "\nPlease input matrix B the same way:"
    )
    B = input_matrix(height_b)
    validate_matrix(height_b, width_b, B)

    C = multiply(A, B)
    pretty_print_matrices(A, B, C)


def multiply(A, B):
    """
    Use some list comprehension magic to multiply the matrices and get the result
    """
    return [[sum(x * y for x, y in zip(A_row, B_col)) for B_col in zip(*B)]
            for A_row in A]


def input_matrix(height):
    """
    Receive input from the user and parse it into a 2d list
    """
    return [[int(i) for i in input().split(" ")] for _ in range(height)]


def validate_matrix(height, width, matrix):
    """
    Check that the matrix has the correct height and width
    """
    valid = True
    if len(matrix) != height:
        valid = False
    for row in matrix:
        if len(row) != width:
            valid = False

    if valid == False:
        print(f"Supplied matrix was not of order {height}×{width} \n\n")
        exit(1)


def pretty_print_matrices(A, B, C):
    """
    Do some magic to format the 3 matrices
    """
    A_fmt = format_matrix(A)
    B_fmt = format_matrix(B)
    C_fmt = format_matrix(C)
    A_gap = " " * len(A_fmt[0])
    B_gap = " " * len(B_fmt[0])
    A_len = len(A)
    B_len = len(B)
    min_len = min(A_len, B_len)
    middle = min_len // 2
    print("")
    for row in range(min_len):
        mid = "×" if row == middle else " "
        mid_eq = "=" if row == middle else " "
        print(f"{A_fmt[row]}{mid}{B_fmt[row]}{mid_eq}{C_fmt[row]}")

    if A_len > B_len:
        for i in range(B_len, A_len):
            print(f"{A_fmt[i]}  {B_gap}  {C_fmt[i]}")
    elif B_len > A_len:
        for i in range(A_len, B_len):
            print(f"{A_gap}   {B_fmt[i]}")


def format_matrix(matrix):
    """
    Format a matrix into rows of a table (accounting for the width of elements)
    """
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = " ".join(f"{{:{x}}}" for x in lens)
    return [" | " + fmt.format(*row) + " | " for row in s]


if __name__ == "__main__":
    main()
