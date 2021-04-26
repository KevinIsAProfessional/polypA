# polypA - A number crunching program for cancer screening records
A polyp is an abnormal growth in the colon (and various other places in the body). Adenomatous polyps are pre-cancerous, and are the main target of colon cancer screenings

## About
This project was started to help organize and parse nearly 20 years of recorded results from colon cancer screenings from my home state of Alaska.
It will (hopefully) be useful in determining trends in cancer rates over time, as well as how geographic location affects community rates. 

The program takes a .csv file of data and returns a .csv file of analysis. 

## Using
Analyze a file \(*outputs results in data\_stats.csv\):
```
python3 get_stats.py your_data_file.csv
```


To run the test suite:
```
make runtest
```


## Requirements 
Python pandas is used in get\_stats.py
