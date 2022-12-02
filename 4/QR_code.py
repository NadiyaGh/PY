import qrcode

name_user = input("Enter your name: ")
mobile = input("Enter your phone number: ")
em = qrcode.make(name_user + mobile)
em.save("phone.png")