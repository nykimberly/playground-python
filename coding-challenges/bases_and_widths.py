from typing import List

def beyond_dec(dec_val: int):
    if dec_val > 9:
        idx = dec_val - 9
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[idx - 1]
    return str(dec_val)

def convert(dec_val: int, base: int):
    result = []
    n = dec_val
    while True:
        m = beyond_dec(n % base)
        result.insert(0,m)
        n = int(n / base)
        if n == 1:
            result.insert(0, str(1))
            break
        if n == 0:
            break
    return "".join(result)

def fmt_str(matrix: List[List[int]], max_width: int) -> str:
    matrix_str = ""
    for row_values in matrix:
        if matrix_str:
            row_str = "\n"
        else:
            row_str = ""
        for i, col in enumerate(row_values):
            row_str += " " * (max_width - len(col))
            if i != 0:
                row_str += " "
            row_str += col
        matrix_str += row_str
    return matrix_str

def print_formatted(n: int):
    base_fmts = [10, 8, 16, 2]
    max_width = 0
    matrix_result = []
    for dec_val in range(1, n+1):
        row_result = []
        for base in base_fmts:
            fmt_val = convert(dec_val, base)
            row_result.append(fmt_val)
            if base == 2 and max_width < len(fmt_val):
                max_width = len(fmt_val)
        matrix_result.append(row_result)
    matrix_str = fmt_str(matrix_result, max_width)
    print(matrix_str)
    return matrix_result

def print_formatted(n):
    for i in range(1,n + 1):
        pad = n.bit_length()
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
