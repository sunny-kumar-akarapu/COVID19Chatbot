import socket
import excel
import os

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("Enter your name:")
    message = input(" -> ")  # take input
    client_socket.send(message.encode())  # send message
    print("Please Enter your Occupation:")
    message = input(" -> ")  # take input
    Occupation=message
    client_socket.send(message.encode())  # send message
    print("Enter  'a' for 'Yes'\n\t'b' for 'No'\n")
    while message.lower().strip() != 'exit':
        que = client_socket.recv(1024).decode()  # receive response
        print('ChatBot: ' + que)  # show in terminal
        message = input(" -> ")  # again take input
        while message.lower().strip()!="a" and message.lower().strip()!="b" and message.lower().strip()!="exit":
            print("Ivalid Input..Please try again!")
            message = input(" -> ")
        client_socket.send(message.encode())  # send message

    if Occupation.lower().strip()=="doctor":
        print("Hey Doc, please checkout the file which consisting of the detials of COVID patients")
        fileData=client_socket.recv(8192).decode()
        excel.initiate()
        details=fileData.split("Patient Name:")
        for detail in details[1:]:
            d=detail.split("\n")
            col=d[1].split()
            col.insert(0, d[0])
            # print(col)
            excel.addNewColumn(col)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
