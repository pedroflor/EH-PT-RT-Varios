#!/usr/bin/python3

from pwn import *
import time
from termcolor import colored

rhost = "192.168.130.131"
rport = 8080
welcome_message = "Welcome to Vulnerable Server! Enter HELP for help."
debug_msg = True

def check_connection():
    try:
        r = remote(rhost, rport, ssl=False)
        welcome_msg = str(r.recvline())
        r.close()
    except:
        print("Server not running. Closing fuzzer.")
        exit(1)
    
    if not welcome_message.find(welcome_msg):
        print("Welcome message not understod. Closing fuzzer.")
        exit(1)
        

def fuzzer():
    #command_list = ["STATS","RTIME","LTIME","SRUN","TRUN","GMON","GDOG","KSTET","GTER","HTER","LTER","KSTAN"]
    command_list = ["TRUN"]
    delimiter = " "
    
    for command in command_list:
        r = remote(rhost, rport, ssl=False)
        increment = 100
        limit = 20000
        fuzz_char = "A"
        buffer = ""
        print('\n>>> Fuzzing command: ' + colored(command, 'cyan'))
        print ("Sending bytes: ", end='')        
        while len(buffer) < limit:
            buffer = buffer + fuzz_char * increment
            time.sleep(0.1)
            """ Fuzz string """
            fuzzer_buffer = (command + delimiter + "/.:/" + buffer + '\r\n')
            try:
                if debug_msg:
                    print(str(len(fuzzer_buffer)) + ", ", end='')
                else:
                    print (".", end='')

                r.send(fuzzer_buffer)
                
                if debug_msg:
                    print(r.recvline().decode("UTF-8"), end='')
                else:
                    r.recvline()
            except:
                print("\n")
                print(colored('>>>> Program crash detected!!! <<<<', 'yellow'))
                print(colored('>>>> Program crash detected!!! <<<<', 'red'))
                print(colored('>>>> Program crash detected!!! <<<<', 'blue'))
                print('\nFuzzed command: ' + colored(command, 'cyan'))
                print("Total bytes sent: " + colored(str(len(str((fuzzer_buffer)))), 'cyan'))
                exit(1)
        r.close()
            

def exploit():
    pass
 
if __name__ == "__main__":
    check_connection()
    fuzzer()
  
