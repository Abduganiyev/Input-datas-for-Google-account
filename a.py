import random
import string
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

# import speech_recognition as sr
# def command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("I'm listen, speak everything...")
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)
#         print("STOP")
#     try:
#         text = r.recognize_google(audio, language="ru-RU").lower()
#         print("You said: " + text)
#     except sr.UnknownValueError:
#         print("не распознано")
#         text = command()
#     except sr.AttributeError::
#         print("not recognized")
#         text = command()
#     except sr.TimeoutError:
#         print("The attempt to establish a connection was unsuccessful.")
#     return text
# def makeSomething(command):
#     if "прив" in command:
#         print("Привет")
#     elif "пока" in command:
#         print("Пока")
#     elif "hi" in command:
#         print("hi")
#     elif "hello" in command:
#         print("hello")
#     else:
#         pass
 
# while True:
#     makeSomething(command())



# import speech_recognition as sr
# def record_volume():
#     r=sr.Recognizer()

#     try:
#         with sr.Microphone(device_index=1) as source:
#             print("I'm listen, speak everything...")
#             audio = r.listen(source)
#             print("Stop")
#     except:
#         with sr.Microphone(device_index=2) as source:
#             print("I'm listen, speak everything...")
#             audio = r.listen(source)
#             print("Stop")


#     query=r.recognize_google(audio, language='en-Us')
#     print(f"You said: {query.upper()}")


# record_volume()


           
# i<=a//2
# import random
# def binary_search(my_list,item):
#     num=0
    
#     low = 0
#     hight = len(my_list) - 1


#     while low <= hight:
#         num+=1
#         mid = int((low + hight) / 2)
#         guess = my_list[mid]
#         if guess == item:
#             return mid,num
        
#         if guess > item:
#             hight = mid - 1
#         else:
#             low = mid + 1
#     return "Загаданное число не найдено"
# my_list = [1,2,3,4,5,6,7,8,9,10]

# print(binary_search(my_list,10))



# INNBOX2905004840


# import telebot


# bot = telebot.TeleBot("1637786279:AAEjpgsoG-bKqpOTjaSoO0FXAmwrWbZjwXw", parse_mode=None) # вы можете установить parse_mode по умолчанию. HTML или MARKDOWN

# keyboard = telebot.types.InlineKeyboardMarkup()
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message, message.from_user.id)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):   
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, message.from_user.first_name) 
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "What is your name?")
#         bot.register_next_step_handler(message, reg_name)
#         #bot.send_message(message.from_user.id, f"Hi {message.from_user.first_name} {message.from_user.last_name}")
#     else:
#         bot.send_message(message.from_user.id, message.text)

# def reg_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, "What is your surname?")
#     bot.register_next_step_handler(message, reg_surname)

# def reg_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id, "How are you old?")
#     bot.register_next_step_handler(message, reg_age)

# def reg_age(message):
#     global age
#     try:
#         age = int(message.text)
#     except:
#         bot.send_message(message.from_user.id, "How are you old?")
#         bot.register_next_step_handler(message, reg_age)


# def check_age(message):
#     pass
# bot.polling()


