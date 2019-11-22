# https://github.com/jarodclark/Week-12-Utility/blob/master/Week12-utility.py
# Jarod Clark
# CSCI 102 - Section B
# Week 11 - Part B

def PrintOutput(string):
    print('OUTPUT', string)
            
def LoadFile(filename):
    with open(filename, 'r') as file:
        file_read = file.read()
    file_list = file_read.split('\n')
    return file_list

def UpdateString(string1, string2, index_integer):
    string1_list = list(string1)
    for i in range(len(string1_list)):
        if i == index_integer:
            string1_list[i] = string2
    string1_string = ''
    for i in range(len(string1_list)):
        string1_string += string1_list[i]
    PrintOutput(string1_string)

def FindWordCount(List, string):
    count = 0
    for i in range(len(List)):
        if List[i] == string:
            count += 1
    return count

def ScoreFinder(players, scores, string):
    players_string = ''
    string = string.lower()
    for i in range(len(players)):
        players_string += players[i]
        players_string += ' '
    players_string_lower = players_string.lower()
    players_list = players_string_lower.split()
    check = False
    for i in players_list:
        if string in players_list:
            check = True
        else:
            check = False
    if check == True:
        for i in range(len(players_list)):
            if players_list[i] == string:
                index = i
        score = players[index] + ' got a score of ' + str(scores[index]) 
    else:
        score = 'player not found'
    PrintOutput(score)

def Union(list1, list2):
    one_set = set(list1)
    two_set = set(list2)

    return_list = []
    return_list = list(one_set | two_set)
    return return_list

def Intersection(list1, list2):
    one_set = set(list1)
    two_set = set(list2)
    
    intersect_list = list(one_set & two_set)
    return intersect_list

def NotIn(list1, list2):
    one_set = set(list1)
    two_set = set(list2)

    newlist = list(one_set - two_set)
    return newlist

