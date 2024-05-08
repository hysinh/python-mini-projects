from cryptography.fernet import Fernet

"""
Password Manager tutorial - tech with Tim, https://www.youtube.com/watch?v=NpmFbWO6HPU
decryption for viewing not working at the moment
"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 



master_pwd = input("What is the master password? ")
key = load_key() #converts master_pwd into bytes format
fer = Fernet(key) #initializing encryption module

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt
# need one function to encrypt and one to decrypt

"""
# Only use once to create a Key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  #wb means write in bytes
        key_file.write(key)

write_key()
"""



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

"""
def view():
    with open("passwords.txt", "r") as f:  # with keyword automatically closes the file, a = mode (means append, adds something to the end of file, creates if it doesn't exist), w = write (overwrites and makes a new one), r= read only
        for line in f.readlines():
            data = line.rstrip() 
            user, passw = data.split("|")
            print("User:", user, "| Password:", 
                  fer.decrypt(passw.encode()).decode())
            #print(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")
            #print(line.rstrip()) # strips carriage return from the end of line"""

def add():
    """
    Creates a new file if one doesn't already exist.
    Add password into it
    """
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:  # with keyword automatically closes the file, a = mode (means append, adds something to the end of file, creates if it doesn't exist), w = write (overwrites and makes a new one), r= read only
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue # brings you back to the top