from getpass import getpass
import instaloader


username = input("Username: ")
password = getpass("Password: ")

Ins = instaloader.Instaloader()
Ins.login(username, password)
profile = instaloader.Profile.from_username(Ins.context, "nadiya.gh0")
print("You log in! 🎉")
f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line.strip())
f.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

for Nfol in new_followers:
    if Nfol not in old_followers:
        print(Nfol)

f = open("followers.txt", "w")
for Nfol in new_followers:
    f.write(Nfol + "\n")
f.close()