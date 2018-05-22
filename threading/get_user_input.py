import os
import threading

client_id = input("client_id = ?")
client_secret = input("client_secret = ?") # if contains letters, will be considered as variable, leads to error

# os.system("mkfifo pipe 2> /dev/null")

def pass_parameter_from_user_input():

    # the 'w' flag is not that stable, 
    # sometimes will need to clear the file, otherwise the file is alwasy emtpy
    file_pipe = open("pipe", "w")
    print(client_secret)
    # need to be careful when you use the {} in .format will lead to key error
    json2pass = '{' + "\"client_id\": {0}, \"client_secret\": {1}".format(client_id, client_secret) + '}'
    
    file_pipe.write(json2pass)
    
    file_pipe.close()

pass_parameter_from_user_input()
input_thread = threading.Thread(target = pass_parameter_from_user_input)
input_thread.start()
os.system("python3 input_consumer.py")

