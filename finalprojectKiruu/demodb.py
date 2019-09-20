import sqlite3


def createTable():
    connection = sqlite3.connect('miniproject.db')

   # connection.execute("DROP TABLE IF EXISTS ")
    ce = """CREATE TABLE NewAttendance(
                 classNm TEXT,StuRollno INT NOT NULL,
                 Months TEXT NOT NULL,
                 TotalLectures INT NOT NULL,
                 AttendedLectures INT NOT NULL
                )"""
    connection.execute(ce)
    connection.commit()







    connection.close()



createTable()
