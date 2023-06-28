import socket

HOST = 'challenges.404ctf.fr'
PORT = 31420

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Connected to' + HOST + ':' + str(PORT))

def send(donnees):
    message = "{}\n".format(donnees)
    client.send(message.encode())
    print("MESSAGE SEND :", message)

def countrhino(donnees):
    donnees = donnees.split("»")[1]
    nb = donnees.count("~c`°^)")
    send(nb)

def fin(donnees):
    flag = donnees.split("404")[1]
    print("[*] FLAG :",flag)

p = 0

for i in range(101):
    donnees = b''
    while b":" not in donnees and p < 550:
        p += 1
        tampon = client.recv(1024)
        donnees += tampon
    print(donnees.decode())
    countrhino(donnees.decode())

print('Deconnected.')
client.close()

fin(donnees.decode())