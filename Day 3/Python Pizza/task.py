print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pay = 0

if size == "S":
    pay = 15
    if pepperoni == "Y":
        pay += 2
elif size == "M":
    pay = 20
    if pepperoni == "Y":
        pay += 3
elif size == "L":
    pay = 25
    if pepperoni == "Y":
        pay += 4

if extra_cheese == "Y":
    pay += 1
print(f"Your final bill is: ${pay}.")