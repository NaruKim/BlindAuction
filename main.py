from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)
bid={}
yes='yes'

while not yes=='no':
  name = input("Como te llamo?: ")
  offer = int(input("Cuanto ofreceras?: "))
  bid[name]=offer
  yes = input("Hay otro?: ")
  clear()

highest_name=""
highest_offer=0
for i in bid:
  if highest_offer<bid[i]:
    highest_name=i
    highest_offer=bid[i]
print(f"{highest_name} gana {highest_offer}")