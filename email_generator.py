import json
import string
import random

def email_generator(name1, name2, extension):
    email_extra = ''.join(random.choice(string.digits))
    email = name1.lower() + '.' + name2.lower() + email_extra + extension
    return email

def save_emails(mail_list, file_name):
    with open(f"{file_name}.txt", "w") as f:
        f.write('---Email Saved---\n')
        for k in range(len(mail_list)):
            f.write(f'email {k+1} : {mail_list[k]}\n')

names = json.loads(open('name.json').read())

email_count = int(input("How many emails do you want ? : "))
email_extension = input("Please enter an email extension : ")
email_list = []

for i in range(email_count):
    generated_email = email_generator(random.choice(names), random.choice(names), email_extension)
    print(f"email {i+1} : {generated_email}")
    email_list.append(generated_email)

is_saving_emails = input("do you want to save the emails in a file ? (y/n) : ")

if is_saving_emails.lower() == 'y':
    file_name_input = input('enter file name : ')
    save_emails(email_list, file_name_input)
