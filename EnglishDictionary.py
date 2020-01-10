import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):#w is short for word
    w = w.lower()#in case someone types the word in capitals then they can still receive the word back
    if w in data: 
        return data[w]
    elif w.title() in data:#makes sure proper nouns are properly written because grammar is important
        return data[w.title()]
    elif w.upper() in data:#makes sure acronyms are all capital because grammar is important
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:#measures the ratio of how close a typed word is to an actual word in the dictionary
        yn = input("Did you mean %s instead of that jibberish you just typed in? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":#yn means "yes no"
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Well, according to this dictionary, the word you typed in is nonsense. Try typing an actual word, this time."
        else:
            return "I have no idea what crazy talk you just tried to type in here. Just try typing the word again."
    else:
        return "You typed in jibberish. Try typing a real word."

word = input("Enter a word into Evan's Dictionary that you would like to look up today: ") 

output = translate(word)

if type(output) == list:#makes sure that the strings returned by the translate function aren't wonky from the code on lines 26-29
    for item in output:#makes sure each definition is printed in a different row. Makes it look organized
        print(item)
else:
    print(output)
    