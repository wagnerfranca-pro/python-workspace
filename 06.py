alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print()
print(alien_0['points'])
print()
print(alien_0)
print()
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print()
alien_0 = {}
alien_0['color'] = 'red'
alien_0['points'] = 10

print(alien_0)
print()
alien_0['color'] = 'yellow'
print(alien_0)
print()

alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
print()

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print(favorite_languages['sarah'].title())
print()

for name, language in favorite_languages.items():
	print(name.title() + "'s " + language.title())
print()	

for name in favorite_languages.keys():
	print(name.title())
print()

for name in sorted(favorite_languages.keys()):
	print(name.title())
print()

for language in sorted(favorite_languages.values()):
	print(language.title())
print()

for language in set(favorite_languages.values()):
	print(language.title())

user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
print()

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
print()

########

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens [:5]:
	print(alien)
print("...")
print(str(len(aliens)))

###############

