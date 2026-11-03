# Função input()

# ~ message = input("Tell me your name, please: ")
# ~ print("\n"+message+"\n")

# ~ prompt = "What do work daily? "
# ~ prompt += "Ok?: "

# ~ job = input(prompt)
# ~ print("\n" + job + " is a good area!\n")

# ~ # Operador de módulo %

# ~ number = input("Enter an number: ")
# ~ number = int(number)

# ~ if number % 2 == 0:
	# ~ print("Even number: " + str(number))
# ~ else:
	# ~ print("Odd number: " + str(number))

# Laços while

# ~ current_number = 1
# ~ while current_number <= 5:
	# ~ print(current_number)
	# ~ current_number += 1
	
prompt = "\n Tell me someyhing that I will repeat:"
prompt += "\n Enter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)
	print(message)
	

