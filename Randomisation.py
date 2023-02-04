import random
test_seed=int(input("Enter the seed number: "))
random.seed(test_seed)
toss=random.randint(0,1)
if toss==0:
    print("Heads")
else:
    print("Tails")