print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

tip = bill / people * tip_percentage / 100
pay =  bill / people + tip

pay = round(pay, 2)

print(f"If the bill was {bill}, spilt between {people}, with {tip_percentage};\nThen each person should pay {pay}")
