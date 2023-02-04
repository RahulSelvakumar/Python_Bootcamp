import random
names=input('Enter all the names: ').split(',')
size=len(names)
print(size)
n=random.randint(0,size-1)
print(f"{names[n]} should pay the bill")