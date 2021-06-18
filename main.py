from typing import List
from numba import njit


@njit(fastmath=True)
def rabbit_hole(array: List[int], size: int, primary: List[int], secondary: List[int]) -> int:
    row = len(array)
    cases = 0

    for column in range(size):
        primary_val = row + column
        secondary_val = row - column

        if column not in array and primary_val not in primary and secondary_val not in secondary:
            if row == size - 1:
                return 1

            array.append(column)
            primary.append(primary_val)
            secondary.append(secondary_val)

            cases += rabbit_hole(
                array=array,
                size=size,
                primary=primary,
                secondary=secondary,
            )

            array.pop()
            primary.pop()
            secondary.pop()

    return cases


@njit()
def n_queens(size: int) -> int:
    total = 0

    mid = size // 2

    for n in range(mid):
        total += rabbit_hole([n], size, [n], [-n])

    total *= 2

    if mid != size / 2:
        n = (mid) + 1
        total += rabbit_hole([n], size, [n], [-n])

    return total


if __name__ == "__main__":
    from time import time

    start = time()
    solutions = n_queens(18)
    diff = time() - start

    print(f"I found {solutions} ways in {diff} seconds")
