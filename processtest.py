# create a test class with an __init__ function that counts number of rows in a file.

import pandas as pd
import sys

class Dataset:
    def __init__(self,csv_input):
        self.df = pd.read_csv(csv_input, header=0)
        self.patients = self.countPatients(self.df) 
        self.mcount = self.df.query('Sex == "M"')['Reason'].count()
        self.fcount = self.df.query('Sex == "F"')['Reason'].count()
        
    def countPatients(self,dataframe):
        return len(dataframe.index)



def main():
    #print("enter filename: ")
    datafile = string(input("enter filename: "))
    #datafile = sys.argv[1]
    dataset = Dataset(datafile) 
    print(dataset.patients) 

if __name__ == "__main__":
    main()
