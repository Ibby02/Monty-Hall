from random import randint
import matplotlib.pyplot as plt
import numpy as np

def monty_hall_game():

    return {
        "options_in_game" : [0,1,2],
        "correct_answer": randint(0,2)
    }

def player():
    player_selection = randint(0,2)
    return player_selection

def play_game():
    monty_hall = monty_hall_game()
    player_selection = player()

    for option in monty_hall['options_in_game']:
        if option != player_selection:
            if option != monty_hall['correct_answer']:
                monty_hall['options_in_game'].remove(option)
                break
    
    new_player_selection = None
    for option in monty_hall['options_in_game']:
        if option != player_selection:
            new_player_selection = option

    #print('Monty_Hall_game: {}'.format(monty_hall))
    print('Player_selection: {}'.format(player_selection))
    print('New Player_Selection: {}'.format(new_player_selection))
    
    if new_player_selection == monty_hall['correct_answer']:
        print('Player has won')
        return True
    else:
        print('Player has not won')
        return False

results = {
    'player_change': 0,
    'player_stays': 0
}


NUM_OF_RUNS = 1000
for i in range(NUM_OF_RUNS):
    result = play_game()
    if result:
        results['player_change']+=1

    else:
        results['player_stays']+=1

print('results of playing game {} times: {}'.format(NUM_OF_RUNS, results))

y = np.array([results['player_change'], results['player_stays']])
my_labels = ["When player changes their original selection", "When player does not change their original selection"]
myexplode = [0.2, 0]
mycolors = ['green','orange']

plt.pie(y, labels = my_labels, autopct='%1.1f%%', explode = myexplode, shadow = True, colors = mycolors)
plt.show() 