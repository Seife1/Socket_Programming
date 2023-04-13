import socket

Truth = 1
c_name = "Alelgn"
print("--------------------------")
print("Client of "+ c_name)
print("--------------------------")

#Accept an integer from the keyboard in a range of 1 - 100
num = input("Enter a number between 1 - 100 ?  ")

#create a socket object for the client side
serverclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the ip_adress and port number to bind the socket object
name = "10.5.231.149" #The address of the server
port = 65222

#Now bind the socket object in order to associate with a specific ntw interface and port number
serverclient.connect((name, port))

while Truth:
    #Recieve the msg from the server
    s_name = serverclient.recv(1024)
    numS = serverclient.recv(1024)

    #Send the name of the client and the number entered
    cName = c_name
    data = num
    serverclient.send(bytes(cName, "utf-8"))
    serverclient.send(bytes(str(data), "utf-8"))#Send the name of the client and the number entered
    cName = c_name
    data = num
    serverclient.send(bytes(cName, "utf-8"))
    serverclient.send(bytes(str(data), "utf-8"))

    try:
        if 1 <= int(num) <= 100:
            #Display all the data from the client
            print("---------------------------------------")
            print("You are connected to",s_name.decode("utf-8") + "'s server")
            print("The client entered a number",num)

            #Display all the data from the server
            print("The server choose a number ",numS.decode('utf-8'))

            #ADD two numbers and display
            sum = int(num) + int(numS)
            print("The sum of the two number is " + str(sum))
            Truth = 0

        else:
            print("ERROR: The number must be between 1 and 100")
            Truth = 0
            serverclient.close()

    except ValueError:
        print("ERROR: Enter number only!!!")
        Truth = 0
        serverclient.close()

#close the connection
serverclient.close()
