#from art import auction
#print(auction)
replit import clear
list_of_bidders = []      
def auction(name_of, amount):
    bidders = {}
    bidders["name"] = name_of
    bidders["bidding_amount"] = amount
    list_of_bidders.append(bidders)
    clear()                                       # since i have been using replit as compiler i have imported clear method from replit ...use can use your own     
last_bidder = False  
while not last_bidder:
    name = input("Enter the name of the bidder: ")
    bidding_amount = int(input("Enter your bidding amount: "))
   
    auction(name_of=name, amount=bidding_amount)
    next_bidder = input("Type 'yes' if there is another bidder or 'no' if you are the last one to bid: ").lower()
   
    if next_bidder == 'no':
        last_bidder = True
        highest_bid = 0
        for bidder in list_of_bidders:
          bids = bidder["bidding_amount"]
          if bids>highest_bid:
            highest_bid = bids
    
        print(f'The highest_bid is bid by {bidder["name"]} : {highest_bid}')
          
          
          
        
          
