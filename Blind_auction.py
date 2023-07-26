from replit import clear
#Blind auction 
bidders = [
    {
            "Bidders": "",
            "Bid":""
    },
           ]



print("Welcome to the secret auction. Tell no one!")
name = input("What is your name? ")

bid = input("What is your bid?: £")

query = input("Are there any other bidders partaking? ")


def add_new_bidder(Users = name, BiddingAmount = bid):
    new_bidder = {}
    new_bidder["Bidders"] = name
    new_bidder["Bid"] = bid
    bidders.append(new_bidder)

add_new_bidder(name,bid)

print(bidders)

#if Query == yes:
#    clear()
    


