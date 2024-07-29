import os
from art import logo

print(logo)


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


bids = {}
bidding_finished = False


def find_bidder(bidding_rec):
    highest_bid = max(bidding_rec.values())
    winner = ""
    for bidder, bid_amount in bidding_rec.items():
        if bid_amount == highest_bid:
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    to_continue = input("Are there anyone else to bid? yes or no.\n")
    if to_continue.lower() == "no":
        bidding_finished = True
        find_bidder(bids)
    elif to_continue.lower() == "yes":
        clear_screen()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Thank you for participating in the auction!")
