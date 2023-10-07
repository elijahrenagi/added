import random
 
def main():
 
    quantity = float(input("Enter a number to randomly create a word:"))
    tense = (input("Please enter a tense - past|present|future:"))
    sentence = get_determiner (quantity)
    print (f"{sentence}")
    noun = get_noun (quantity)
    print (f"{noun}")
    verb = get_verb(quantity, tense)
    print (f"{verb}")
    
 
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
        words = ["bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = [ "birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word        
    return words
 
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
        
    word = random.choice(words)
    return word  
                        
main()
