import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','+','&','*','(',')']
print("Welcome to password Generator!!")
ip_letters=int(input("How many letters do you like in your password: \n"))
ip_symbols=int(input("How many symbols do you like in your password: \n"))
ip_numbers=int(input("How many numbers do you like in your password: \n"))
password=[]
for _ in range(1,ip_letters+1):
    password.append(random.choice(letters))
    #print(random_char,end="")
for _ in range(1,ip_symbols+1):
    password.append(random.choice(symbols))
    #print(random_sym,end="")
for _ in range(1,ip_numbers+1):
    password.append(random.choice(numbers))
    #print(random_num,end="")

random.shuffle(password)

newPassword=""
for i in password:
    newPassword+=i
print(f"Your password is {newPassword}")
