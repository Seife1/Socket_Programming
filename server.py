import socket

#assigning a random number for the server
numS = 100

s_name = "Sileshi"
t_value = 1 #check point for while loop

#create a socket object for the server side
objServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the ip_adress and port number to bind the socket
name = socket.gethostname()
port = 65222

#Now bind the socket object in order to associate with a specific ntw interface and port number
objServer.bind((name, port))

#listen for incoming connection(s)
objServer.listen(3)

while t_value:

    print('----------------------------------')
    print(f"Hello, This is {s_name}'s server\n-------------------------------\nThe server is waiting for the client")

    #wait a client to connect
    clientsocket, address = objServer.accept()
    print('------------------------------------------------')
    print(f"connection from {address} has been established!")
    print('------------------------------------------------')

    #Send a data to the client
    clientsocket.send(bytes(s_name, "utf-8"))
    clientsocket.send(bytes(str(numS), "utf-8"))

    #Recieve the data from the client side
    cName = clientsocket.recv(1024)
    data = clientsocket.recv(1024)

    #Check the number entered in a given range

    try:
        if 1 <= int(data) <= 100:

            #Display the message of the client
            print("The name of the client is " + cName.decode('utf-8'))
            print("The client entered a number " + data.decode('utf-8'))

            #Number chosen by a server
            print("The server choose a number " + str(numS))

            sum = int(data) + numS
            print("The sum of the two number is " + str(sum))
            t_value = 0

        else:

            print("ERROR: The number must be between 1 and 100")
            t_value = 0

    except ValueError:
        print("ERROR: NOT String")
        t_value = 0

#close the connection
clientsocket.close()
