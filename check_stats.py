#!/usr/bin/env python3

###########################################################
#         Compare two .csv files for equivalence          #
###########################################################

import sys
import difflib

def check_stats(data_stats,test_stats):
    with open('data_stats.csv', 'r') as datafile:
        data = datafile.readlines()
    
    with open('test_stats.csv', 'r') as testfile:
        test = testfile.readlines()

    for line in difflib.unified_diff(data, test, fromfile='test_stats.csv', tofile='data_stats.csv', lineterm=''):
        print(line)


if __name__=="__main__":
    check_stats(sys.argv[1],sys.argv[2])
