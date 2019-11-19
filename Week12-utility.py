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
