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

print(f"your love percentage is {true}{love}%")

