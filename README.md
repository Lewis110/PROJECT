This program helps you find something to do if you're bored. It relies on Bored API at https://www.boredapi.com/ .

* Probably don't print "Calling..."
* Drop lines 8-22
* Decapitalize the first letter of action OR change the phrasing to: Here's an idea! <action>
* don't mention the accessibility or price number directly
* accessibility rate -> accessibility rating
* "It does however " -> "Also, it does "
* Period after accessibility sentence
* sentence1 -> accessibilitySentence
* change price to describe in words

price = None
if price == 0:
  price = "free"
elif price < 0.25:
  price = "cheap"
elif .....:
else:
  price = "for richie riches"