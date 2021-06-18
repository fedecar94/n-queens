matrix = []
primary = []
secondary = []


def rabbit_hole(size: int) -> int:
    row = len(matrix)
    cases = 0

    for column in range(size):
        if column not in matrix and row + column not in primary and row - column not in secondary:
            if row == size - 1:
                return 1

            primary.append(row + column)
            secondary.append(row - column)
            matrix.append(column)

            cases += rabbit_hole(size=size)

            primary.pop()
            secondary.pop()
            matrix.pop()

    return cases


def n_queens(size: int) -> int:
    total = 0

    for n in range(size // 2):
        primary.append(n)
        secondary.append(-n)
        matrix.append(n)

        total += rabbit_hole(size)

        primary.pop()
        secondary.pop()
        matrix.pop()

    total *= 2

    if size // 2 != size / 2:
        n = (size // 2) + 1

        primary.append(n)
        secondary.append(-n)
        matrix.append(n)

        total += rabbit_hole(size)

    return total


if __name__ == "__main__":
    from time import time

    start = time()
    solutions = n_queens(14)
    diff = time() - start

    print(f"I found {solutions} ways in {diff} seconds")
