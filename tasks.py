"""Utility functions for solving assignment 6 exercises.

The module contains small helpers that were originally implemented as a
script.  They now expose reusable functions and an interactive ``main`` entry
point that mirrors the behaviour of the initial solution while improving the
input validation and overall structure.
"""

from __future__ import annotations

import random
from typing import Iterable, List


def max_of_two(a: float, b: float) -> float:
    """Return the greater of two numbers.

    When the numbers are equal the shared value is returned.  The function does
    not perform any printing so it can be reused from tests and other modules.
    """

    return a if a >= b else b


def check_odd_even(value: str) -> str:
    """Classify the parity of ``value``.

    ``value`` can use either a comma or a dot as the decimal separator.  When
    the provided value is not a positive integer a descriptive message is
    returned instead of raising an exception.
    """

    if value is None:
        return "Неправильне значення аргументу"

    normalised = value.replace(",", ".").strip()
    try:
        number = float(normalised)
    except ValueError:
        return "Неправильне значення аргументу"

    if number <= 0:
        return "Неправильне значення аргументу"

    if not number.is_integer():
        return "Це не ціле число, тому парність неможливо визначити"

    integer_value = int(number)
    if integer_value % 2 == 0:
        return "Число парне"
    return "Число непарне"


def reorder_non_negative_then_negative(numbers: Iterable[int]) -> List[int]:
    """Return ``numbers`` with non-negative values before negative ones."""

    non_negative = [num for num in numbers if num >= 0]
    negative = [num for num in numbers if num < 0]
    return non_negative + negative


def move_zeros_to_end(numbers: Iterable[int]) -> List[int]:
    """Return ``numbers`` where all zeros are moved to the end."""

    non_zero = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zero + zeros


def _prompt_float(prompt: str) -> float:
    """Prompt the user for a floating point number with validation."""

    while True:
        raw = input(prompt)
        try:
            return float(raw.replace(",", "."))
        except (AttributeError, ValueError):
            print("Некоректне число. Спробуйте ще раз.")


def _prompt_positive_int(prompt: str) -> int:
    """Prompt the user for a positive integer."""

    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Введіть ціле додатне число.")
            continue

        if value <= 0:
            print("Число має бути додатним.")
            continue

        return value


def main() -> None:
    """Run the interactive version of the four exercises."""

    print("Перше завдання. Пошук більшого з двох чисел.")
    first = _prompt_float("Введіть перше число: ")
    second = _prompt_float("Введіть друге число: ")
    bigger = max_of_two(first, second)

    if first == second:
        print("Числа рівні:", bigger)
    else:
        print("Найбільше число:", bigger)

    print("\nДруге завдання. Перевірка на парність.")
    parity_input = input("Введіть число для перевірки парності: ")
    print(check_odd_even(parity_input))

    print("\nТретє завдання. Робота зі списками.")
    size = _prompt_positive_int("Введіть кількість елементів списку n: ")
    numbers = [random.randint(-10, 10) for _ in range(size)]
    print("Початковий список:", numbers)

    reordered = reorder_non_negative_then_negative(numbers)
    print("Список (спочатку невід'ємні, потім від'ємні):", reordered)

    moved_zeros = move_zeros_to_end(numbers)
    print("Список (нулі перенесено у кінець):", moved_zeros)


if __name__ == "__main__":  # pragma: no cover - behaviour exercised manually
    main()
