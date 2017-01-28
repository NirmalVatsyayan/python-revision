user_input = input("Enter a value !! : ")

try:
    user_input = int(user_input)
    difference = 100 - user_input
    print(difference)
except:
	print("Invalid input !!")