import random
import telebot
import gtts
import qrcode
from datetime import date
from telebot import types
import jdatetime

my_keyboard = types.ReplyKeyboardMarkup()
keyhelp = types.KeyboardButton('/help')
keygame = types.KeyboardButton('/game')
keymax = types.KeyboardButton('/max')
keyargmax = types.KeyboardButton('/argmax')
keyvoice = types.KeyboardButton('/voice')
keyqrcode = types.KeyboardButton('/qrcode')
keyage = types.KeyboardButton('/age')

my_keyboard.row(keyhelp)
my_keyboard.row(keymax, keyargmax)
my_keyboard.row(keygame)
my_keyboard.row(keyvoice, keyqrcode,keyage)

#bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
bot = telebot.TeleBot("5942789065:AAEP6qN15jDXSNPNoEE6mPioBg9EeGinmns",parse_mode=None)


################# START ################
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hi "+ message.from_user.first_name + " Welcome 💙",reply_markup=my_keyboard)


################# HELP #################
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
    """,reply_markup=my_keyboard)

# ################# GAME #################   
def Game(message):
    global Rand_Number
    user_guess = int(message.text)
    if user_guess < Rand_Number:
        bot.send_message(message.chat.id, "Go Up ⬆️")
        bot.register_next_step_handler(message ,Game)
    elif user_guess > Rand_Number:
        bot.send_message(message.chat.id, "Go Down ⬇️")
        bot.register_next_step_handler(message ,Game)
    elif user_guess==Rand_Number:
        bot.send_message(message.chat.id , "You Win 🎉")   
#------------#
@bot.message_handler(commands=["game"])
def send_game(message):
    global Rand_Number 
    Rand_Number = int(random.randint(10,999)) 
    bot.reply_to(message,"Number guessing game 🎮")
    bot.send_message(message.chat.id,"Guess a number between 10 - 1000")
    bot.register_next_step_handler(message ,Game)




################# MAX ##################
def Max(message):
    MAX = message.text.split(",")
    maxx = 0
    list_of_MAX = []
    for item in MAX:
        list_of_MAX.append(int(item))
    for i in list_of_MAX:
        if i > maxx:
            maxx = i
    bot.send_message(message.chat.id ,maxx)
#------------#    
@bot.message_handler(commands=["max"])
def send_max(message):
    bot.reply_to(message,"Find Max number 💡")
    bot.send_message(message.chat.id,"Enter the numbers in this format: 3,5,9,16,90,8 ")
    bot.register_next_step_handler(message , Max)



################ ARGMAX ################
def ArgMax(message):      
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
#------------#
@bot.message_handler(commands=["argmax"])
def send_argmax(message):
    bot.reply_to(message,"It Tells you place of max number🏅")
    bot.send_message(message.chat.id,"Enter the numbers in this format: 3,5,9,16,90,8 ")
    bot.register_next_step_handler(message , ArgMax)


################# AGE ##################
def Age(message):
    EBirth = []
    Birth = message.text.split("/")
    for item in Birth:
        EBirth.append(int(item))
    today = jdatetime.date.today()
    check_birthday = ((today.month, today.day) < (EBirth[1],EBirth[2]))
    year = today.year - EBirth[0]
    age = year - check_birthday
    bot.send_message(message.chat.id,age)
#------------#
@bot.message_handler(commands=["age"])
def send_age(message):
    bot.reply_to(message,"I tell How old are you? 🎂")
    bot.send_message(message.chat.id,"Enter your birthday: ")
    bot.send_message(message.chat.id,"year/month/day")
    bot.register_next_step_handler(message , Age)


################# VOICE ################
def Voice(message):    
    out = gtts.gTTS(message.text,lang="en",slow=False)
    out.save("D:\PY1\PY\9\Voice2.mp3")
    voice = open("D:\PY1\PY\9\Voice2.mp3", "rb")    
    bot.send_voice(message.chat.id, voice)
#------------#
@bot.message_handler(commands=["voice"])
def send_voice(message):
    bot.reply_to(message,"I read what you type 🎤")
    bot.send_message(message.chat.id,"type somethings in English: ")
    bot.register_next_step_handler(message , Voice)


################ QRCOED ################
def QR(message):
    qr = qrcode.make(message.text)
    qr.save("D:\PY1\PY\9\yourQRcode.png")
    qr = open("D:\PY1\PY\9\yourQRcode.png","rb")
    bot.send_photo(message.chat.id, qr)
#------------#
@bot.message_handler(commands=["qrcode"])
def send_qrcode(message):
    bot.reply_to(message,"Enter whatever you want convert to QRcode 🔗")
    bot.register_next_step_handler(message , QR)


############ MESSAGE HANDLER ###########
@bot.message_handler(func=lambda m:True)
def echo_all(message):
    if message.text == "سلام":
        bot.send_message(message.chat.id,"علیک سلام رفیق😍")
    elif message.text == "خوبی؟":
        bot.send_message(message.chat.id,"خداروشکر")
    elif message.text == "چه خبر؟":
        bot.send_message(message.chat.id,"سلامتییی")
    else:
        bot.send_message(message.chat.id,"I can't understand what you say..🥺",reply_markup=my_keyboard)

bot.infinity_polling()