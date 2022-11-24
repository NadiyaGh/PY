import random

Words = ["nadiya","woman","god","fruit","flower","sky","computer","man","book","key","math","phone","folder","program"
        , "paper","note","iran","islam","shia","iraq","america","bathroom","car","cat","dog","garage","library","calculator"]

wrong_letters = 0
Correct_letters = 0
ch = False
ch1 = False
check_T = 0
rand_word = random.choice(Words)
LenRW = len(rand_word)

CorrectLetters = [] 

while wrong_letters < 6: # user can not say wrong letter more than 6 times

    for i in range(0,LenRW): #print - - - and correct letter
        if rand_word[i] in CorrectLetters:
            print(rand_word[i],end=' ')
        else:
            print("_ ",end =' ')

    if check_T == LenRW: # all letter of word are input
        break

    user_input = input("\nEnter letter you think it is in word! ")
    user_input.lower() # all input letter should been small
    ch = False
    ch1 = False

    for i in range(0,LenRW): # check all letter of rand word
        if rand_word[i] == user_input:
            if user_input not in CorrectLetters: #check how many of this letter are in word and check it wasn't exist
                check_T += 1        
                ch = True        
            else:
                print("You have entered this before!")
                ch1 = True
                break

    if ch != True and ch1 == False: # letter is not in rand word
        print("💔")
        wrong_letters += 1
    elif ch1 != True: # letter is in rand word in it wasn't enter befor       
        print("✅")
        CorrectLetters.append(user_input)       
