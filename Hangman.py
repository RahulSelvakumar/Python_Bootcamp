import random
word_List=['apple','orange','bananna']
word=random.choice(word_List)
guess=input('Guess a lowercase character: ')
length=len(word)
blank="_"*length
print(blank)
i=0
while i<length:
    if guess in word[i]:
        print("Right Guess")
        blank[i].replace(blank[i],guess)
    else:
        print("wrong guess")
    i+=1
    print(blank)
    
    