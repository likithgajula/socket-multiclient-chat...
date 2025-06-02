import socket
import select
import threading

clients = {}  # Stores usernames and connections

# Setup TCP chat server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555))  # Fixed port for easier connection
server_socket.listen(100)
print("Chat server running on port 5555...")

# Setup TCP discovery server (responds with IP & port)
discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
discovery_socket.bind(("0.0.0.0", 5001))  # Fixed discovery port
discovery_socket.listen(5)
print("Discovery server running on port 5001...")

def handle_discovery():
    """Responds to clients asking for server details."""
    while True:
        conn, addr = discovery_socket.accept()
        conn.sendall(b"192.168.1.29:5555")  # Send IP & port
        conn.close()

threading.Thread(target=handle_discovery, daemon=True).start()

# Handle incoming clients & messages
while True:
    readable, _, _ = select.select([server_socket] + list(clients.values()), [], [])
    for sock in readable:
        if sock == server_socket:
            conn, addr = server_socket.accept()
            conn.sendall(b"Enter username: ")
            username = conn.recv(1024).decode().strip()
            clients[username] = conn
            print(f"New user joined: {username} ({addr})")
        else:
            try:
                message = sock.recv(1024).decode()
                sender_username = next(user for user, conn in clients.items() if conn == sock)

                if not message:
                    clients.pop(sender_username)
                    sock.close()
                elif message.startswith("@"):
                    target, private_msg = message.split(" ", 1)
                    target_username = target[1:]
                    if target_username in clients:
                        clients[target_username].sendall(f"(Private) {sender_username}: {private_msg}".encode())
                    else:
                        sock.sendall(b"User not found.")
                else:
                    print(f"{sender_username}: {message}")
                    for client in clients.values():
                        if client != sock:
                            client.sendall(f"{sender_username}: {message}".encode())
            except:
                sock.close()
