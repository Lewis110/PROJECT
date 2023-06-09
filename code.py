import requests

def trace(*args):
  """Used for debug output"""
  print (*args)  # Comment out this line to remove debug output
  pass

"""Change wording for Sentence"""

modificators = ["activity", "participants"]
modificator = input("Hi! I am here to help you find something to do. Please specify whether you want to choose by the 'activity' or 'participants': ")
while modificator not in modificators:
  modificator = input ("Try again: ")

suffix = None

if modificator == "activity":
  activities = ["recreational", "relaxation", "social", "cooking"]
  print ("Available activities:", activities)
  type = input("What type of activity would you like to do? ")
  while type not in activities:
    type = input("Try again: ")
  suffix = "type=" + type
  
elif modificator == "participants":
  participants = ["1", "2", "3", "4", "5", "8"]
  participant = input("How many people whould you like to be with? ")
  while participant not in participants:
    participant = input("Try again: ")
  suffix = "participants=" + participant

else: 
  print("Try again: ")

URL = "https://www.boredapi.com/api/activity?" + suffix

response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

people = "person" if data["participants"] == 1 else "people"

price = None
if data["price"] == 0:
  price = "free"
elif data["price"] < 0.25:
  price = "cheap"
elif data["price"] < 0.5:
  price = "moderately expensive"
elif data["price"] < 0.75:
  price = "quite expensive"
else:
  price = "very expensive"

accessibility = data["accessibility"] 
if accessibility == 1:
  AccessibilitySentence = "It does, however, have a terrible accessibility rating."
elif accessibility >0.75:
  AccessibilitySentence = "It does have a pretty bad accessibility rating."
elif accessibility > 0.5:
  AccessibilitySentence = "It also has an ok accessibility rating."
elif accessibility > 0.25:
  AccessibilitySentence = "It also has a pretty good accessibility rating."
else:
  AccessibilitySentence = "It also has a great accessibility rating."


# See what the raw data looks like
trace ("\n Here's an idea!", data["activity"] + ". It only takes", data["participants"], people + "! Its cost is " + price + ".", AccessibilitySentence,  "Thank you for using this program, and go have fun!")