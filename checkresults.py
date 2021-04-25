#!/usr/bin/env python3 
#import datagathering as dg
import processtest as dg

#def check_results(infile: str, resultsfile: str):
#    """
#    runs datagathering.py on test_patients.csv and 
#    checks the output against the figures specified 
#    in test_results.txt
#
#    >>> check_results('test_patients.csv','test_results.txt'):
#    
#    
#    """
#    if(type(infile) != str || type(resultsfile != str)):
#        raise Exception("invalid filenames")
#
#    pass

def check_results(infile,resultsfile):
    dataset = dg.Dataset(infile)
    rf = open(resultsfile, 'r')

    out = "Number of patients: " + str(dataset.patients) + "\n"
    patient_count(out,rf.readline())
    
    out = " Number of Male/Female: " + str(dataset.mcount) + "/" + str(dataset.fcount) + "\n"

    gender_count(out,rf.readline())
    rf.close()


def patient_count(patients_count_recieved,patients_count_actual):
    if(patients_count_recieved == patients_count_actual):
        print("Number of patients: Passed")
    else:
        print("Number of patients: Failed")
        print("Expected: " + patient_count_actual)
        print("Got: " + patient_count_recieved)
        
def gender_count(gender_count_recieved, gender_count_actual):
    if(gender_count_recieved == gender_count_actual):
        print("Number of male/female: Passed")
    else:
        print("Number of male/female: Failed")
        print("Expected: " + gender_count_actual)
        print("Got: " + gender_count_recieved)

def main():
    check_results("test_patients.csv","test_stats.txt")

if __name__ == "__main__":
    main()
