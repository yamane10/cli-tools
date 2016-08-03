def query_select(question, choices, default=None, max_columns=3, multi=True):
	number_of_choices = len(choices)
	columns = []
	longest_choice = sorted(choices, key=lambda c: len(c), reverse=True)[0]
	
	while True:
		number_of_rows = number_of_choices // max_columns
		modulus = number_of_choices % max_columns
		if modulus == 0:
			break
		elif max_columns - modulus > 1:
			max_columns -= 1
		elif max_columns > number_of_choices:
			max_columns = number_of_choices
		else:
			break

	column = []
	count = 0
	choice_number = 1
	choice_dict = {}
	while len(choices) > 0:
		choice = choices.pop(0)
		choice_dict[choice_number] = choice
		column.append((choice_number, choice))
		count += 1
		choice_number += 1
		
		if count == number_of_rows:
			if modulus > 0:
				choice = choices.pop(0)
				choice_dict[choice_number] = choice
				column.append((choice_number, choice))
				count = 0
				choice_number += 1
				modulus -= 1
				
				columns.append(column)
				column = []
			else:
				count = 0
				columns.append(column)
				column = []
	if len(column) > 0:
		columns.append(column)
		
	print(question)
	
	for i in range(len(columns[0])):
		row = []
		for column in columns:
			try: row.append(column[i])
			except: pass
		print("\t".join(["{}) {}".format(str(number).rjust(2), choice).ljust(len(longest_choice)) for (number, choice) in row]))
	
	plural = ''
	if multi:
		print("\nYou can enter multiple selections by giving a comma-separated (e.g. 1, 5)")
		plural = "(s)"
	selections = input("Enter selection{} (by number): ".format(plural))
	
	valid_choice = False
	while not valid_choice:
		valid_choice = True
		
		if (not multi) and (len(selections.split(',')) > 1):
			selections = input("ERROR: Please make only one selection: ")
			break
		else:
			try:
				for selection in selections.split(','):
					if int(selection.strip(' ')) not in choice_dict:
						selections = input("ERROR: selection {} not a valid choice. Please enter again: ".format(selection))
						valid_choice = False
						break
					else:
						break
			except:
				selections = input("ERROR: selection {} not a valid choice. Please enter again: ".format(selection))
				valid_choice = False
	if multi:
		output = [choice_dict[int(selection.strip(' '))] for selection in selections.split(',')]
	else:
		output = choice_dict[int(selections.strip(' '))]

	return output