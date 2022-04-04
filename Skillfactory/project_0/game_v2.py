"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 101
    while True:
        count += 1
        predict_number = (max - min)//2 + min #Предполагаемое число
        if number == predict_number:
            break #выход из цикла, если угадали
        if number > predict_number:
            min = predict_number     #Если загаданное число больше, увеличиваем минимум диапазона
        if number < predict_number:
            max = predict_number     #Если загаданное число меньше, уменьшаем максимум диапазона
    return(count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    n_min = min(count_ls)
    n_max = max(count_ls)
    print(f"\nВаш алгоритм угадывает число в среднем за: {score} попыток\n")
    print(f"Числа угадывались за {n_min} - {n_max} попыток:")
    for n in range(n_min, n_max +1): # выводим, по сколько раз было угадывание за n попыток
        if n == 1: l = "шаг"
        if 1 < n < 5: l = "шага"
        if n > 4: l = "шагов"
        print(f"За {n} {l} число было угадано {count_ls.count(n)} раз.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
