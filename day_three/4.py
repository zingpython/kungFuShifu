with open("traffic.txt", "r") as traffic_file:
	new_lines = []

	#Get each line as a list of lists
	for line in traffic_file.readlines():
		new_lines.append( line.strip().split(" ") )

	
	dict_room_visitors = {}

	#FOr each room get all unique visitors
	for line in new_lines:
		#Check if room is in dict_room_visitors already
		room = dict_room_visitors.get( line[1], False )

		#If room is not in dict add it to dict with the value of the current visitor
		if room == False:
			dict_room_visitors[ line[1] ] = [ line[0] ]
		#If the room is in the dict and the visitor is not already in the room add the user to the list
		else:
			if line[0] not in dict_room_visitors[ line[1] ]:
				dict_room_visitors[ line[1] ].append( line[0] )


	dict_room_times = {}

	#For each room get time each visitor spent in room
	#FOr each room
	for room in dict_room_visitors.keys():
		#FOr each unique visitor in that room
		for visitor in dict_room_visitors[room]:
			#Get the enter and exit times of that user in that room
			enter_time = []
			exit_time = []
			#Go through each line of new_lines and find any lines that match the current visitor and the current room
			for line in new_lines:
				if line[0] == visitor and line[1] == room:
					#If enter time add to enter_time list as an integer
					if line[2] == "I":
						enter_time.append( int(line[3]) )
					#If exit time add to exit_time list as an integer
					else:
						exit_time.append( int(line[3]) )

			#If this visitor only enters the room once find the difference in times and add that time to the dict_room_times
			if len(enter_time) == 1 and len(exit_time) == 1:
				time_in_room = exit_time[0] - enter_time[0]
				
				if dict_room_times.get(room, False) == False:
					dict_room_times[room] = [time_in_room]

				else:
					dict_room_times[room].append(time_in_room)

			#If visitor entered the room multiple times find the length of each time he/she entered and exited the room 
			else:
				#By sorting both lists we know that each index matches the exit/enterance time of the other list
				enter_time.sort()
				exit_time.sort()

				#For each entry in enter_time find the difference and add it to the dict_room_time dictionary
				for index in range( len(enter_time) ):
					time_in_room = exit_time[index]- enter_time[index]

					#If room is not in dictonary add that room to the dictionary with the value of a list with time_in_room as it's only value
					if dict_room_times.get(room, False) == False:
						dict_room_times[room] = [time_in_room]

					#If room already exisits in dict_room_times add time_in_room to that room's list
					else:
						dict_room_times[room].append(time_in_room)

	# Output rooms in proper formatting
	for room in sorted(dict_room_times.keys()):
		#Get the number of unique visitors in a room
		unique_visitors = len( dict_room_visitors[room] )
		#Find the average time spent in a room
		average = sum( dict_room_times[room] ) // len(dict_room_times[room])
		print("Room "+room+", "+ str(average) +" minute average visit, "+ str(unique_visitors)+" visitor(s) total")