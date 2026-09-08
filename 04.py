cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
	print(car)
	print()
	print(car.title())
	print()

for value in range(0,5):
	print(value)
print()

numbers = list(range(0,6))
print(numbers)
print()

even_mumbers = list(range(2,11,2))
print(even_mumbers)
print()

squares = []
for value in range(0,11):
	squares.append(value**2) 
	
print(squares)
print()

# List comprehensions

squares = [value**3 for value in range(0,11)]
print(squares)
print()

# End list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print()
print(players[:4])
print()
print(players[2:])
print()
print(players[-3:])
print()
for player in players[0:]:
	print(player.title())
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print()
print(friend_foods)
print()
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print()
print(friend_foods)
print()

# Tuplas

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()

for dimension in dimensions:
	print(dimension)
print()

dimensions = (400,100)
for dimension in dimensions:
	print(dimension)
