import json

data= json.load(open("data.json"))

print("The definition d of the word is")
print(data["rain"])