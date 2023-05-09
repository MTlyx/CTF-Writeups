from itertools import cycle

text = open("./intercepted-original-mesage.txt", "r").read()
output = open("./message-encrypted.txt", "r").read()
output = output.split(",")

Force = []
SECRET=[[0]]*16

for i in range(0,0x2600):
    Force.append(chr(i))

for x in range(len(text)):
    if text[x] != "*":
        print("Letter: {} Position: {}  Encrypted as: {}".format(text[x],x%16,output[x]))
        for number in Force:
            if (str(ord(text[x]) ^ ord(number))) == output[x]:
                print("XOR key: {}\n".format(ord(number)))
                SECRET[x%16] = ord(number)

print(f"Total XOR key: {SECRET}\n")

def decrypt(message):
    return [chr(int(a) ^ b) for a , b in zip(message,cycle(SECRET))]

with open("./output.txt","w") as f:
    f.write("".join(decrypt(output)))

print("Message:",open("./output.txt","r").read())