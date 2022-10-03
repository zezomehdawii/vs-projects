 
import math
import random
import hashlib
print("----------------------------------------------------------------")
print("|             Assignment 2: RSA ENCRYPTOR/DECRYPTOR            |")
print("----------------------------------------------------------------")


def primesInRange(x,y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False
                
        if isPrime:
            prime_list.append(n)
    return prime_list

prime_list = primesInRange(1,1000)
firstP = random.choice(prime_list)
secondP = random.choice(prime_list)

p = firstP
q = secondP

print ("[*] Generating random primes for p & q...")
print (f"p = {p} || q = {q}")
print("----------------------------------------------------------------")

 
#RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n = p * q
print("RSA Modulus {n} is:",n)
 
#Eulers Toitent
'''CALCULATION OF EULERS TOITENT 'r'.'''
r= (p-1)*(q-1)
print("Eulers Toitent {r} is:",r)

print("----------------------------------------------------------------")
 
#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s mod, i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
 
#e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("----------------------------------------------------------------")
print ("The value of {e} before hashing:",e)   
print("The value of {e} after hashing: ", hashlib.md5((str(e)).encode('utf-8')).hexdigest())
print("----------------------------------------------------------------")
 
#d, Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
print("EUCLID'S ALGORITHM:")
eugcd(e,r)
print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
print("----------------------------------------------------------------")
print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e,r)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("----------------------------------------------------------------")
print("The value of {d} before hashing:",d)
print("The value of {d} after hashing: ", hashlib.md5((str(d)).encode('utf-8')).hexdigest())
print("----------------------------------------------------------------")
public = (e,n)
private = (d,n)
print("Private Key is:",hashlib.md5((str(private)).encode('utf-8')).hexdigest())
print("Public Key is:",hashlib.md5((str(public)).encode('utf-8')).hexdigest())
print("----------------------------------------------------------------")
 
#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
 
#Choose Encrypt or Decrypt and Print
choose = "" 
while (choose != 3):
    choose = input("[1] Encryption\n[2] Decrytion\n[3] Exit\nEnter choice: ")
    if(choose=='1'):
        message = input("""[NOTE] if the message is encrpyted and you want to decrypt it, separate the numbers by comma ','
Enter the message you want to encrypt or decrypt: """)
        print("Your message is:",message)
        enc_msg=encrypt(public,message)
        print("Your encrypted message is:",enc_msg)
    elif(choose=='2'):
        message = input("""[NOTE] if the message is encrpyted and you want to decrypt it, separate the numbers by comma ','
Enter the message you want to encrypt or decrypt: """)
        print("Your message is:",message)
        print("Your decrypted message is:",decrypt(private,message))
    elif (choose == '3'):
        print("Thank you for using the RSA Encryptor. Goodbye!")
        exit (1)
    else:
        print("You entered the wrong option.")