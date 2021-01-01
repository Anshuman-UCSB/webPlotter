import json

with open('data.csv', "a") as file:
	data = {'x':4, 'y':5}
	file.write(f"{data['x']}, {data['y']}\n")
	
with open('data.csv') as file:
	print(file.read())