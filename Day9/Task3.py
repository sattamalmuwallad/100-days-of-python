from art import logo
print(logo)
# TODO-1: Ask the user for input
def high_bidder(record):
    high_bid = 0 
    winner = ""
    for bid in record:
        if record[bid] > high_bid:
            high_bid = record[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of ${high_bid}")
# TODO-2: Save data into dictionary {name: price}
data = {}
cont_bidding = True
while cont_bidding :
    name = input("what is your name? ")
    price = float(input("What is your bid? "))
    data[name] = price
    bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    if bidders.lower()== 'no':
        cont_bidding = False
        high_bidder(data)
    elif bidders.lower()== "yes":
        print("\n" * 20)
    
    


# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

    