text = input("Enter your text: ")
#print(len(text.split()))

word_num = 1
for i in range(0,len(text)):
    if (text[i]=="\n") or (text[i]=="\t") or (text[i]==" " and text[i-1]!=" "):
        word_num += 1
print(word_num)
