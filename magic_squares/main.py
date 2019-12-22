from typing import List


def generate_odd_square(size: int) -> List[List[int]]:
    """Build associative magic square of given odd size using terrace method."""
    if size <= 0:
        raise ValueError("Size should be grater than 0. Actual: {}.".format(size))
    if size % 2 == 0:
        raise ValueError("Size should be odd. Actual: {}.".format(size))
    temp_square_size = 2 * size - 1
    margin_size = size // 2
    temp_square = [[0 for j in range(temp_square_size)] for i in range(temp_square_size)]
    counter = 1
    dj = 0
    for i in range(size):
        di = size - 1
        for j in range(size):
            temp_square[i + di][j + dj] = counter
            counter += 1
            di -= 1
        dj += 1
    for j in range(margin_size):
        for i in range(temp_square_size):
            temp_square[i][j - margin_size * 2] = temp_square[i][j] or temp_square[i][j - margin_size * 2]
            temp_square[i][j] = 0
            temp_square[i][j + margin_size] = temp_square[i][j - margin_size] or temp_square[i][j + margin_size]
            temp_square[i][j - margin_size] = 0
            temp_square[j - margin_size * 2][i] = temp_square[j][i] or temp_square[j - margin_size * 2][i]
            temp_square[j][i] = 0
            temp_square[j + margin_size][i] = temp_square[j - margin_size][i] or temp_square[j + margin_size][i]
            temp_square[j - margin_size][i] = 0
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(temp_square[margin_size + i][margin_size + j])
        result.append(row)
    return result


def generate_double_even_square(size: int) -> List[List[int]]:
    """Build associative magic square of given double even size using square frames method."""
    if size <= 0:
        raise ValueError("Size should be grater than 0. Actual: {}.".format(size))
    if size % 4 != 0:
        raise ValueError("Size should be double even. Actual: {}.".format(size))
    result = [[0 for j in range(size)] for i in range(size)]
    half_size = size // 2
    value = 1
    for start in range(0, size, 4):
        # clockwise square
        for j in range(half_size):
            i = (start - j + size) % size
            result[i][j] = value
            value += 1
        for j in range(half_size, size):
            i = (start + j + 1) % size
            result[i][j] = value
            value += 1
        for j in range(size - 1, half_size - 1, -1):
            i = (start + size - j) % size
            result[i][j] = value
            value += 1
        for j in range(half_size - 1, -1, -1):
            i = (start + j + 1) % size
            result[i][j] = value
            value += 1
        # anticlockwise square
        anticlockwise_start = start + 2
        for j in range(size - 1, half_size - 1, -1):
            i = (anticlockwise_start + j + 1) % size
            result[i][j] = value
            value += 1
        for j in range(half_size - 1, -1, -1):
            i = (anticlockwise_start - j + size) % size
            result[i][j] = value
            value += 1
        for j in range(half_size):
            i = (anticlockwise_start + j + 1) % size
            result[i][j] = value
            value += 1
        for j in range(half_size, size):
            i = (anticlockwise_start - j + size) % size
            result[i][j] = value
            value += 1
    return result


def generate_single_even_square(size: int) -> List[List[int]]:
    """Build magic square of given single even size using 4 squares method."""
    if size <= 0:
        raise ValueError("Size should be grater than 0. Actual: {}.".format(size))
    if size % 4 != 2:
        raise ValueError("Size should be single even. Actual: {}.".format(size))
    if size == 2:
        raise ValueError("There is no magic square of size 2.")
    result = [[0 for j in range(size)] for i in range(size)]
    base_square_size = size // 2
    base_square = generate_odd_square(base_square_size)
    addition = base_square_size * base_square_size
    for i in range(base_square_size):
        for j in range(base_square_size):
            result[i][j] = base_square[i][j]
            result[i][j + base_square_size] = base_square[i][j] + 2 * addition
            result[i + base_square_size][j] = base_square[i][j] + 3 * addition
            result[i + base_square_size][j + base_square_size] = base_square[i][j] + addition
    result[0][0], result[base_square_size][0] = result[base_square_size][0], result[0][0]
    result[base_square_size - 1][0], result[size - 1][0] = \
        result[size - 1][0], result[base_square_size - 1][0]
    for i in range(1, base_square_size - 1):
        result[i][1], result[base_square_size + i][1] = result[base_square_size + i][1], result[i][1]
    middle_swap_size = base_square_size // 2 - 1
    for j in range(base_square_size - middle_swap_size, base_square_size + middle_swap_size):
        for i in range(base_square_size):
            result[i][j], result[i + base_square_size][j] = result[i + base_square_size][j], result[i][j]
    return result


def print_square(square: List[List[int]]) -> None:
    for row in square:
        for element in row:
            print(element, end=" ")
        print()


def get_magic_square(size: int) -> List[List[int]]:
    """Build magic square with given size. Magic squares of odd and double even sizes are also built associative."""
    if size <= 0:
        raise ValueError("Size should be grater than 0. Actual: {}.".format(size))
    if size == 2:
        raise ValueError("There is no magic square of size 2.")
    if size % 2 == 1:
        return generate_odd_square(size)
    elif size % 4 == 0:
        return generate_double_even_square(size)
    else:
        return generate_single_even_square(size)


if __name__ == '__main__':
    print_square(generate_odd_square(9))
    print()
    print_square(generate_double_even_square(8))
    print()
    print_square(generate_single_even_square(10))
