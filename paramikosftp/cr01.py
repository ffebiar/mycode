#!/usr/bin/env python3
## Moving files with SFTP

import paramiko
import os

def main():
    answer= " "
    while True:
        answer= input("Where would you like to transfer the files?: ").lower()
        if answer == "bender":
            t = paramiko.Transport("10.10.2.3", 22)
            t.connect(username="bender", password="alta3")
            sftp= paramiko.SFTPClient.from_transport(t)
            for x in os.listdir("/home/student/filestocopy/"):
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)
            sftp.close()
        elif answer == "fry":
            t = paramiko.Transport("10.10.2.4", 22)
            t.connect(username="fry", password="alta3")
            sftp= paramiko.SFTPClient.from_transport(t)
            for x in os.listdir("/home/student/filestocopy/"):
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)
            sftp.close()
        elif answer == "zoidberg":
            t = paramiko.Transport("10.10.2.5", 22)
            t.connect(username="zoidberg", password="alta3")
            sftp= paramiko.SFTPClient.from_transport(t)
            for x in os.listdir("/home/student/filestocopy/"):
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)
            sftp.close()
        elif answer == "exit":
            exit()
        else:
            print("ERROR! Directory not found!")
            print("If finished, enter exit!")

if __name__ == "__main__":
    main()
