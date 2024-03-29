import socket
import threading

host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 6789         # Port to listen on (non-privileged ports are > 1023)

THREADS = []

def handle_connection(connection, address):
    try:
        while True:
            msg = connection.recv(1024).decode()
            if not msg or msg == "close":
                break
            print(f"Received: {msg}")
            connection.send(msg.encode())
    except ConnectionResetError:
        print("Connection reset by peer.")
    finally:
        close_connection(connection)

def close_connection(connection):
    connection.close()

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
ss.bind((host, port))  # Bind to the port
ss.listen(5)           # Now wait for client connection.

try:
    while True:
        connection, address = ss.accept()  # Establish a connection with the client
        print(f"Connected to {address}")
        t = threading.Thread(target=handle_connection, args=(connection, address))
        THREADS.append(t)
        t.start()
except KeyboardInterrupt:
    print("Server is shutting down...")
    for thread in THREADS:
        thread.join()  # Wait for all threads to finish
    ss.close()        # Close the server socket
