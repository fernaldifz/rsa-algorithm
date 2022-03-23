import random,math

def generatePairNumbers():
    primes = []
    p,q,counter = 0,0,0

    for i in range(2**12,2**16):
        if isPrime(i):
            primes.append(i)
            counter += 1

        if counter == 500:
            break

    while p == q:
        p,q = random.choice(primes),random.choice(primes)
    
    print("p dan q sudah ada")
    return p,q

def encryptFile(Path, n, e): #enkripsi menggunakan RSA
    byteArray = openFile(Path)

    encryptArray = [0 for i in range(len(byteArray))]

    for i, value in enumerate(byteArray):
        encryptArray[i] = str(value**e % n)
    
    encryptString = " "
    encryptString = encryptString.join(encryptArray)
        
    with open("encrypted", "w") as encryptedFile:
        encryptedFile.write(encryptString)

def decryptFile(Path, d): #dekripsi menggunakan RSA
    encryptFile = open(Path, "r").readlines()
    encryptString = encryptFile[0]
    encryptArray = encryptString.split()

    decryptArray = [0 for i in range(len(encryptArray))]
    for i, value in enumerate(encryptArray):
        decryptArray[i] = chr(int(value)**d % n)
    
    decryptString = ""
    for i in range(len(decryptArray)):
        decryptString += decryptArray[i]
    
    with open("decrypted", "w") as decryptedFile:
        decryptedFile.write(decryptString)
    return decryptArray

def encryptText(Path, n, e): #enkripsi menggunakan RSA
    byteArray = openFile(Path)

    encryptArray = [0 for i in range(len(byteArray))]

    for i, value in enumerate(byteArray):
        encryptArray[i] = value**e % n
    
    return encryptArray

def decryptText(encryptArray, d): #dekripsi menggunakan RSA
    decryptArray = [0 for i in range(len(encryptArray))]
    for i, value in enumerate(encryptArray):
        decryptArray[i] = value**d % n
    
    return decryptArray

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
    for e in range(2**12,phi//(2**12)):
        if isPrime(e):
            publicKeyCandidate.append(e)

    print("mulai cari d")

    e = random.choice(publicKeyCandidate)

    d = modInverse(e,phi)

    return (e,N),(d,N)

def toHex(encryptArray): #khusus untuk ciphertext dalam notasi heksadesimal
    tmpArray = []
    encryptHexArray = []
    encryptHexString = ''

    for block in encryptArray:     
        if len(str(block)) % 3 == 0:
            tmpString = '0' + str(block)
            tmpArray.append(tmpString)
        else:
            tmpArray.append(str(block))

    for strBlock in tmpArray:
        if strBlock[0] == '0':
            encryptHexArray.append('%x' % int(strBlock[1]))
            encryptHexArray.append('%x' % int(strBlock[2] + strBlock[3]))
        else:
            encryptHexArray.append('%x' % int(strBlock[0] + strBlock[1]))
            encryptHexArray.append('%x' % int(strBlock[2] + strBlock[3]))
    
    for hexStr in encryptHexArray:
        encryptHexString += hexStr + ' '
    
    return encryptHexString


def showTimeLapse(): #program dapat menampilkan interval waktu enkripsi / dekripsi berapa lama
    pass

def showFileSize(): #program dapat menampilkan size file hasil enkripsi / dekripsi
    pass

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
n = 26878129
e = 4703
d = 14704967 
#############
def encryptDecryptText(n, e, d):
    enc = encryptText("ori-file/test_text.txt", n, e)
    print(enc)
    dec = decryptText(enc, d)
    print(dec)

encryptDecryptText(n, e, d)
#############
