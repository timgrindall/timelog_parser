# Timelog Parser 1.0 by Timothy Grindall
# 	This script parses a timelog (which uses a certain format for the log entries, one per line) and compiles a list of totals for each subject (subjects must be programmed in seperately).
#
# Features I could add to this script:
#	- subject combination: combine subjects that are basically the same thing and output a new combined subject in addition to the ones I already have (requires some work)
#	- Date/Time Stamping taken from input file
#	- Pass filename as a command line argument
#	- Pass line from file to error handler when there is an error

def get_time_string(minutes):
	hours = minutes // 60

	remainder = minutes % 60

	minutes_int = int(remainder)

	if (minutes_int < 10):
		minutes_str = '0' + str(minutes_int)
	elif (minutes_int >= 10):
		minutes_str = str(minutes_int)

	hours_int = int(hours)

	time_string = ''.join([str(hours_int), ':', minutes_str])

	return time_string

import re
numeric_reg = re.compile(r'\D')

debug = False # Set to True to get verbose output for each and every line. Set to False to minimize output for regular use

import sys

filename = sys.argv[1]

subject_names = ['Programming', 'Web Development', 'Web Design', 'Film Scoring', 'Video Editing', 'Screenwriting', 'Music Composition', 'Outside Work', 'Sound Mixing', 'Bible Study', 'Editing', 'Watching', 'Looking for Work', 'IT Work', 'Color Grading', 'UpWork', 'Songwriting', 'Filmmaking', 'Photography', 'Other', 'Writing']
combined_subjects = ['Programming', 'Video Editing', 'Music Composition', 'Web Development', 'Looking for Work']
combined_indexes = [[0, 1, 2],[4, 8, 10, 14], [3, 6, 16], [1], [12, 15]]

total_minutes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]	# don't forget to update total_minutes to reflect number of items in subject_names array!

with open(filename) as file:
	for line in file:
		if (line == '\n'):
			if (debug == True):
				print('empty line!')
				#skip empty line
		else:
			line_array = line.split()

			if (line_array[0] != 'Sunday:' and line_array[0] != 'Monday:' and line_array[0] != 'Tuesday:' and line_array[0] != 'Wednesday:' and line_array[0] != 'Thursday:' and line_array[0] != 'Friday:' and line_array[0] != 'Saturday:'):
				#continue as usual

				if (debug == True):
					print(line)
				
				for index in range(len(subject_names)):
					if (line_array[0] == (subject_names[index] + ':') or (line_array[0] + ' ' + line_array[1]) == (subject_names[index] + ':')):
						skip = False
						numeric = True

						if (debug == True):
							print("line_array[-1]: " + line_array[-1])

						match = numeric_reg.match(line_array[-1])
						if match:
							numeric = False
						else:
							numeric = True

						for word in line_array: # had to do to avoid list index out of range error
							if (word == 'total:'):
								# skip line
								skip = True
							elif (word == 'Note:'):
								# skip line
								skip = True

						if (skip == False and numeric == True):
							#add to total for name at index 0

							if (line[-2] == '?'):
								print('question mark found!')
								#add zero to total
							elif (line[-2] != '?' and line[-2] != ')'):
								#process as normal
								time_string = line[-5:-1]

								if (debug == True):
									print(time_string)

								hours_str = line[-5]
								minutes_str = line[-3:-1]

								if (debug == True):
									print('hours: ' + hours_str)
									print('minutes: ' + minutes_str)

								hours = int(hours_str)
								minutes = int(minutes_str)

								total_minutes[index] = total_minutes[index] + hours * 60 + minutes

# print out totals
print('\n\nSubject totals for \"' + filename + '\":\n')

for index in range(len(total_minutes)):
	print('\nindex: ' + str(index))
	print('\nminutes:' + str(total_minutes[index]))

	print('total time for ' + subject_names[index] + ': ' + get_time_string(total_minutes[index]))

print('\n\nCombined totals/subjects:\n')

#print out combined totals
for index in range(len(combined_subjects)):
	minutes = 0
	# print('\ntotals for ' + combined_subjects[index] + ":")

	for item in combined_indexes[index]:
		minutes = minutes + total_minutes[item]

	if (debug == True):
		print('\nindex: ' + str(index))
	else:
		pass
	print('\nminutes: ' + str(minutes))

	print('total time for ' + combined_subjects[index] + ": " + get_time_string(minutes))

