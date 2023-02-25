#Basic love calculator
total=0
print("Welcome to python Love Calculator ")
name1=input("Enter your name: ")
name2=input("Enter your love's name: ")
name1=name1.lower()
name2=name2.lower()
name=name1+name2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e1=name.count("e")
true=t+r+u+e1
l=name.count("l")
o=name.count("o")
v=name.count("v")
e2=name.count("e")
love=l+o+v+e2
love_percetage=str(true)+str(love)
love_percetage=int(love_percetage)
if love_percetage>10 and love_percetage<90:
    statement="Your are in a good relationship:-)"
elif love_percentage>90:
    statement="You have an unbreakable bond!! ;-)"
else:
    statement="Sorryyy try to improve your relationship:-("
print(f"your love percentage is {love_percetage}% {statement}")
