def highest_bidder(auction):
    highest_name = max(auction, key=auction.get)
    highest_amount = auction[highest_name]
    print(f"The highest bidder is {highest_name} bid is amount is : ${highest_amount}.")

auction={}
should_con=True
while should_con:
    name=input("what is your name:\n")
    amount=int(input("enter your bid amount:\n"))


    auction[name]=amount

    continue_bid=input(" is there any bidders type 'yes' or 'no'\n")
    if continue_bid == "no":
        highest_bidder(auction)
    elif continue_bid == "yes":
        print("\n" * 30)
    else:
        print("you type a wrong answer")
        should_con = False
        highest_bidder(auction)


