import json
from difflib import get_close_matches


data= json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "paris" this will check for "Paris" as well.
        return data[word.title()]
    elif len(get_close_matches(word,data.keys())) >0:
        confirmation=input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead? Y or N?: ").lower()
        if confirmation=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif confirmation=="n":
            return f"The word {word} doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return f"The word {word} doesn't exist. Please double check it."



input_word=input("Enter a existing word: ")
output= translate(input_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)