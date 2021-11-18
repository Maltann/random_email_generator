import json
import string
import random

def email_generator(name1, name2, extension):
    email_extra = ''.join(random.choice(string.digits))
    email = name1.lower() + '.' + name2.lower() + email_extra + extension
    return email

names = json.loads(open('name.json').read())

email_count = int(input("How many emails do you want ? : "))
email_extension = input("Please enter an email extension : ")
for i in range(email_count):
    print(f"email {i+1} : {email_generator(random.choice(names), random.choice(names), email_extension)}")