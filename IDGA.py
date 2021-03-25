import random,string
linktofile="new_file.txt"
def main():
    print("Input datas for Goole account")
    random_Name()
    input()
def random_Name():
    name=""
    for i in range(4):
        rLatter = random.choice(string.ascii_lowercase)
        name+=rLatter
    print("Name:",name,end=" ")
    SaveFrom(linktofile,f"Name: {name}"+'\n')
    random_Surename(name)
def random_Surename(name):
    surname=""
    for i in range(4):
        rLatter = random.choice(string.ascii_lowercase)
        surname+=rLatter
    print("Surname:",surname)
    SaveFrom(linktofile,f"Surname: {surname}"+'\n')
    random_Login(name,surname)
def random_Login(name,surname):
    login=surname+name
    print("login:",login)
    SaveFrom(linktofile,f"Login: {login}"+'\n')
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
    SaveFrom(linktofile,f"Password: {password}"+'\n\n')
def SaveFrom(linktofile,text):
    with open(linktofile,'a') as file:
        file.write(text)

main()
