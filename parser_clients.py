# Timelog Parser 1.1 for Client Work by Timothy Grindall

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

debug = True

import sys

filename = sys.argv[1]
total_minutes = 0
num_totals = 0

with open(filename) as file:
	#find number of totals in timelog
	for line in file:
		print('entered first loop')
		if (line == '\n'):
			if (debug == True):
				print('empty line!')
				#skip empty line
		else:
			line_array = line.split()

			if (line_array[0] == 'total:'):
				# print('found "total" line')
				num_totals += 1

	#iterate through lines again to add up time
	index = 0	# index for how many times we have seen 'total:' so far

with open(filename) as file:
	#go through file again and get totals
	for line in file:
		print('entered second loop')
		if (line == '\n'):
			if (debug):
				print('empty line!')
		else:
			#read next line
			#split line into array
			line_array = line.split()

			if (line_array[0] == 'total:'):
				if (debug):
					print('\nfound a total')
				index += 1

			print('\nnum_totals: ' + str(num_totals))
			print('\nindex: ' + str(index))

			if (index == num_totals):	#found last total
				print('\nbegin adding up totals')
				# begin adding up totals

				if (line_array[0] != 'Sunday:' and line_array[0] != 'Monday:' and line_array[0] != 'Tuesday:' and line_array[0] != 'Wednesday:' and line_array[0] != 'Thursday:' and line_array[0] != 'Friday:' and line_array[0] != 'Saturday:'):
					#continue as usual
					skip = False	# why use this variable? in case we add more use cases

					if (line == '<need this last line>'):
						skip = True

					#only adding up time for one subject so skipping checking for subject
					if (skip == False):

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

							total_minutes = total_minutes + hours * 60 + minutes

#print out debugging info for finding "total" line
print('\n\nnumber of times "total:" was found: ' + str(num_totals) + ' times')

#print out total time
print('\n\nminutes: ' + str(total_minutes))
print('\ntotal: ' + get_time_string(total_minutes))