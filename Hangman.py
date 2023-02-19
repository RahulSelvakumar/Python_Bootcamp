import random
word_List=['apple','orange','bananna']
word=random.choice(word_List)
guess=input('Guess a lowercase character: ')
print(word)
for letter in word:
    if letter==guess:
        print("Right Guess")
    else:
        print("wrong guess")
    
    