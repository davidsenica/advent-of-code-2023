def line_iterator(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.rstrip()


def read_all(file_name, as_list=True):
    with open(file_name) as f:
        if as_list:
            return [line.strip() for line in f.readlines()]
        return f.read()


def to_int(numbers):
    if isinstance(numbers, list):
        return [int(n) for n in numbers]
    return int(numbers)


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))
    print()

