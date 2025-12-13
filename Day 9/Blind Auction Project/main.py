import art
# TODO-1: Ask the user for input
print(art.logo)

answer = True
dictionary = {}

while answer:
    name = input("What's your name?")
    bid = int(input("What's your bid? $"))
    dictionary[name] = bid
    x = input("Are there other bidders? Yes or no.").lower()
    if x == "no":
        answer = False
        print("\n" * 100)
    else:
        print("\n" * 100)
x = 0
name = ""
for key in dictionary:
    if dictionary[key] > x:
        x = dictionary[key]
        name = key

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print(f"Highest bidder is {name}, with ${x}")
print(dictionary)
