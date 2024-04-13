# We will listen for the requests on a port and then forward these requests to another server
# In real life, this server/port handles a service 

import socket
import sys
import signal

be_server_message = None

def signal_handler(sig,frame):
    print("\nClosing the server")
    sys.exit(0)

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

            global be_server_message
            be_server_message = None

            client_socket, client_address = server.accept()

            print(f"Recieved Request from {client_address[0]}:{client_address[1]}")

            request_data = client_socket.recv(4096).decode('utf-8')

            request_data = request_data[:16] + f"Recieved Request from {client_address[0]}:{client_address[1]}\n" + request_data[16:]

            print(request_data)
            
            #orward_request(client_socket=client_socket)
            #request_data = request_data + be_server_message.decode('utf-8')


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



