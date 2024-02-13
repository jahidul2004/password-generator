import random

small_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

capital_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number = ['1','2','3','4','5','6','7','8','9','0']

symbol = ['!','@','#','$','%','^','&','*','(',')','-','+','/']


password = []


for i in range(1,4):
    password.append(random.choice(small_letter))
for i in range(1,4):
    password.append(random.choice(capital_letter))
for i in range(1,4):
    password.append(random.choice(number))
for i in range(1,4):
    password.append(random.choice(symbol))
shufle=random.shuffle(password)

strpass = ''
for i in password:
    strpass = strpass+i
print(f"Password is: {strpass}")