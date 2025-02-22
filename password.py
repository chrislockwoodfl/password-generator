import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!\nI will create a random password for you.")
try:
    num_letters = int(input("How many letters would you like in your password?\n"))
except ValueError:
    print("Please ender a va;id number") 
    num_letters = 0   

try:    
    num_symbols = int(input(f"How many symbols\n"))
except ValueError:
    print("Please ender a va;id number") 
    num_symbols = 0   
    
try:    
    num_digits = int(input(f"How many digits?\n"))
except ValueError:
    print("Please ender a va;id number") 
    num_digits = 0   

# Create password with desired number of characters
password = ""
for i in range(num_letters):
    j = random.randint(0, len(letters)-1)
    password += letters[j]

for i in range(num_symbols):
    j = random.randint(0, len(symbols)-1)
    password += symbols[j]

for i in range(num_digits):
    j = random.randint(0, len(digits)-1)
    password += digits[j]

#print(password)

# Rearrange password characters in random order
final_password = ""

while len(password) > 0:
    i = random.randint(0,len(password)-1)
    #print(i)
    final_password += password[i]
    password = password.replace(password[i], "", 1)

print("Your new password is " + final_password)





