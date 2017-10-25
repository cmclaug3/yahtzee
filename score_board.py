import json
import datetime
import os
from tablegen import print_table

##from terminaltables import AsciiTable


def add_to_score_board(s,fn):

    with open(fn, 'r+') as f:
        try:
            data = json.load(f)
        except (ValueError,FileNotFoundError,):
            data = {}

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    if len(new) >= 5:
        if s < new[4][1][0]:
            return 'Sorry, not a new high score'

    n = input('Enter name for high score: ')
    date = datetime.datetime.now()
    string_date = date.strftime('%m/%d/%y')

    
    data[n] = [s, string_date]

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    with open(fn, 'w+') as end:
        json.dump(data, end)
 


def show_score_board(fn):
    
    with open(fn, 'r+') as f:
        data = json.load(f)

    new = sorted(data.items(), key=lambda e: e[1][0], reverse=True)

    with open(fn, 'w+') as end:
        json.dump(data, end)


    table_data = [(' ','Name','Score','Date')]

    for k,v in enumerate(new[:5], 1):
        table_data.append([str(k), v[0], str(v[1][0]), v[1][1]])


    print()
    print('HIGH SCORES')
    print()
    print_table(table_data)






 
##    print()
##    print()
##    print('****************HIGH********************')
##    print('***************SCORES*******************')
##    print()
##    for k,v in enumerate(new[:5], 1):
##        print('{}. {}  {}   {}'.format(k,v[0],v[1][0],v[1][1]))
##    print()
##    print('****************************************')
##    print('****************************************')
##    print()
##    print()





    
