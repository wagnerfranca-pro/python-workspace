cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars:
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())
print()

banned_users = ['andrew', 'caroline', 'david']
user = 'marie'
if user not in banned_users:
	print(user.upper())
print()

age = 100

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65: 
	price = 10
elif age >= 65:
	price = 5

print(str(price))
print()

