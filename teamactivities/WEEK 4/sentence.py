import random
 
def main():
    quantity = float(input("Enter a number to randomly create a word:"))
    tense = (input("Please enter a tense - past|present|future:"))
    
    sentence0 = make_sentence(quantity, tense)
    print(f"{sentence0.capitalize()}.")
    sentence1 = make_sentence(quantity, tense)
    print(f"{sentence1.capitalize()}.")
    sentence2 = make_sentence(quantity, tense)
    print(f"{sentence2.capitalize()}.")
    sentence3 = make_sentence(quantity, tense)
    print(f"{sentence3.capitalize()}.")
    sentence4 = make_sentence(quantity, tense)
    print(f"{sentence4.capitalize()}.")
    sentence5 = make_sentence(quantity, tense)
    print(f"{sentence5.capitalize()}.")
    sentence6 = get_prepositional_phrase(quantity)
    print(f"{sentence6.capitalize()}.")
    sentence7 = get_prepositional_phrase(quantity)
    print(f"{sentence7.capitalize()}.") 
    sentence8 = get_prepositional_phrase(quantity)
    print(f"{sentence8.capitalize()}.")


def make_sentence(quantity, tense):
    sent = get_determiner(quantity)
    sent1 = get_noun(quantity)
    sent2 = get_verb(quantity, tense)

    full = (f'{sent} {sent1} {sent2}')
    dot = full
    return (dot)
    
    
 
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
 
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
    
def get_noun(quantity):
    if quantity == 1:
        words = ["birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"]

    else:
        words = ["bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"]
    #randomly choose and return a noun
    word = random.choice(words)
    return word       
 
def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"]
            
    if tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"]
            
    if tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"]
            
    if tense == "future":
        words = [ "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"]
    #randomly choose and return a verb  
    word = random.choice(words)
    return word  
    #Adding get_proposition function and get_prepositional phrase function (WEEK 4 TASK)
def get_preposition():
    words = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    w1 = get_preposition()
    w3 = get_determiner(quantity)
    w4 = get_noun(quantity)

    pot = (f"{w1} {w3} {w4}")
    return pot
            
main()
