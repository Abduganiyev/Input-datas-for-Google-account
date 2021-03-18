import random,string
def main():
    print("Input datas for Goole account")
    random_Name()
def random_Name():
    name=""
    for i in range(4):
        rLatter = random.choice(string.ascii_lowercase)
        name+=rLatter
    print("Name:",name,end=" ")
    random_Surename(name)
def random_Surename(name):
    surname=""
    for i in range(4):
        rLatter = random.choice(string.ascii_lowercase)
        surname+=rLatter
    print("Surname:",surname)
    random_Login(name,surname)
def random_Login(name,surname):
    login=""
    print("login:",surname+name)
    random_Password(name,surname)
def random_Password(name,surname):
    password=""
    for i in range(7):
        rNumber = random.choice(string.digits)
        password+=rNumber
    
    upperLatter=name[3].upper()
    lowLatter=surname[2].lower()
    password=upperLatter+lowLatter+password
    print("Password:",password)

main()
