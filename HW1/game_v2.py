import numpy as np

def random_predict(number: int=1) -> int:
    """ Binary search,
        The upper and lower search boundaries are used.
        At each iteration of the loop: a hidden number is compared with
        the average between the upper and lower limits.
        Returns the number of iterations.

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts.
    """
    count = 0   # save the number of attempts
    upper = 100  
    lower = 1
    mid = 50
    while mid != number:
        count += 1
        if mid > number:
            upper = mid - 1
        elif mid < number:
            lower = mid + 1
        mid = (upper + lower) // 2
    return count

def score_game(random_predict) -> int:
    """
    Generates a list of random numbers and applies random_predict to each one
    Returns an average number of iterations of random_predict.
    
    Args:
        random_predict (function): search a hidden number

    Returns:
        int: the number on average tries
    """
    count_ls = [] # list to save the number of attempts
    np.random.seed(1) # fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))#hid list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average number of attempts

    print(f'Your algorithm guesses the number on average in: {score} tries')
    return(score)

score_game(random_predict)