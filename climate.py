import sqlite3
import matplotlib.pyplot as plt
        
years = []
co2 = []
temp = []

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM ClimateData")

for row in cursor.fetchall():
	years.append(row[0])
	co2.append(row[1])
	temp.append(row[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()



