import random,math

def generatePairNumbers():
    primes = [i for i in range(2**8,(2**16)-1) if isPrime(i)]
    p,q = 0,0

    while p == q:
        p,q = random.choice(primes),random.choice(primes)
    
    return p,q

def encrypt(Path, n, e): #enkripsi menggunakan RSA
    byteArray = openFile(Path)

    encryptArray = [0 for i in range(len(byteArray))]

    for i, value in enumerate(byteArray):
        encryptArray[i] = str(value**e % n)
    
    encryptString = " "
    encryptString = encryptString.join(encryptArray)
        
    with open("encrypted", "w") as encryptedFile:
        encryptedFile.write(encryptString)

def decrypt(Path, d): #dekripsi menggunakan RSA
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

def generatePairKey(): #pembangkit kunci publik
    p,q = generatePairNumbers()

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
n = 3337
e = 79
d = 1019 
#############
def encryptDecryptText(n, e, d):
    encrypt("ori-file/test_text.txt", n, e)
    decrypt("encrypted", d)

encryptDecryptText(n, e, d)
#############
