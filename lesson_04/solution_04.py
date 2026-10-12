
"""Домашнее задание № 4. Две задачи на изученные приёмы."""


def min_boats(weights, limit):
    """Вернуть минимальное число лодок, не изменяя исходный список."""
    people = sorted(weights)
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        # Самого тяжёлого пробуем посадить с самым лёгким.
        if left < right and people[left] + people[right] <= limit:
            left += 1

        # Самый тяжёлый в любом случае занимает одну лодку.
        right -= 1
        boats += 1

    return boats


def even_first(nums):
    """Переставить чётные числа перед нечётными на месте."""
    left = 0
    right = len(nums) - 1

    while left < right:
        # Ищем нечётное число слева.
        while left < right and nums[left] % 2 == 0:
            left += 1

        # Ищем чётное число справа.
        while left < right and nums[right] % 2 != 0:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
