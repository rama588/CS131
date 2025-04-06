#Function to calculate the average 
function calc_avg(total, count) {
        return total/count
}

BEGIN {
        FS = ","
        header = 0 #Flag to skip the header.
        max_total = -1 #Initializing the highest score. Setting it to -1 so it is less than any real total and it will get updated by the first student's score.
        min_total = 1000 #Initializing the lowest score. Setting it to 1000 as it is more than any real total and any smaller number will update this value.
}

{
        if (header == 0) {
                subject_count = NF - 2  #Calculating the number of subjects.
                header = 1  #Marking the header as processed.
        }
        else {
                name = $2  #Student name in 2nd field
                total = 0

                #Looping through all subject scores.
                for (i = 3; i <= NF; i++) {
                        total += $i
                }

                avg = calc_avg(total, subject_count) #Calling the function to get the average.

                #Determinging pass/fail status based on average score.
		if (avg >= 70)
                        status = "Pass"
                else
                        status = "Fail"

		#Storing values in associative arrays 
                total_scores[name] = total
                avg_scores[name] = avg
                pass_status[name] = status

		#Updating top scorer if the total is higher than current maximum.
                if (total > max_total) {
                        max_total = total
                        top_stu = name
                }

		#Updating lowest scorer if the total is lower than the current minimum.
                if (total < min_total) {
                        min_total = total
                        bot_stu = name
                }
        }
}

END {
        print "Student Grade Report -"

	#Loop through each student and print their details.
        for (student in total_scores) {
		#Rounding average to two decimal places.
		average = int(avg_scores[student] * 100 + 0.5) / 100
                
		print ""
		print "Name:", student
	        print "Total:", total_scores[student]
	        print "Average:", average
	        print "Status:", pass_status[student]
        }

print ""
print ""
print "Top and Bottom Performers -"
print ""
print "Top Scorer:", top_stu, "(Total:", max_total")"
print "Lowest Scorer:", bot_stu, "(Total:", min_total")"
}
