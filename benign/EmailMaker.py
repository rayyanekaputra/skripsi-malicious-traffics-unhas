import random

def NamesReader():

    names = []

    with open("./names/propernames.txt") as file:
        for item in file:
            names.append(item.strip())
    return names

def NamesPickRandom():
    return (random.choice(NamesReader()))

def EmailMaker():
    emails = []

    with open("./email/valid_email_providers.txt") as file:
        files = file.readlines()
        files_shuffled = random.shuffle(files)
        for item in files:
            print(item.rstrip("\n"))
            email = "{}".format(NamesPickRandom().lower()+"@"+item.strip())
            emails.append(email)

    return emails
