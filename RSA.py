def encrypt(Path, n, e): #enkripsi menggunakan RSA
    byteArray = openFile(Path)

    encryptArray = [0 for i in range(len(byteArray))]

    for i, value in enumerate(byteArray):
        encryptArray[i] = value**e % n
    
    return encryptArray

def decrypt(encryptArray, d): #dekripsi menggunakan RSA
    decryptArray = [0 for i in range(len(encryptArray))]
    for i, value in enumerate(encryptArray):
        decryptArray[i] = value**d % n
    
    return decryptArray

def generatePublicKey(): #pembangkit kunci publik
    pass

def generatePrivateKey(): #pembangkit kunci privat
    pass

def toHex(): #khusus untuk ciphertext dalam notasi heksadesimal
    pass

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
    encryptArray = encrypt('ori-file/test_text.txt', n, e)
    print("hasil enkripsi: ", encryptArray)
    decryptArray = decrypt(encryptArray, d)
    print("hasil dekripsi: ", decryptArray)

encryptDecryptText(n, e, d)
#############