# 🧠 Python Multi-Client Chat System with Server Discovery

This project is a **beginner-friendly Python socket programming chat system** that allows multiple clients to communicate over a network. It features a **discovery server** that dynamically shares the server’s IP and port, making it ideal for learning the fundamentals of networking, threading, and inter-device communication.

---

## 🚀 Features

- 🔍 **Server Discovery**: Clients don't need hardcoded IPs. A separate discovery server provides the current IP and port.
- 💬 **Multi-client chat**: Supports simultaneous messaging between multiple users.
- 🔐 **Private messaging**: Send direct messages using `@username`.
- 🧵 **Threaded client handling**: Ensures non-blocking communication on both client and server.
- 🖥️ **No external libraries** required — just pure Python!

---

## 📁 Project Structure
socket-chat-discovery/
├── server/
│ └── server.py # The main server with chat and discovery functionality
├── client/
│ └── client.py # The client that connects via discovery server
├── README.md # This file
├── LICENSE # MIT license
└── .gitignore # Ignores unnecessary files



---

## ⚙️ How It Works

### 📡 Discovery Phase

1. A client first connects to a lightweight **discovery server** running on a known port (`5001`).
2. The discovery server responds with the IP and port of the chat server.
3. The client uses this info to connect to the chat server (`5555`).

### 💬 Messaging Phase

- On connection, the client enters a **username**.
- Users can:
  - Send messages to everyone.
  - Send **private messages** using: `@username Your message here`.

---

## 🧪 How to Run

> 🐍 Prerequisite: Python 3.x installed

### 🖥️ Start the Server

```bash
cd server
python server.py

This launches both the chat server and the discovery server.

💻 Start a Client (on same or different machine in same network)
cd client
python client.py
Enter your username when prompted.

Start chatting with others connected to the same server.
🔐 Private Messaging
To send a private message:
@john Hello John!
🌐 Network Configuration
Ensure:

All devices are connected to the same network.

The server device’s IP is correctly used in discovery_socket.connect().
📜 License
This project is licensed under the MIT License.





