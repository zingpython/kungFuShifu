from model import Traffic
from view import View

my_database = Traffic()

my_view = View()

with open("traffic.txt", "r") as traffic_file:
	lines = traffic_file.readlines()

	for line in lines:
		line = line.strip().split(" ") 

		line[3] = int(line[3])

		my_database.insertEvent(line)

traffic_information = my_database.selectRows()

room_list = []

for row in traffic_information:
	room_list.append( row[2] )

room_list = set(room_list)

room_visitors = {}

for room in room_list:
	user_list = my_database.selectUsersofRoom(room)

	user_list =set(user_list)

	room_visitors[room] = user_list

room_times = {}

for room in room_list:
	time_difference = []
	for user in room_visitors[room]:
		enter_times = my_database.selectTimes(room, user[0],"I")
		exit_times = my_database.selectTimes(room,user[0],"O")

		for index in range(len( enter_times )):
			time_difference.append( exit_times[index][0] - enter_times[index][0] )

	room_times[room] = time_difference

print(room_times)