import sqlite3

class Traffic:

	def __init__(self):
		self.connection = sqlite3.connect("traffic.db")

		self.cursor = self.connection.cursor()

	def createTable(self):
		self.cursor.execute(""" CREATE TABLE traffic_event(
			id INTEGER PRIMARY KEY,
			user_id VARCHAR(256),
			room_id VARCHAR(4),
			io VARCHAR(1),
			time INTEGER
			) """)

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def insertEvent(self, info_list):
		self.cursor.execute(" INSERT INTO traffic_event(user_id,room_id,io,time) VALUES (?,?,?,?) ",
			 (info_list[0], info_list[1], info_list[2], info_list[3]) )

		self.connection.commit()

	def selectRows(self):
		self.cursor.execute("SELECT * FROM traffic_event")

		return self.cursor.fetchall()

	def selectUsersofRoom(self, room_id):
		self.cursor.execute("SELECT user_id FROM traffic_event WHERE room_id=?", (room_id,) )

		return self.cursor.fetchall()

	def selectTimes(self, room_id, user_id, io):
		self.cursor.execute(""" SELECT time FROM traffic_event 
			WHERE room_id=? AND user_id=? AND io=? """, (room_id,user_id,io))

		return self.cursor.fetchall()


if __name__ == "__main__":
	my_database = Traffic()
	my_database.createTable()
	my_database.closeConnection()