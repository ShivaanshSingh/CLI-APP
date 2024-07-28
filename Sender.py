import socket #module

#socket.AF_INET --> THROUGH THE INTERNET 
#socket.SOCK_DGRAM --> protocol (UDP?TCP)

#class
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "127.0.0.1"
target_port = 2424 
target_address = (target_ip,target_port)
condition = True

while True:
    
    message = input("Please enter your message: ")
    message_encrypted = message.encode('ascii')
    s.sendto(message_encrypted, target_address)
    print("Your message has been sent!")
    permission = input("Do you want to exit this program? Y/N: ")
    
    if permission=="Y" or permission == 'y':
        condition = False
    