#!/bin/bash

#Generating the timestamp.
timestamp=$(date "+%F-%T")

#Defining the input file, which is present in the CS131 directory.
input_file="../2019-01-h1.csv"

#Checking if the input file exists.
if [[ ! -f "$input_file" ]]; then
    echo "Error: Input file $input_file not found!"
    exit 1
fi

#Extracting the header of the input file.
header=$(head -n 1 "$input_file")

#Processing each vendoriD using sed command.
for vendor in 1.0 2.0 4.0; do
    output_file="${timestamp}-${vendor}.csv"

    #Writing the header line first.
    echo "$header" > "$output_file"

    #Using sed to extract lines that contain the vendorID.
    sed -n "/^$vendor,/p" "$input_file" >> "$output_file"

    #Appending the output file name to .gitignore. 
    echo "$output_file" >> .gitignore
done

#Using wc to count lines, words, and characters of all the csv files.
wc -l -w -c ${timestamp}-1.0.csv ${timestamp}-2.0.csv ${timestamp}-4.0.csv > ws4.txt

#Appending .gitignore contents to ws4.txt.
echo -e "\nContents of .gitignore:" >> ws4.txt
cat .gitignore >> ws4.txt

echo "Process Done! Files are in ws4/."

