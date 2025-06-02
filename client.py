import socket
import threading

# Connect to the discovery server to get chat server IP
discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
discovery_socket.connect(("192.168.1.29", 5001))  # Discovery server known IP

server_details = discovery_socket.recv(1024).decode()
server_ip, server_port = server_details.split(":")
server_port = int(server_port)
discovery_socket.close()

print(f"Discovered chat server at {server_ip}:{server_port}")

# Connect to the chat server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Register username
username = input("Enter your username: ")
client_socket.sendall(username.encode())

# Background thread to receive messages
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(f"\n{message}")
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

# Send messages
while True:
    message = input("You: ")
    client_socket.sendall(message.encode())
