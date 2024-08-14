from random import shuffle

def shuffle_list(myList: list):
    shuffle(myList)
    #print(myList)
    return myList

def player_guess():
    guess = ''
    while(True):
        guess = input("Enter user guess 1,2 or 3 : ")
        if guess == "1" or guess == "2" or guess == "3":
            break
    return int(guess)

def check_guess(cup_list:list, user_guess:int):
    result = ''
    if cup_list[user_guess - 1] == 'o':
        result = 'correct'
    else:
        result = 'wrong'
        print(cup_list)
    return result

example = ['','o', '']
v_cup_list = shuffle_list(example)
v_player_guess = player_guess()
status = check_guess(v_cup_list, v_player_guess)
print(f'Result of game is {status}')