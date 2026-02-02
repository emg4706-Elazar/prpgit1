import random

def input_integrity():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num > 500 or num < 0:
                print("out of range")
            else:
                return num
        except ValueError:
            print("Invalid input")

def is_right_number(SECRET_NUMBER,num):
    if num > SECRET_NUMBER:
        print("The number is higher than the secret number!")
        return False
    if num < SECRET_NUMBER:
        print("The number is lower than the secret number!")
        return False
    if num == SECRET_NUMBER:
        print("Right guess!")
    return True

def valid_user(username,password):
    with open("users.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        listi = line.split(":")
        if listi[0] == username and listi[1] == password:
            return True
    raise "Invalid username or password"



username = input("Enter your name: ")
password = input("Enter your password: ")
valid_user(username,password)

with open("guesses.txt","r",encoding="utf-8") as f:
    record = f.readline().rstrip("\n")
if record:
    print(f"Record win: {record}")

SECRET_NUMBER = random.randint(0,500)
win = False
guesses = 0

while not win:
    num = input_integrity()
    win = is_right_number(SECRET_NUMBER,num)
    guesses += 1

if not record:
    with open("guesses.txt", "w", encoding="utf-8") as f:
        f.write(str(guesses))
elif guesses < int(record):
    with open("guesses.txt", "w", encoding="utf-8") as f:
        f.write(str(guesses))
    print("saved new record")
    
print()
print(f"Secret number: {SECRET_NUMBER}")
print(f"number of guesses: {guesses}")




















