import numpy as np

def random_predict(number:int=1)->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаланное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 0
    max = 101
    while True:
        count += 1
#       predict_number = np.random.randint(1,101) #Предполагаемое число
        predict_number = (max - min)//2 + min #Предполагаемое число
        if number > predict_number:
            min = predict_number
        if number < predict_number:
            max = predict_number
        if number == predict_number:
            break #выход из цикла, если угадали
    return(count)
   
    
def score_game(random_predict)->int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


#RUN
if __name__ == '__main__':
    score_game(random_predict)
