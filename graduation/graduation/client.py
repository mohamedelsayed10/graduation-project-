import socket

user_input = ''
HEADER = 64
FORMAT = 'utf-8'
port = 8080
SERVER = socket.gethostbyname(socket.gethostname())
addr = (SERVER,port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)
D = "0"
def send(msg):
    MSG = msg.encode(FORMAT)
    print(MSG)
    client.send(MSG)

while user_input != "0" :
    user_input = input("Enter feature you need to work : ")
    send(user_input)
