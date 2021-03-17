from difflib import SequenceMatcher

# Function that counts out the change using different denominations, takes in the change to be issued as a parameter
# Goal is to minimize the number of coins given as change 
def countCurrency(amount): 
      
	notes = [200,100,25,10,5] 
	change_dict = {}			# Dictionary to store the change issued
	i = 0
	while i < len(notes):
		key = "$" + str(notes[i]/100)  # Key of denominations for the change dictionary
		if(amount == 0):
			break

		# Checks if change is a multiple of the highest denomination of coins
		if(amount%notes[i] == 0):
			if key not in change_dict:
				change_dict[key] = amount/notes[i]
			else:
				change_dict[key] = change_dict[key]+(amount/notes[i])
			break

		else:
			if(amount >= notes[i]):
				amount = amount - notes[i]
				if key not in change_dict:
					change_dict[key] = 1
				else:
					change_dict[key] = change_dict[key]+1

		# If the change is greater than highest denomination of notes, issue the highest denomination of change again
		if(amount > notes[i]):
			i = notes.index(notes[i])
		else:
			i = i+1

	print("\nPlease collect your change. You should have the following denominations:")
	for item in change_dict:
		print(item ,"->",int(change_dict[item])," coins")
 
def main():
	print("*" *19,"VENDING MACHINE","*"*19)
	print("Welcome to the vending machine! Here are the options available ")
	print("\nCandy Bar -> $2")
	print("Chips -> $1.5")
	print("Soda -> $1")

	items_list = {"Candy Bar":200,"Chips":150,"Soda":100}
	cost = 0 # Total cost of items
	change = -1 # Total change to be dispensed
	selection={} # Items selected
	while(True):
		food_item = input("\nPlease enter your choice : ")
		quantity = input("Please enter the quantity needed for item selected : ")

		for item in items_list:
			# SequenceMatcher accounts for typos in the input
			# For example, if the input is chibs, the system knows to interpret that as Chips
			if((SequenceMatcher(None, food_item, item).ratio())>0.5):
				cost = cost + (items_list[item]*int(quantity))
				selection[item] = quantity
				print("Thank you for choosing the",item)
				decision = input("Would you like to choose another item? [Y or N]: ")
				break

		# If non-menu items are chosen
		if (cost==0):
			print("Please enter a valid choice on the menu.")

		if(decision=="N") or (decision=="n") or (decision=="no"):
			break
		
	print("\nHere are the selected items.")
	for item in selection:
		print(item ,"-> Quantity:",selection[item])

	print("\nYour total is $",cost/100)
	# Ideally, the system should recognise the denominations of notes/coins fed into vending machine and return the change accordingly
	while(change < 0):
		
		total_money = float(input("\nPlease enter the amount of money fed into the vending machine: "))
		change = (total_money*100) - cost

		if(change < 0):
			print("\nPlease feed enough money into the machine.")

	print("\nThe change is $",change/100)

	# If exact money is fed into the machine
	if(change==0):
		print("\nThank you. You can now collect your order.")
	else:
		countCurrency(change)


	
main()