# We will listen for the requests on a port and then forward these requests to another server
# In real life, this server/port handles a service 

import socket
import sys
import signal

def signal_handler(sig,frame):
    print("\nClosing the server")
    sys.exit(0)

def forward_request(client_socket):
    #print("forward request executed")
    try:
        backend_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        backend_server_socket.connect(("127.0.0.1",4000)) # this is where our backend server will be running
        print("connected to backend server")
        # forward request data to the server @ 127.0.0.1:5000
        while True:
            print("Here1")
            client_socket.settimeout(5)
            try:
                data = client_socket.recv(4096)
                print("Here2")
            except socket.timeout:
                break
            if not data:
                break
            print(f"Forwarding request to {"127.0.0.1"}:{4000}")
            backend_server_socket.sendall(data)
        
        # recieve response from the server and forward it to the client
        while True:
            data = backend_server_socket.recv(4096)
            if not data:
                break
            client_socket.sendall(data)
    except Exception as e:
        print(f"Error forwarding the requesting {e}")
    finally:
        backend_server_socket.close()




def run_lb_server():
    signal.signal(signal.SIGINT, signal_handler)
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip, port = "127.0.0.1", 8000

    # bind the socket object to a port and ip
    server.bind((server_ip, port))               
    
    print(f"Listening on {server_ip}:{port}")   

    # allow only one connection in queue on this port
    server.listen(2)                
    
    # we are using try except finally clause to ensure that server is exited gracefully whenever error is encountered
    try:        
        while True:

            client_socket, client_address = server.accept()

            print(f"Recieved Request from {client_address[0]}:{client_address[1]}")

            request_data = client_socket.recv(4096).decode('utf-8')

            request_data = request_data[:16] + f"Recieved Request from {client_address[0]}:{client_address[1]}\n" + request_data[16:]

            print(request_data)
            
            forward_request(client_socket=client_socket)
            print("")


            http_response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(request_data)}\r\nContent-Type: text/plain\r\n\r\n{request_data}"
            http_response = http_response.encode('utf-8')
            client_socket.sendall(http_response)

            client_socket.close()
    
    except KeyboardInterrupt:
        print("Server closed by admin")
    
    finally:
        server.close()

if __name__ == '__main__':
    run_lb_server()



