# polypA - analysis tool on cancer screening records
_A polyp is an abnormal growth in the colon. Adenomatous polyps are pre-cancerous, and are the main target of colon cancer screenings_

## About
This project was started to help organize and parse nearly 20 years of recorded results from colon cancer screenings from my home state of Alaska.
It will (hopefully) be useful in determining trends in cancer rates over time, as well as how community cancer rates differ by geographic location. 

The program takes a .csv file of data and returns a .csv file of analysis. 

# Using
Analyze a file \(outputs results in data\_stats.csv\):
```
python3 get_stats.py your_data_file.csv
```

To run the test suite:
```
make runtest
```

# Requirements 
Python pandas is used in get\_stats.py.

# Coming Soon
- Add functionality to produce graphs from data\_stats.csv.
- Add tools to clean up incoming data files more easily.
- Update testing framework to be more specific, provide more user feedback.
- Update get\_stats.py to allow user to specify output file name.
- Add function to compare the results of two or more datasets

# Author~~s~~
- Kevin Christensen
