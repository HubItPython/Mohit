# from osproject import userpass as U


def userpass():
    username=input("You are the administrator of this program!Please assign username and password.\nUsername:")
    password=input("Password:")
    with open("D:/Python Files VS code/OS Module/user.txt","w") as file:
        file.write(f"Username:\n{username}\nPassword:\n{password}")
    
if __name__=="__main__":
    userpass()