# Week-12-utility
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
