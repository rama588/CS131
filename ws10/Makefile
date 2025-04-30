
all: clean.csv

trimmed.csv: raw.csv
	cut -d',' -f1,3,5 raw.csv > trimmed.csv

clean.csv: trimmed.csv
	awk -F',' 'NR==1 || ($$2!="" && $$3!="")' trimmed.csv > clean.csv

clean:
	rm -f trimmed.csv clean.csv
