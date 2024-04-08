import socket

def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip, port = "127.0.0.1", 8000

    # bind the socket object to a port and ip
    server.bind((server_ip, port))               
    
    print(f"Listening on {server_ip}:{port}")   

    # allow only one connection in queue on this port
    server.listen(0)                
    
    while True:

        client_socket, client_address = server.accept()

        print(f"Recieved Request from {client_address[0]}:{client_address[1]}")

        client_socket.close()
        server.close()

if __name__ == "__main__":
    run_server()


