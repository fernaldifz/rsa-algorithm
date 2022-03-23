import random,math

def generatePairNumbers():
    primes = [i for i in range(2**8,(2**16)-1) if isPrime(i)]
    p,q = 0,0

    while p == q:
        p,q = random.choice(primes),random.choice(primes)
    
    return p,q

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

def encrypt(): #enkripsi menggunakan RSA
    pass

def decrypt(): #dekripsi menggunakan RSA
    pass

def toHex(): #khusus untuk ciphertext dalam notasi heksadesimal
    pass

def showTimeLapse(): #program dapat menampilkan interval waktu enkripsi / dekripsi berapa lama
    pass

def showFileSize(): #program dapat menampilkan size file hasil enkripsi / dekripsi
    pass

p,q = generatePairNumbers()
print(p,q)