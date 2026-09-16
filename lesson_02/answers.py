"""Ваши ответы по фрагментам из fragments.py · занятие 3.

Заполните оба словаря и запустите проверку:

    pytest course-materials/complexity/test_lesson_03.py

Проверка сравнивает не текст, а отпечаток ответа, поэтому подсмотреть
правильные оценки в тестах нельзя. Зато можно проверять себя сколько угодно
раз: тест называет номер фрагмента, но не называет верный ответ.

Как записывать оценку:

    O(1)        O(log n)      O(n)        O(n log n)      O(n^2)
    O(n + m)    — когда входов два и они растут независимо

Регистр букв и пробелы значения не имеют: «o(N LOG N)» засчитается.
Записи «O(2n)», «O(n/2)» и «O(n^2 + n)» — нет: константы и младшие
слагаемые в оценке не пишутся.

Незаполненный ответ — пустая строка. Тест покажет его как «не заполнено»,
а не как ошибку.
"""

# Время: как растёт число операций с ростом входа.
TIME = {
    "01_find_pass": "O(n)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(n^2)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n log n)",
    "06_find_receipt": "O(log n)",
    "07_average_and_spikes": "O(n)",
    "08_closest_pair_distance": "O(n^2)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n^2)",
    "11_halving_steps": "O(log n)",
    "12_merge_sorted": "O(n + m)",
}

# Память: сколько функция занимает дополнительно к тому, что ей передали.
SPACE = {
    "01_find_pass": "O(1)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(1)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n)",
    "06_find_receipt": "O(1)",
    "07_average_and_spikes": "O(1)",
    "08_closest_pair_distance": "O(1)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n)",
    "11_halving_steps": "O(1)",
    "12_merge_sorted": "O(n + m)",
}

# Худший случай двух фрагментов — одной строкой: при каком входе
# работы больше всего и почему.
WORST_CASE = {
    "01_find_pass": "Искомого пропуска нет в списке, или он стоит самым последним.",
    "04_has_duplicate_badges_fast": "В списке нет одинаковых пропусков",
}
