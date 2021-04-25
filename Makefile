
.PHONY: runtest
runtest: 
	python3 testbuilder.py
	python3 get_data.py test_patients.csv
	python3 check_stats.py data_stats.csv test_stats.csv

.PHONY: clean
clean:
	rm test_patients.csv test_stats.csv data_stats.csv


	
