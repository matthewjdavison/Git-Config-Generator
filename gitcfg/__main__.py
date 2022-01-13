import sys
import subprocess
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    # print('in main')
    args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    if len(args) < 2:
        print("Please enter the following: \nhost repositoryname")
        return
    git_host = args[0]
    git_repo = args[1]
    print("Git Host: " + git_host)
    print("Git Repository Name: " + git_repo)

    username = ""
    email = ""
    
    if(git_host == "personal"):
        username = "testPersonal"
        email = "testPersonalEmail"
    elif(git_host == "online"):
        username = "testOnline"
        email = "testOnlineEmail"
    else:
        print("That host is unknown.")
        return

    print("username: "+username)
    print("email: "+email)
    

    print(subprocess.run(["git", "init"], capture_output=True, shell=True))

    print(subprocess.run(["git", "config", "user.name", username], capture_output=True, shell=True))
    print(subprocess.run(["git", "config", "user.email", email], capture_output=True, shell=True))
    
    print(subprocess.run(["touch", "README.md"], capture_output=True, shell=True))
    print(subprocess.run(["git", "add", "."], capture_output=True, shell=True))
    print(subprocess.run(["git", "commit",  "-m", "first commit"], capture_output=True, shell=True))
    print(subprocess.run(["git", "branch",  "-M", "master"], capture_output=True, shell=True))
    print(subprocess.run(["git", "remote",  "add", "origin", "git@"+git_host+":"+username+"/"+git_repo+".git"], capture_output=True, shell=True))
    print(subprocess.run(["git", "push",  "-u", "origin", "master"], capture_output=True, shell=True))

    


if __name__ == '__main__':
    main()