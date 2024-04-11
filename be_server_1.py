import socket
import signal
import sys

def signal_handler(sig,frame):
    print("\nClosing the server")
    sys.exit(0)

def run_be_server():
    signal.signal(signal.SIGINT, signal_handler)
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip, port = "127.0.0.1", 4000

    # bind the socket object to a port and ip
    server.bind((server_ip, port))               
    
    print(f"Listening on {server_ip}:{port}")   

    # allow only one connection in queue on this port
    server.listen(0)                
    
    # we are using try except finally clause to ensure that server is exited gracefully whenever error is encountered
    try:        
        while True:
            client_socket, client_address = server.accept()
            print(f"Received Request from {client_address[0]}:{client_address[1]}")
            #print(type(client_socket),client_socket.__sizeof__(),client_socket)

            # Add debug output
            print("Waiting to receive data from client...")
            
            request_data = "hello world"
            http_response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(request_data)}\r\nContent-Type: text/plain\r\n\r\n{request_data}"
            http_response = http_response.encode('utf-8')

            client_socket.sendall(http_response)
            client_socket.close()
            '''

            request_data = client_socket.recv(4096).decode('utf-8')
            print("Data received from client:", request_data)

            request_data = request_data[:16] + f"Received Request from {client_address[0]}:{client_address[1]}\n" + request_data[16:]
            print(request_data)

            client_socket.sendall(http_response)

            client_socket.close()
            '''
    
    except KeyboardInterrupt:
        print("Server closed by admin")
    
    finally:
        server.close()

if __name__ == "__main__":
    run_be_server()


