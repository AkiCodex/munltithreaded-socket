# munltithreaded-socket
## TCP Client-Server Chat Application

This is a simple TCP client-server chat application implemented in Python. It allows multiple clients to connect to a server, send messages, and receive responses.

## Features

- **Client-Server Architecture**: The application follows a client-server architecture, where multiple clients can connect to a server over TCP/IP.
- **Bi-Directional Communication**: Clients can send messages to the server, and the server can respond back to each client individually.
- **Graceful Shutdown**: Clients and the server can gracefully terminate the connection by sending a "close" message.

## Usage

1. **Server Setup**:
   - Run the `server.py` script to start the server. It will listen for incoming connections on the specified host and port.
   
2. **Client Connection**:
   - Run the `client.py` script to connect a client to the server. You can run multiple instances of the client script to simulate multiple clients connecting to the server.

3. **Communication**:
   - Once connected, clients can send messages to the server by typing them in the terminal. The server will respond with an appropriate message.
   - To close the connection, a client can type "close". The server will acknowledge the request and close the connection with that client.

## Requirements

- Python 3.x
- No additional libraries or packages are required.

## Getting Started

1. Clone this repository:

```
git clone https://github.com/Trojanhax/munltithreaded-socket.git
```
2. Run the server:

```
python threaded_server.py
```
3. Run the client(s):

```
python threaded_client.py
```

4. Start chatting!

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

* Hat tip to anyone whose code was used
* Inspiration
* etc
