import random
word_List=['apple','orange','bananna']
word=random.choice(word_List)
guess=input('Guess a lowercase character: ')
print(word)
i=0
while i<len(word):
    if guess in word[i]:
        print("Right Guess")
    else:
        print("wrong guess")
    i+=1
    