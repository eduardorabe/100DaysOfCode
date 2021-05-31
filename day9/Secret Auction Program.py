# 100 Days of Code
# DAY 9
# Created by eduardorabe
# Secret Auction Program

from art import logo
from subprocess import call

bid_dict = {}
want_to_continue = True
higher_bid_key = ""

while want_to_continue:
    print(logo)
    name = str(input("What is your name? "))
    user_bid = int(input("What's you bid? $"))
    bid_dict[name] = user_bid

    cont = ""
    while cont.lower() != "yes" and cont.lower() != "no":
        cont = input("Do you want to continue? Yes or no ")
    if cont.lower() == "no":
        want_to_continue = False
        call("clear")
for key in bid_dict:
    if higher_bid_key == "":
        higher_bid_key = key
    elif bid_dict[key] > bid_dict[higher_bid_key]:
        higher_bid_key = key
print(f"The auction winner is {higher_bid_key} and the bid amount was ${bid_dict[higher_bid_key]}")
