import sqlite3

connection = sqlite3.connect("spin.db")

table = "CREATE TABLE spins (id integer primary key, bet INTEGER, pay INTEGER, machine INTEGER)"

cursor = connection.cursor()
cursor.execute(table)
connection.commit()

