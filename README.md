import requests

def trace(*args):
  """Used for debug output"""
  print (*args)  # Comment out this line to remove debug output
  pass

"""# This base URL works, but doesn't return anything too interesting
# After running this script, read https://www.boredapi.com/ and
# figure out how to change it to get back a filtered activity.
# The filter is up to you: number of people, category, price, etc.
# Tip: try testing the API URLs directly in a browser first
URL = "https://www.boredapi.com/api/activity"

# Get data from the web site and put it into Python collections
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
trace ("\nText returned:", response.text)"""
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
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

people = "person" if data["participants"] == 1 else "people"
price = data["price"] * 100
price = str(price)

accessibility = data["accessibility"] * 100
accessibility = str(accessibility)
sentence1 = "It also has a great accessibility rate of " if data["accessibility"]>0.5 else "It does however have a mediocre accessibility rate of "

# See what the raw data looks like
trace ("\n You should", data["activity"] + ". It only takes", data["participants"], people, "and only costs $" + price + "!", sentence1,  accessibility + "% Go have fun!")