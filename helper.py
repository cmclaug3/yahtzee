



def show_keyboard_shortcuts():
    print()
    print()
    print()
    print('     KEYBOARD SHORTCUTS')
    print()
    print('      Always available')
    print('==============================')
    print('QUIT               ----->    Q')
    print('HELP               ----->    H')
    print('KB SHORTCUTS       ----->    K')
    print('REMAINING CHOICES  ----->    C')
    print('HIGH SCORES        ----->    S')
    print()
    print('     During dice rolling')
    print('==============================')
    print('HOLD ALL DICE      ----->    a')
    print('GET ALL NEW DICE   ----->    0')
    print()
    print()
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
    print()
    print('EXIT HELP MENU       ------->  E')
    print()
    print('*********************************')
    print('*********************************')
    print()

    while need_help:
        print()
        help_choice = input('Please choose a topic from menu above\nOr "E" to EXIT: ')

        if help_choice == '1':
            print()
            print('this is where yahtzee info will go')

        elif help_choice == '2':
            print()
            print('this is where game play info will go')

        elif help_choice == '3':
            show_keyboard_shortcuts()

        elif help_choice == 'E':
            print()
            print('----------------------------------------------')
            print()
            break

        else:
            print()
            print('Not a valid choice')
            continue



    

    
    
    
