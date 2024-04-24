userID = "nandakishore"
password = "123@nanda"

while(True):
    t_usrID = input("Enter user ID:")
    t_pass = input("Enter password:")
    if(t_usrID != userID or t_pass != password):
        print("Wrong Credentials, Please try again")
    else:
        print(f"Hello {t_usrID}, Welcome")
        break
    
    txt = input("Do you want to try again? y/n:")
    if(txt == 'n'):
        break

