import json
from difflib import get_close_matches

filename = './data.json'

with open(filename) as f_obj:
            words = json.load(f_obj)
print(type(words))
def translate_word(w):
    w = w.lower()
    if w in words:
        return words[w]
    elif w.title() in words:
        return words[w.title()]
    elif w.upper() in words:
        return words[w.upper()]
    elif len(get_close_matches(w, words.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, words.keys())[0])
        if yn.lower() == "y":
            return words[get_close_matches(w, words.keys())[0]]
        elif yn.lower() == "n":
            return "The word does not exists"
        else:
            return "Invalid input"
    else:
        return "Word not in dictionary - please double check it."

wordin = input("Enter a word: ")
wordout = translate_word(wordin)
if type(wordout) == list:
    for i in wordout:
        print(i)
else:
    print(wordout)