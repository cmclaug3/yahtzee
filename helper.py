from tablegen import print_table



def show_keyboard_shortcuts():
    print()
    print('     __________________')
    print('     KEYBOARD SHORTCUTS')
    print()
    print('      Always available')
    print('==============================')
    print('QUIT               ----->    Q')
    print('HELP               ----->    H')
    print('KB SHORTCUTS       ----->    K')
    print('REMAINING CHOICES  ----->    C')
    print('HIGH SCORES        ----->    S')
    print('HIGH SCORES (all)  ----->    Sa')
    print()
    print('     During dice rolling')
    print('==============================')
    print('HOLD ALL DICE      ----->    a')
    print('GET ALL NEW DICE   ----->    0')
    print()
    print()



def point_breakdown():
    print()
    print('     _______________')
    print('     POINT BREAKDOWN')
    print()
    print()
    print('** UPPER choices --> 1s 2s 3s 4s 5s 6s')
    print()
    print('     Score --> Sum of dice in roll matching choice')
    print()
    print()
    print('** LOWER Choices')
    print()

    table_data = [('Choice','Play','Score','Stipulations'),
                    ['3ok', 'Three of a kind', 'Sum of all', 'Must have atleast three of same dice'],
                    ['4ok', 'Four of a kind', 'Sum of all', 'Must have atleast four of same dice'],
                    ['fh', 'Full House', '25', 'Three of one, two of another'],
                    ['ss', 'Small Straight', '30', '>= Four dice in numerical order'],
                    ['ls', 'Large Straight', '40', '>= Five dice in numerical order'],
                    ['y', 'Yahtzee', '50', 'All five dice the same'],
                    ['w', 'Wild', 'Sum of all', 'NONE']
                ]

    print_table(table_data)


def about_yahtzee():
    print()
    print('     ABOUT YAHTZEE')
    print()
    print('The object of the game is to score points by rolling five dice\n'
    'to make certain combinations. The dice can be rolled up to three times\n'
    'in a turn to try to make various scoring combinations. A game consists\n'
    'of thirteen rounds. After each round the player chooses which scoring\n'
    'category is to be used for that round. Once a category has been used\n'
    'in the game, it cannot be used again. The scoring categories have\n'
    'varying point values, some of which are fixed values and others where\n'
    'the score depends on the value of the dice.')
    print()
    

            
def master_help():
    
    need_help = True
    
    print('----------------------------------------------')
    print()
    print('HELP MENU')
    print()
    print()
    print('What do you need help with?')
    print()
    print('**************HELP**************')
    print('*************OPTIONS************')
    print()
    print('ABOUT YAHTZEE        ------->  1')
    print('HOW TO PLAY          ------->  2')
    print('KEYBOARD SHORTCUTS   ------->  3')
    print('POINT BREAKDOWN      ------->  4')
    print()
    print('EXIT HELP MENU       ------->  E')
    print()
    print('*********************************')
    print('*********************************')
    print()

    while need_help:
        print()
        help_choice = input('Please choose a topic from menu above ("H")\nOr "E" to EXIT: ')

        print('*********************************')
        print('*********************************')

        if help_choice == '1':
            print()
            print('this is where yahtzee info will go')

        elif help_choice == '2':
            print()
            print('this is where game play info will go')

        elif help_choice == '3':
            show_keyboard_shortcuts()

        elif help_choice == '4':
            point_breakdown()

        elif help_choice == 'H':
            print()
            print('What do you need help with?')
            print()
            print('**************HELP**************')
            print('*************OPTIONS************')
            print()
            print('ABOUT YAHTZEE        ------->  1')
            print('HOW TO PLAY          ------->  2')
            print('KEYBOARD SHORTCUTS   ------->  3')
            print('POINT BREAKDOWN      ------->  4')
            print()
            print('EXIT HELP MENU       ------->  E')
            print()
            print('*********************************')
            print('*********************************')
            print()

        elif help_choice == 'E':
            print()
            print('----------------------------------------------')
            print()
            break

        else:
            print()
            print('Not a valid choice')
            continue







    
    
    
