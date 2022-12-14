def search(sen,word):
    if word in sen:
        return ("Word found")
    else:
        return("Word not found")

sen = []
sen = input()
word = input()
ans = search(sen,word)
print(ans)