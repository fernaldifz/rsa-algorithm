import random, math, time, os

def generatePairNumbers():
    primes = []
    p,q,counter = 0,0,0

    for i in range(2**6,2**8):
        if isPrime(i):
            primes.append(i)
            counter += 1

        if counter == 100:
            break

    while p == q:
        p,q = random.choice(primes),random.choice(primes)
    
    print("p dan q sudah ada")
    return p,q

def encryptFile(Path, n, e): #enkripsi menggunakan RSA
    startTime = time.time()
    byteArray = openFile(Path)

    encryptArray = [0 for i in range(len(byteArray))]

    for i, value in enumerate(byteArray):
        encryptArray[i] = str(value**e % n)
    
    encryptString = " "
    encryptString = encryptString.join(encryptArray)
        
    with open("encrypted", "w") as encryptedFile:
        encryptedFile.write(encryptString)
    
    encryptTime = time.time() - startTime
    return encryptArray, encryptTime



def decryptFile(Path, d,n): #dekripsi menggunakan RSA
    startTime = time.time()

    encryptFile = open(Path, "r").readlines()
    encryptString = encryptFile[0]
    encryptArray = encryptString.split()

    decryptArray = [0 for i in range(len(encryptArray))]
    for i, value in enumerate(encryptArray):
        decryptArray[i] = chr(int(value)**d % n)
    
    decryptString = ""
    for i in range(len(decryptArray)):
        decryptString += decryptArray[i]
    
    with open("decrypted", "w", encoding="utf-8") as decryptedFile:
        decryptedFile.write(decryptString)

    decryptTime = time.time() - startTime
    return decryptArray, decryptTime


def isPrime(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    else:
        for i in range(2,num,1):
            if num % i == 0:
                return False
    return True

def modInverse(e, phi):
    for d in range(1,phi):
        if ((e % phi) * (d % phi)) % phi == 1:
            return d

def generatePairKey(): #pembangkit pasangan kunci (privat dan publik)
    p,q = generatePairNumbers()
    N = p*q
    phi = (p-1)*(q-1)

    print("mulai cari e")

    publicKeyCandidate = []
    for e in range(2,phi//(2**8)):
        if isPrime(e):
            publicKeyCandidate.append(e)

    print("mulai cari d")

    e = random.choice(publicKeyCandidate)

    d = modInverse(e,phi)

    return (e,N),(d,N)

def toHex(encryptArray): #khusus untuk ciphertext dalam notasi heksadesimal
    encryptHexArray = [0 for i in range(len(encryptArray))]
    for i in range(len(encryptArray)):
        encryptHexArray[i] = str(hex(int(encryptArray[i]))[2:])
    
    encryptHexString = " "
    encryptHexString = encryptHexString.join(encryptHexArray)
    return encryptHexString

def showFileSize(Path): #program dapat menampilkan size file hasil enkripsi / dekripsi
    fileSize = os.path.getsize(Path)
    return fileSize

def unpackKeyTuples(string):
    sX, sY = '',''

    for idx in range(0,string.index(',')):
        if string[idx] != "(":
           sX += string[idx]

    for idx in range(string.index(',')+1, len(string)):
        if string[idx] != ")":
           sY += string[idx]

    return int(sX),int(sY)

def openFile(Path):
    file = open(Path, "rb")
    data = file.read()
    file.close()

    byteArray = bytearray(data)
    return byteArray


#############
# SEMENTARA # 
# n = 3337
# e = 79
# d = 1019 
#############
# p = generatePairKey()
# print(p)
def encryptDecryptFile(n, e, d):
    # enc,etime = encryptFile("ori-file/test_text.txt", n, e)
    # print("array enkripsi: ", enc)
    # print("time : ",round(etime,4))
    dec, dtime = decryptBin("cipher-result/cipherResult.mp4", d,n)
    # print("array dekripsi", dec)
    print("time : ",dtime)

# encryptDecryptFile(n, e, d)
#############
