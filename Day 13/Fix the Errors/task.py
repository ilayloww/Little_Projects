try:
    age = int(input("How old are you?"))

except ValueError:
    print("You've typed in an invalid number. Please try again.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at the age of {age}.")
else:
    print(f"You can't drive at the age of {age}.")
