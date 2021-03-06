.PHONY: all
all: runtest

.PHONY: runtest
runtest: 
	@echo "Building test files"
	@python3 testbuilder.py
	@echo "Running data analysis on test file"
	@python3 get_stats.py test_patients.csv
	@echo "Comparing output to test_stats"
	@python3 check_stats.py data_stats.csv test_stats.csv
	@echo "Test complete. If you don't see anything, then the test was successful"
	@echo "Cleaning up"
	@rm test_patients.csv test_stats.csv data_stats.csv

.PHONY: clean
clean:
	rm test_patients.csv test_stats.csv data_stats.csv


	
