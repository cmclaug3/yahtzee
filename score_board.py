import json
import datetime
import os
from tablegen import print_table



def add_to_score_board(s,fn):

    with open(fn, 'r+') as f:
        try:
            data = json.load(f)
        except (ValueError,FileNotFoundError,):
            data = {}

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    if len(new) >= 10:
        if s < new[9][1][0]:
            print()
            print('Sorry that\'s not a worthy high score')

        else:
            n = input('Enter name for HIGH score: ')

            date = datetime.datetime.now()
            string_date = date.strftime('%m/%d/%Y')

            data[n] = [s, string_date]

    else:
        n = input('Enter name for NEW score: ')

        date = datetime.datetime.now()
        string_date = date.strftime('%m/%d/%Y')

        data[n] = [s, string_date]

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    with open(fn, 'w+') as end:
        json.dump(data, end)
 


def show_score_board(fn, length='a'):
    
    with open(fn, 'r+') as f:
        data = json.load(f)

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    with open(fn, 'w+') as end:
        json.dump(data, end)

    if length == 'a':
        length = len(new)

    table_data = [(' ','Name','Score','Date')]

    for k,v in enumerate(new[:length], 1):
        table_data.append([str(k), v[0], str(v[1][0]), v[1][1]])


    print()
    print('HIGH SCORES')
    print()
    print_table(table_data)



# Erase all scores except for defaults
def trash_score_board(fn):
    pass





    
