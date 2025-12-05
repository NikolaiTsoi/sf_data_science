import numpy as np

def game_core_v3(number: int = 1) -> int:
    # Бинарный поиск: угадываем число в диапазоне 1..100
    # number (int): Загаданное число
    # int: Число попыток

    count = 0
    left = 1  # левая граница
    right = 100  # правая граница

    while left <= right:
        count += 1
        predict = (left + right) // 2  # берём середину диапазона

        if number == predict:
            return count  # угадали!
        elif number > predict:
            left = predict + 1  # ищем в правой половине
        else:
            right = predict - 1  # ищем в левой половине

    # Если вдруг число вне диапазона (на всякий случай)
    return count

def score_game(game_core_v3) -> int:
    # За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм
    # game_core_v3 ([type]): функция угадывания
    # int: среднее количество попыток

    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=10000)  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score


print(game_core_v3(20))
score_game(game_core_v3)