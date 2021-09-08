import json

data= json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return f"The word {word} doesn't exist.Please double check it."



input_word=input("Enter a existing word: ")
print(translate(input_word))
