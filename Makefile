
.PHONY: runtest
runtest: test_patients.csv test_stats.csv	
	python3 ../datagathering.py test_patients.csv
	cat test_stats.txt

test_patients.csv:
	python3 testbuilder.py

.PHONY: clean
clean:
	rm test_patients.csv test_stats.csv


	
