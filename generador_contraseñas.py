import random
import string 

length = int(input("Enter the length you want for your password"))

generator = string.ascii_letters + string.digit + string.punctuation

generated_password = ''.join(random.choice(generator) for x in range(length))

print(f"Your password is {generated_password}")
