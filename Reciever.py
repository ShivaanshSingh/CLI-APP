import socket #module

#class
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = "127.0.0.1"
port_no = 2424  #0-65353, 0 to 1023 reserved hai
complete_address = (ip_address, port_no)
s.bind(complete_address)
print("Listening Mode on")
while True: #infinite loop
    Data = s.recvfrom(100)
    message = Data[0]
    message = message.decode('ascii')
    sender_address = Data[1]
    sender_ip_address = sender_address[0]
    
    file = open('database', 'a') #writes content
    file.write(  message)
    file.close()
    
    s.sendto("Thanks lil nigga", sender_ip_address)
    print(message)
    
    #Assignment - ip - date - time