import socket

HOST = 'challenges.404ctf.fr'
PORT = 30980

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Connected to' + HOST + ':' + str(PORT))

def send(input):
    message = "{}\n".format(input)
    client.send(message.encode())
    print("MESSAGE SEND:", message)

def getinfo(data):
    data = data.split("Entrée :")[1]
    info = data.split("{")[1].split("}")[0]
    return info

def fin(donnees):
    flag = donnees.split("404")[1]
    print("[*] FLAG :",flag)

def regle0(input):
    return input

def regle1(input):
    input = regle0(input)
    return input[::-1]

def regle2(input):
    input = regle1(input)
    new = ""
    n = len(input)
    if n % 2 == 0:
        new = input[n//2:] + input[:n//2]
    elif n % 2 == 1:
        lettre = input[n//2]
        for i in range(n):
            if input[i] != lettre:
                new += input[i]
    return new

def regle3(input):
    consonne = set("bcdfghjklmnpqrstvwxz")
    voyelle = set("aeiouy")
    llist = []
    nlist = []
    new = list(input)
    word = regle2(input)
    if len(word) >= 3:
        if word[2] in consonne:
            for i in range(len(input)):
                if input[i] in voyelle:
                    llist.append(input[i])
                    nlist.append(int(i))
            for p in range(len(llist)):
                try:
                    new[(nlist[p])] = llist[p+1]
                except:
                    new[(nlist[p])] = llist[0]
        else:
            for i in range(len(input)):
                if input[i] in voyelle:
                    llist.append(input[i])
                    nlist.append(int(i))
            for p in range(len(llist)):
                try:
                    new[(nlist[p])] = llist[p-1]
                except:
                    new[(nlist[p])] = llist[-1]
        input = ''.join(new)
        return regle2(input)
    else :
        return word 

def regle4(input):
    consonnes = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
    voyelles = set("aeiouyAEIOUY")
    tmp = 0
    n = 0
    input = regle3(input)
    while n < len(input):
        c = input[n]
        if c in consonnes:
            letter = ord(input[n])
            while chr(letter-tmp) not in voyelles:
                tmp += 1
            vp = (letter-tmp)
            s = 0
            for i in range(n-1,-1,-1):
                ai = ord(input[i])
                li = input[i]
                if li in voyelles:
                    Id = 1
                else:
                    Id = 0
                s += (ai*2**(n-i)*Id)
            a = (((vp + s) % 95) + 32)
            input = input[:n+1] + chr(a) + input[n+1:]
        n += 1
        tmp = 0
    occurrences = {}
    for caractere in input:
        if caractere in occurrences:
            occurrences[caractere] += 1 
        else:
            occurrences[caractere] = 1
    caracteres_tries = sorted(occurrences.keys(), key=lambda x: (-occurrences[x], ord(x)))
    chaine_triee = ""
    for caractere in caracteres_tries:
        chaine_triee += caractere * occurrences[caractere]
    return chaine_triee

data = client.recv(1024).decode()
print(data)

send(regle0(getinfo(data)))

data = client.recv(1024).decode()
print(data)

send(regle1(getinfo(data)))

data = client.recv(1024).decode()
print(data)

send(regle2(getinfo(data)))

data = client.recv(1024).decode()
print(data)

send(regle3(getinfo(data)))

data = client.recv(1024).decode()
print(data)

send(regle4(getinfo(data)))

data = client.recv(1024).decode()
if ">>" not in data:
    data += client.recv(1024).decode()
print(data)

resultat = ""
mot = getinfo(data)
mot = mot.split(" ")

for nombre in range(len(mot)):
    temp = regle4(mot[nombre])
    resultat += temp
    if nombre != len(mot)-1:
        resultat += " "

send(resultat)

data = client.recv(1024).decode()
print(data)

print('Deconnect.')
client.close()

fin(data)