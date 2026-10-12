
"""Домашнее задание № 5. Скользящее окно фиксированного размера."""


def step_score(steps, k, lower, upper):
    """Подсчитать очки фитнес-браслета за все окна длины k."""
    n = len(steps)

    # Сумма первого окна.
    window_sum = sum(steps[:k])
    score = 0

    def evaluate(total):
        if total < lower:
            return -1
        if total > upper:
            return 1
        return 0

    score += evaluate(window_sum)

    # Сдвигаем окно: убираем ушедший день,
    # добавляем новый день.
    for i in range(k, n):
        window_sum += steps[i] - steps[i - k]
        score += evaluate(window_sum)

    return score


def decrypt(code, k):
    """Расшифровать круговой код с помощью скользящего окна."""
    n = len(code)

    if k == 0:
        return [0] * n

    result = []
    window_size = abs(k)

    if k > 0:
        # Сумма k следующих чисел для первой позиции.
        window_sum = sum(code[1:k + 1])

        for i in range(n):
            result.append(window_sum)

            # Убираем первое число прежнего окна
            # и добавляем следующее по кругу.
            window_sum -= code[(i + 1) % n]
            window_sum += code[(i + k + 1) % n]

    else:
        # Сумма |k| предыдущих чисел для первой позиции.
        window_sum = sum(
            code[j % n] for j in range(k, 0)
        )

        for i in range(n):
            result.append(window_sum)

            # При движении вправо меняется граница окна.
            window_sum -= code[(i + k) % n]
            window_sum += code[i % n]

    return result
