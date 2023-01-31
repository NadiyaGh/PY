
class FilmServices:
    def __init__(self,ID,NAME):
        self.id = ID
        self.name = NAME

    def add_Film():
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

    def edit_Film():
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
    def search_Film():
        print("----------- Search -------------")
        user_input_search = input("Enter code or name of product: ")
        for product in PRODUCTS:
            if user_input_search==product["code"] or user_input_search==product["name"]:
                print("code: " , product["code"])
                print("name: " , product["name"])
                print("price: " , product["price"])
                print("count: " , product["count"])
    def remove_Film():
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
    def show_list_of_Films():
        i = 1
        for product in PRODUCTS:
            print(i ,"- ",end="")
            print("code: " , product["code"])
            print("name: " , product["name"])
            print("price: " , product["price"])
            print("count: " , product["count"])
            i+=1
    def show_Film():
        ...
    def download_Film():
        ...
    