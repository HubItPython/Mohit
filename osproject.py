import os 

import OSP as O
if os.path.exists("D:/Python Files VS code/user.txt"):
    username_input=input("Username:")
    pass_input=input("Password:")
    with open("user.txt","r") as f:
        lines=f.readlines()
        us=lines[1].strip()
        ps=lines[3].strip()
    if username_input==us and pass_input==ps:
        print("Access Granted!.Opening your file......") 
        with open("D:/Python Files VS code/OS Module/gangeshwor.txt","r") as f:
            print(f.read())
    else:
        print("Invalid Username or Password")

    
else:
    O.userpass()

    
    

