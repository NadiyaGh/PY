import qrcode

PRODUCTS = []
######## File ########
def read_from_database():
    f = open("database.txt","r")

    for line in f:
        result = line.split(",")
        my_dict = {"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODUCTS.append(my_dict)
    f.close()

def write_to_database():
    f = open("database.txt","w")

    for product in PRODUCTS:
        f.write(product["code"])
        f.write(",")
        f.write(product["name"])
        f.write(",")
        f.write(str(product["price"]))
        f.write(",")
        f.write(str(product["count"]))
       # f.write("\n")
        
    f.close()

def Factor(pro,i):
    sum = 0
    j = 1
    print("_____________ Factor _____________")
    for product in pro:
        print(j , "- " , product["name"],"     ",product["price"],"    ",product["count"])
        sum += (product["count"] * product["price"])
        j+=1
    print("Sum = ",sum)
    
######## Menu ########
def show_menu():
    print("1 - Add product")
    print("2 - Edit product")
    print("3 - Remove product")
    print("4 - Search in StoreRoom")
    print("5 - Show list of products")
    print("6 - Buy")
    print("7 - save product with QRcode")
    print("8 - Exit")

######## Add ########
def add():
    print("------------- Add --------------")
    while True:
        code = input("Enter code : ")
        name = input("Enter name : ")
        price = input("Enter price : ")
        count = input("Enter count : ")
        new_product = {"code":code,"name":name,"price":price,"count":count}
        PRODUCTS.append(new_product)
        con = input("Do you want to continue? (y/n) ")
        if con == "n":
            break
        print(".............")

######## Edit ########
def edit():
    while True:
        user_input_edit = input("Enter code or name of product: ")
        for product in PRODUCTS:
            if user_input_edit==product["code"] or user_input_edit==product["name"]:
                print("The product you selected -> ")
                print("code: " , product["code"])
                print("name: " , product["name"])
                print("price: " , product["price"])
                print("count: " , product["count"])
                check = input("Is it true?(y/n) ")
                if check == "n":
                    ch = False
                    break
                else:
                    ch = True
                print("Enter what do you want to edit? ")
                print("1- name")
                print("2- price")
                print("3- count")
                choice_e = int(input("Enter your choice: "))
                if choice_e == 1:
                    name_e = input("Enter new name : ")
                    product["name"]=name_e
                elif choice_e == 2:
                    price_e = input("Enter new price : ")
                    product["price"]=price_e
                elif choice_e == 3:
                    count_e = input("Enter new count : ")
                    product["count"]=count_e
                
                break
        if ch==True:
            break


    print()

######## Remove ########                        
def remove():
     while True:
        user_input_edit = input("Enter code or name of product: ")
        for product in PRODUCTS:
            if user_input_edit==product["code"] or user_input_edit==product["name"]:
                print("The product you selected -> ")
                print("code: " , product["code"])
                print("name: " , product["name"])
                print("price: " , product["price"])
                print("count: " , product["count"])
                check = input("Is it true?(y/n) ")
                if check == "n":
                    ch = False
                    break
                else:
                    ch = True
                PRODUCTS.remove(product)
                break
        if ch==True:
            break

######## Search ########
def search():
    print("----------- Search -------------")
    user_input_search = input("Enter code or name of product: ")
    for product in PRODUCTS:
        if user_input_search==product["code"] or user_input_search==product["name"]:
            print("code: " , product["code"])
            print("name: " , product["name"])
            print("price: " , product["price"])
            print("count: " , product["count"])

######## Show list ########
def show_list():
    i = 1
    for product in PRODUCTS:
        print(i ,"- ",end="")
        print("code: " , product["code"])
        print("name: " , product["name"])
        print("price: " , product["price"])
        print("count: " , product["count"])
        i+=1

######## Buy ########
def buy():
    i= 0
    PurchaseAmount = 0
    #list of factor:
    pro = []
    while True:
        checkE = False
        user_input_buy = input("Enter the product code or name: ")
        for product in PRODUCTS:
            if user_input_buy==product["code"] or user_input_buy==product["name"]:
                checkE = True
                print("The product you selected -> ")
                print("code: " , product["code"])
                print("name: " , product["name"])
                print("price: ", product["price"])
                print("count: " , product["count"])

                check = input("Is it true?(y/n) ")
                if check == "n":
                    ch = False
                    break
                else:
                    ch = True
                while True:
                    user_input_buy_num = input("Enter your desired number of: ")
                    if int(user_input_buy_num) > int(product["count"]):
                        print("The supply is NOT enough!!\nThe available suppply list is: ",end=" ")
                        print(product["count"])
                        Ans = input("Do you want to continue??? (y/n) -> ")
                        if Ans == 'Y' or Ans == 'y':
                            continue
                        else:
                            return
                    else:
                        user_input_buy_num = int(user_input_buy_num)
                        product["count"] = int(product["count"]) - user_input_buy_num
                        
                        PurchaseAmount += (user_input_buy_num * int(product['price']))
                        i+=1
                        factor_dict = {"name":product["name"],"price":PurchaseAmount,"count":user_input_buy_num}
                        str(product["count"])
                        str(product["price"])
                
                        pro.append(factor_dict)
                        break
                
        if checkE==False:
            print("your intended object code not found!!")
        check = input("Do you want to continue to buy?(y/n)")
        if check == 'n':
            Factor(pro,i)
           
            break

###### QRcode #######
def QR():
    user_input_co = input("Enter name or code of product:  ")
    for product in PRODUCTS:
        if user_input_co==product["code"] or user_input_co==product["name"]:
            em = qrcode.make(product)
            em.save("product.png")        

######## Main ########
print("--------------------------------")
print("Welcome! ")
read_from_database()
while True:
    print("--------------------------------")
    show_menu()
    choice = int(input("Enter your choice: "))
    print("--------------------------------")
    if choice == 1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice==7:
        QR()
    elif choice==8:
        write_to_database()
        exit(0)