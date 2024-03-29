import socket

host = "127.0.0.1"   # Standard loopback interface address (localhost)
port = 6789          # Port to listen on (non-privileged ports are > 1023)

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a TCP socket

try:
    cs.connect((host, port))                             # Establish connection with server
    print("Connected to:", cs.getpeername())              # Print connected host and port
    
    while True:
        msg = input("Enter message: ") + "\n"             # Get string from user, add newline
        cs.sendall(msg.encode())                          # Send the message to the server
        
        if msg.strip().lower() == "close":
            break
        
        server_response = cs.recv(1024).decode()          # Receive data from the server
        print("Server says:", server_response)            # Print what server sent us

except ConnectionRefusedError:
    print("Connection refused. Is the server running?")
except ConnectionResetError:
    print("Connection reset by peer.")
except KeyboardInterrupt:
    print("Closing the client...")
finally:
    cs.close()                                             # Close the connection
