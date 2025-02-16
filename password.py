print("password check")
current_value = 100000
target_value = 200000
months = 0
increment = 0.1
while current_value < target_value:
    current_value += (current_value*increment)
    months += 1
    print(months, '10 % increment ', round(current_value))

print('to reach the target value ', months, 'months', round(current_value))

total = 0
while True:
    num = int(input("Enter a number (or 0 to exit): "))
    if num == 0:
        break
    total += num
print("Total:", total)

s = 'Python 3.2'
c = n = 0
for ltt in s:
    if ltt.isalpha():
        c += 1
    elif ltt.isdigit():
        n += 1
    else:
        pass
print('characters', c)
print('digits ', n)

record = []
while True:
    try:
        roll = int(input("Enter your roll no :"))
        name = input("Enter your name: ")
        subject = input("Enter your Subject: ")
        marks = int(input("Enter your marks: "))
        data = [roll, name, marks, subject]
    except ValueError:
        print('roll no is numeric value ')
        continue
    record.append(data)
    choice = input("Do you want to continue (y:N) ").upper()
    if choice == 'N':
        break
print("printing records ")
for R in record:
    roll_no = R[0]
    name = R[1]
    marks = R[2]
    subject = R[3]
    print(roll_no, name, marks, subject)

import random

secret_number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number between 1 to 100 "))
    if guess == secret_number:
        print("Congratulation you guess correct ")
        break
    elif guess < secret_number:
        print("too low try again")
    else:
        print('too high try again')

def password_checker(password):
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    special_chars = False

    has_digit = False
    special_chars = '!@#$%^&*().,'

    if len(password) < min_length:
        print('password is too short ')
        return False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            special_chars = True

    if not has_uppercase:
        print('password contains one uppercase letter ')
        return False
    elif not has_lowercase:
        print('password contains one lowercase letter ')
        return False
    elif not has_digit:
        print('password contains one digit  ')
        return False
    elif not special_chars:
        print('password contains one special char ')
        return False

    print("password is strong ")
    return True


password = input("Enter a password ")
password_checker(password)
