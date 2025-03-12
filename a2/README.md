# `findsort.sh` - File Finder and Organizer

## **What This Command Does**  
`findsort.sh` is a command-line tool that helps users:  
- Search for files by name, type, or content.  
- Organize files into categorized folders (Documents, Images, Scripts, etc.).  
- Keep directories clean by sorting files into appropriate locations.  

---

## **Why/When This Command Is Useful**  
- **For Developers**: Quickly find scripts, logs, or project files.  
- **For Students & Researchers**: Locate PDFs, notes, and reports easily.  
- **For General Users**: Clean up messy directories by auto-sorting files.  

---

## **How to Use This Command**  

### **Basic Syntax**  
findsort \<directory> \<option> \<value>

**Options:**  
  --search \<name>    Find files by name.  
  --type \<ext>       Find files by extension.  
  --content \<text>   Find files containing text.  
  --sort             Categorize files into folders.  
  --help             Show this message.

### **Examples** 

\1. Search for files by name -  

ramakrishna\_pudota@instance-20250203-032935:~/CS131/a2$ ./findsort.sh ~/CS131 --search 2019  
Searching for '2019' in /home/ramakrishna\_pudota/CS131...  
/home/ramakrishna\_pudota/CS131/2019-01-h1.csv


\2. Search for files by type -  

ramakrishna\_pudota@instance-20250203-032935:~/CS131/a2$ ./findsort.sh ~/CS131 --type csv  
Searching for .csv files in /home/ramakrishna\_pudota/CS131...  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-2.0.csv  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-4.0.csv  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-1.0.csv  
/home/ramakrishna\_pudota/CS131/2019-01-h1.csv  
/home/ramakrishna\_pudota/CS131/sample1/ws3csvs/jan2\_data.csv  
/home/ramakrishna\_pudota/CS131/sample1/ws3csvs/jan10\_data.csv  


\3. Search for files by content -  

ramakrishna\_pudota@instance-20250203-032935:~/CS131/a2$ ./findsort.sh ~/CS131 --content "vendor"  
Searching for 'vendor' inside files in /home/ramakrishna\_pudota/CS131...  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-2.0.csv  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-4.0.csv  
/home/ramakrishna\_pudota/CS131/ws4/2025-03-07-02:26:06-1.0.csv  
/home/ramakrishna\_pudota/CS131/ws4/reorg.sh  
/home/ramakrishna\_pudota/CS131/2019-01-h1.csv  
/home/ramakrishna\_pudota/CS131/ws2/ws2.txt


\4. Organize files - 
ramakrishna\_pudota@instance-20250203-032935:~/CS131/a2$ ./findsort.sh ~/CS131/sample1 --sort  
Sorting files in /home/ramakrishna\_pudota/CS131/sample1...  
Scripts: sh files found.  
/home/ramakrishna\_pudota/CS131/sample1/long.sh  
Data: csv files found.  
/home/ramakrishna\_pudota/CS131/sample1/ws3csvs/jan2\_data.csv  
/home/ramakrishna\_pudota/CS131/sample1/ws3csvs/jan10\_data.csv  
Documents: txt files found.  
/home/ramakrishna\_pudota/CS131/sample1/sample3.txt  
/home/ramakrishna\_pudota/CS131/sample1/aa.txt  
/home/ramakrishna\_pudota/CS131/sample1/b.txt  
/home/ramakrishna\_pudota/CS131/sample1/g.txt  
/home/ramakrishna\_pudota/CS131/sample1/sorted\_data.txt  
/home/ramakrishna\_pudota/CS131/sample1/temp2/sample.txt  
/home/ramakrishna\_pudota/CS131/sample1/result.txt  
/home/ramakrishna\_pudota/CS131/sample1/aa123.txt  
/home/ramakrishna\_pudota/CS131/sample1/sample2.txt  
/home/ramakrishna\_pudota/CS131/sample1/results.txt  
/home/ramakrishna\_pudota/CS131/sample1/sample.txt  
/home/ramakrishna\_pudota/CS131/sample1/exercise.txt  
/home/ramakrishna\_pudota/CS131/sample1/datafile.txt  
/home/ramakrishna\_pudota/CS131/sample1/a.txt  
/home/ramakrishna\_pudota/CS131/sample1/notes/26thFeb.txt  
/home/ramakrishna\_pudota/CS131/sample1/error.txt  
Move files? (y/n): y  
Files sorted.
