import gtts

def read_from_file():
    global words_bank
    try:
        f = open("translate.txt","r+")
    except IOError:
            print("Could not open file!")
            exit(0)


    words_bank = []
    for i in range(0,len(temp),2):
        my_dict = {"en":temp[i],"fa":temp[i+1]}
        words_bank.append(my_dict)

    f.close()

def Menu():
    print("******* TRANSLATE *******")
    print("1 - Persian to English")
    print("2 - English to Persian")
    print("3 - add a new word to database")
    print("4 - Exit")
    
def English_to_persian():
    user_text = input("enter your english text : ")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)
    out = gtts.gTTS(output,lang="ar",slow=False)
    out.save("voicefa.mp3")

def persian_to_English():
    output = ''
    user_text = input('Enter your Persian text: ')
    user_words = user_text.split(' ')
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] +  " "
                break
        else:
            output = output + user_word + " "

    print(output)
    out = gtts.gTTS(output,lang="en",slow=False)
    out.save("voiceEn.mp3")

def add_new_word():
    user_new_num = int(input("How many words do you want to add? "))
    for i in range(user_new_num):
        user_new_en_word = input("Enter what you want to add in English: ")
        user_new_fa_word = input("Enter what you want to add in Persian: ")
        words_bank.append(user_new_en_word)
        words_bank.append(user_new_fa_word)
        f = open("translate.txt","a")
        f.write("\n" + user_new_en_word + "\n" + user_new_fa_word)
        
read_from_file()
while True:
    Menu()
    choice = int(input("Enter your choice -> "))
    print("*************************")
    if choice == 1:
        persian_to_English()
    elif choice == 2:
        English_to_persian()
    elif choice == 3:
        add_new_word()
    elif choice == 4:
        exit(0)