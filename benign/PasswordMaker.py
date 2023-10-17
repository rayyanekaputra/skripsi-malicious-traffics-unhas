import random

def PasswordListReader():

    password = []
    with open("./password/10k-most-common.txt") as file:
        files = file.readlines()
        for item in files:
            password.append(item.strip())

    return password
    
def PasswordPickRandom():
    return (random.choice(PasswordListReader()))

