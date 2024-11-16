import numpy as np


def random_predict(number: int = 1, left: int = 1, right: int = 101, count=0) -> int:
    """бинарный поиск, только со случайными числами"""
    count += 1
    predict_numb = np.random.randint(left, right)
    if predict_numb < number:
        left = predict_numb + 1
    elif predict_numb > number:
        right = predict_numb
    elif predict_numb == number:
        return count
    return random_predict(number, left, right, count)


def score_game(random_predict) -> None:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм
    Args: random_predict ([type]): функция угадывания
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(6))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == '__main__':
    score_game(random_predict)