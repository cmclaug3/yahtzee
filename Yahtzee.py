# YAHTZEE

import random
import time



# End game function
def quit_game():
    print()
    if len(player_choices) == 13:
        print('YOU COMPLETED THE GAME!')
    else:
        print('YOU QUIT')
    print()
    print('Final Score: {}'.format(score))


# Output list of n number of random dice rolls (random five dice rolls)
def diceRoll(n):
    rolls = 0
    roll_list = []
    while rolls < n:
        roll_list.append(random.choice(range(1,7)))
        rolls += 1
    return roll_list


# Make sure input "keep dice positions" are valid
def come_correct(string_of_nums):
    holder = []
    if string_of_nums.isdigit() == False:
        return False
    string_of_nums = str(string_of_nums)
    for num in string_of_nums:
        if int(num) < 0 or int(num) > 5:
            return False
        else:
            holder.append(int(num))
    if len(holder) == len(set(holder)):
        return True
    else:
        return False


# Complete all rolls and keeps in turn
def turn_roll(roll_list):
    turns = 3
    while turns > 0:
        print(roll_list)
        keep_list = []
        print()
        keeper_ind = str(input('Which dice to keep? Press "a" to hold all, "0" to hold none: '))
        print()
        if keeper_ind == '0':
            roll_list = diceRoll(5)
            turns -= 1
            continue
        elif keeper_ind == 'a':
            break
        elif keeper_ind == 'Q':
            return 'user wants to quit'
        elif come_correct(keeper_ind) == False:
            print('You need to enter a valid position(s) or command')
            print()
            continue                                                   
        else:
            for i in keeper_ind:
                keep_list.append(int(i))
            keeper_list = []
            for dice in keep_list:
                keeper_list.append(roll_list[dice-1])
            while len(keeper_list) < 5:
                randy = random.choice(range(1,7))
                keeper_list.append(randy)
            roll_list = keeper_list
            turns -= 1
    print()
    return roll_list


# Check if player has a full house
def is_full_house(roll):
    valueDict = dict([(x, 0) for x in range(1,7)])
    for die in roll:
        valueDict[die] += 1
    setDict = dict([(x, 0) for x in range(0,6)])
    for setSize in valueDict.values():
        setDict[setSize] += 1
    return setDict[2] == 1 and setDict[3] == 1


# Check if player has a 4 of a kind
def is_4_of_kind(roll):
    valueDict = dict([(x, 0) for x in range(1,7)])
    for die in roll:
        valueDict[die] += 1
    setDict = dict([(x, 0) for x in range(0,6)])
    for setSize in valueDict.values():
        setDict[setSize] += 1
    if min(roll) == max(roll):
        return True
    return setDict[4] == 1


# Check if player has a 3 of a kind
def is_3_of_kind(roll):
    valueDict = dict([(x, 0) for x in range(1,7)])
    for die in roll:
        valueDict[die] += 1
    setDict = dict([(x, 0) for x in range(0,6)])
    for setSize in valueDict.values():
        setDict[setSize] += 1
    if is_4_of_kind(roll) == True:
        return True
    return setDict[3] == 1


# Check if player has a small straight (four in a row)
def is_small_straight(roll):
    a = [1,2,3,4]
    b = [2,3,4,5]
    c = [3,4,5,6]
    count = 0
    for dice in roll:
        if dice in a:
            a.remove(dice)
            count += 1
    if count == 4:
        return True
    count = 0
    for dice in roll:
        if dice in b:
            b.remove(dice)
            count += 1
    if count == 4:
        return True
    count = 0
    for dice in roll:
        if dice in c:
            c.remove(dice)
            count += 1
    if count == 4:
        return True
    else:
        return False


# Check if player has a large straight (five in a row)
def is_large_straight(roll):
    a = [1,2,3,4,5]
    b = [2,3,4,5,6]
    count = 0
    for dice in roll:
        if dice in a:
            a.remove(dice)
            count += 1
    if count == 5:
        return True
    count = 0
    for dice in roll:
        if dice in b:
            b.remove(dice)
            count += 1
    if count == 5:
        return True
    else:
        return False




## Start of Game
score = 0
player_rolls = []
player_choices = []
num_choices = ['1s','2s','3s','4s','5s','6s']
ex_choices = ['fh','ss','ls','3ok','4ok','y','w']
choices = num_choices + ex_choices

print()
print()
print('***************************************')
print('***************************************')
print()
print('WELCOME TO YAHTZEE!')
print()
print()
print()
print('Hold dice by place number')
print()
print('Set of dice   -->    [4,1,4,4,6]')
print('Positions     -->     1 2 3 4 5')
print()
print('For example: to hold the three 4\'s, enter 134')
print()
print()
print('You have up to three rolls to obtain your best set of dice')
print()
print()
print('Then make a scoring choice')
print()
print('CHOICES ---- HOW TO CHOOSE')
print('One\'s             1s')
print('Two\'s             2s')
print('Three\'s           3s')
print('Four\'s            4s')
print('Five\'s            5s')
print('Six\'s             6s')
print('Full House        fh')
print('Small Straight    ss')
print('Large Straight    ls')
print('Three of a Kind   3ok')
print('Four of a Kind    4ok')
print('Yahtzee           y')
print('Wild              w')
print()
print('Press "Q" to quit at any time')
print()
print('***************************************')
print('***************************************')
print()
time.sleep(1)
for i in [7,'.','.',6,'.','.',5,'.','.',4,'.','.',3,'.','.',2,'.','.',1,]:
    print(i, end='')
    time.sleep(.33)
    if i == 1:
        print()
        print('Lets Play')
print()
print()
print()
print()

while len(choices) > 0:
    
    time.sleep(.5)
    
    the_roll = turn_roll(diceRoll(5))

    if the_roll == 'user wants to quit':
        choices = []
        continue
    
    print(the_roll)
    
    print()
    time.sleep(.5)

    not_good_choice = True

    while not_good_choice:
    
        score_choice = str(input('How do you want to play this roll? '))
        print()

        if score_choice == 'Q':
            choices = []
            break

        elif score_choice not in choices:
            print('You messed up try again. Make an available pick')
            continue
        else:

            # Successful choices / add points
            if score_choice == '1s':
                new = [i for i in the_roll if i == 1]
                score += sum(new)
                
            elif score_choice == '2s':
                new = [i for i in the_roll if i == 2]
                score += sum(new)
                
            elif score_choice == '3s':
                new = [i for i in the_roll if i == 3]
                score += sum(new)
                
            elif score_choice == '4s':
                new = [i for i in the_roll if i == 4]
                score += sum(new)
                
            elif score_choice == '5s':
                new = [i for i in the_roll if i == 5]
                score += sum(new)
                
            elif score_choice == '6s':
                new = [i for i in the_roll if i == 6]
                score += sum(new)
                
            elif score_choice == 'ss':
                if is_small_straight(the_roll) == True:
                    score += 30
                else:
                    print('that is not a small straight')
                
            elif score_choice == 'ls':
                if is_large_straight(the_roll) == True:
                    score += 40
                else:
                    print('that is not a large straight')
                
            elif score_choice == 'fh':
                if is_full_house(the_roll) == True:
                    score += 25
                else:
                    print('that is not a full house')
                
            elif score_choice == '3ok':
                if is_3_of_kind(the_roll) == True:
                    score += sum(the_roll)
                else:
                    print('that is not a 3 of a kind')

            elif score_choice == '4ok':
                if is_4_of_kind(the_roll) == True:
                    score += sum(the_roll)
                else:
                    print('that is not a 4 of a kind')

            elif score_choice == 'y':
                if min(the_roll) == max(the_roll):
                    score += 50
                else:
                    print('that is not a yahtzee..')

            elif score_choice == 'w':
                score += sum(the_roll)

    
            not_good_choice = False
            player_rolls.append(the_roll)
            player_choices.append(score_choice)

                
        print()
        yay = zip(player_choices, player_rolls)
        
        print('______________________________________')
        print('SCORE: {}       "Q" to quit at anytime'.format(score))
        print()
        for key, val in yay:
            print('{} = {}'.format(key,val))

        choices.remove(str(key))
        
        print()
        print('Still need -->  {}'.format('  '.join([i for i in num_choices if i in choices])))
        print('           -->  {}'.format('  '.join([i for i in ex_choices if i in choices])))
        print('______________________________________')
        print()
        time.sleep(1)

quit_game()

