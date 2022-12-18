import random
import telebot
import gtts
import qrcode
from datetime import date
global bot_state

bot = telebot.TeleBot("5942789065:AAEP6qN15jDXSNPNoEE6mPioBg9EeGinmns",parse_mode=None)
#def echo_all(message,Rand_Number):
   
    

             
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hi "+ message.from_user.first_name + " Welcome 💙")

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message,"""
/start -> start bot!😉
/help -> say what can you do in this bot! 😍
/game -> You can play a game with bot, The robot chooses a number between 1 and 1000 and you have to guess that number. Meanwhile, the robot also guides you 🎮
/max -> It declares the largest entered number 🏆
/argmax -> It tells you that the largest number is the most number entered 🧮
/voice -> It reads the entered sentence for you and sends its audio 🎧
/qrcode -> Converts the input to QRcode 💾
/age -> Tells How old are you 👩👨
    """)



def Game(message):
    Rand_Number = int(random.randint(10,999))
    bot.send_message(message.chat.id,"Guess a number between 10 - 1000")
    
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
            user_guess = int(message.text)
            if user_guess < Rand_Number:
                bot.send_message(message.chat.id, "Go Up ⬆")
            elif user_guess > Rand_Number:
                bot.send_message(message.chat.id, "Go Down ⬇")
            elif user_guess==Rand_Number:
                bot.send_message(message.chat.id , "You Win 🎉")
   
@bot.message_handler(commands=["game"])
def send_game(message):
    bot.reply_to(message,"Number guessing game 🎮")
    global bot_state
    bot_state = "game"
    Game(message)



def Max(message):
    bot.send_message(message.chat.id,"Enter the numbers in this format: 3,5,9,16,90,8 ")
    
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        MAX = message.text.split(",")
        maxx = 0
        list_of_MAX = []
        for item in MAX:
            list_of_MAX.append(int(item))
        for i in list_of_MAX:
            if i > maxx:
                maxx = i
        bot.send_message(message.chat.id ,maxx)
        
@bot.message_handler(commands=["max"])
def send_max(message):
    bot.reply_to(message,"Find Max number 💡")
    bot_state = "max"
    Max(message)



def ArgMax(message):
    bot.send_message(message.chat.id,"Enter the numbers in this format: 3,5,9,16,90,8 ")
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):        
        MAX = message.text.split(",")
        maxx = 0
        list_of_MAX = []
        for item in MAX:
            list_of_MAX.append(int(item))
        j = 0
        for i in list_of_MAX:
            j+=1
            if i > maxx:
                maxx = i
                k = j
        bot.send_message(message.chat.id ,k)
        
@bot.message_handler(commands=["argmax"])
def send_argmax(message):
    bot.reply_to(message,"It Tells you place of max number🏅")
    bot_state = "argmax"
    ArgMax(message)


def Age(message):
    today = date.today()
    EBirth = []
    bot.send_message(message.chat.id,"Enter your birthday: ")
    bot.send_message(message.chat.id,"year/month/day")
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        Birth = message.text.split("/")
        for item in Birth:
            EBirth.append(int(item))
        check_birthday = ((today.month, today.day) < (EBirth[1],EBirth[2]))
        bot.send_message(message.chat.id,EBirth)
        year = today.year - EBirth[0]
        age = year - check_birthday
        bot.send_message(message.chat.id,age)
    
@bot.message_handler(commands=["age"])
def send_age(message):
    bot.reply_to(message,"I tell How old are you? 🎂")
    bot_state = "age"  
    Age(message)


def Voice(message):    
    bot.send_message(message.chat.id,"type somethings in English: ")
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        out = gtts.gTTS(message.text,lang="en",slow=False)
        out.save("D:\PY1\PY\9\Voice2.mp3")
        voice = open("D:\PY1\PY\9\Voice2.mp3", "rb")    
        bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=["voice"])
def send_voice(message):
    bot.reply_to(message,"I read what you type 🎤")
    bot_state = "voice"
    Voice(message)


def QR(message):
    qr = qrcode.make(message.text)
    qr.save("D:\PY1\PY\9\yourQRcode.png")
    qr = open("D:\PY1\PY\9\yourQRcode.png","rb")
    bot.send_photo(message.chat.id, qr)

@bot.message_handler(commands=["qrcode"])
def send_qrcode(message):
    bot.reply_to(message,"Enter whatever you want convert to QRcode 🔗")
    bot_state = "qrcode"
    QR(message)

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    if message.text == "سلام":
        bot.send_message(message.chat.id,"علیک سلام رفیق😍")
    elif message.text == "خوبی؟":
        bot.send_message(message.chat.id,"خداروشکر")
    elif message.text == "چه خبر؟":
        bot.send_message(message.chat.id,"سلامتییی")
    else:
        bot.send_message(message.chat.id,"I can't understand what you say..😥")

# @bot.message_handler(func=lambda m:True)
# def echo_all(message,bot_state):
#     if bot_state == "qrcode":
#         QR(message)
#     elif bot_state == "game":
#         Game(message)
#     elif bot_state == "max":
#         Max(message)
#     elif bot_state == "ArgMax":
#         ArgMax(message)
#     elif bot_state == "voice":
#         Voice(message)
#     elif bot_state ==
bot.infinity_polling()