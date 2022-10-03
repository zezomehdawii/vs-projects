# Importing required libraries
import math, random # To generate random number
import hashlib # For hashing function
from pyfiglet import Figlet #To print the name of our tool in specific font


# Colors
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
U= '\033[33m'  # blue 


# Information about our tool
version= "1.0.0"
groupMembers = ["Asma Bader" , "Noor AlHomeed", "Alghadeer Alshams"  ,"Layan Almubarak" ,"Salma Almogbil" , "Buhhra Alhetelah"]

# Print the name of our tool
custom_fig = Figlet(font='graffiti')
print(G + custom_fig.renderText('ECC'))

# Function to print banner of our tool (version, members name , Instructor name, etc)
def banner():
    for i in range(6):
        print(G + " |---> ", C + "[*]", W + groupMembers[i])
    print('')
    print(G + '[>]' + C + ' Version    :  ' + W + version)
    print(G + '[>]' + C + ' COPYRIGHT  : ' + W , 'Cryptography Assignment at Imam Abdulrahman Bin Faisal University')
    print(G + '[>]' + C + ' COURSE     : ' + W , 'CYS 406 - APPLIED CRYPTOGRAPHY')
    print(G + '[>]' + C + ' INSTRUCTOR : ' + W + ' Dr. Naya Nagy ' + '\n'+ W)

#Calling banner function to print details
banner()



# Initialzing constants, keys and prime number required
nTimes = 100 # Represent number of dots till we reach the max area

# y = (x**3)+(A*x)+ B (mod P)
primeNumber = 4093 # P --> y = (x**3)+(A*x)+ B (mod P)
randomSender = random.choice(range(1,primeNumber)) # --> random value for x in equation --> y = (x**3)+(A*x)+ B (mod P) for generating points
ConstantA_curve = 1 # A --> y = (x**3)+(A*x)+ B (mod P)
ConstantB_curve = 6 # B --> y = (x**3)+(A*x)+ B (mod P)
randomK = 5 # For encryption purpose 


class EllipticCurve :
    def __init__(self, a, b, p): # a is ConstantA_curve , b is ConstantB_curve, p is a prime number in (x ** 3)+(a*x)+b (mod P)
        """Function to initialize elliptic curve."""

        # Initialzing variables required in --> y = (x**3)+(A*x)+ B (mod P)
        self.a = a
        self.b = b
        self.p = p

    def addition(self, P1, P2) : # First and Second point
        """Function to add points on elliptic curve."""

        # Returning if points are at infinity (reach max)
        if P1.isInfinity() :
            return Dots(P2.x,P2.y)
        if P2.isInfinity() :
            return Dots(P1.x,P1.y)

        # If points are same
        if P1.equal(P2) :
            return self.selfAddition(P1) # find other point
        # Otherwise
        else :
            if P1.x == P2.x :
                return Dots(-1, -1)
            else :
                deltaX = (P1.x - P2.x) # x2 -x1
                lambdaY = ((P1.y - P2.y) * self.inverseModulo(deltaX)) % self.p # appply inverse in case it is not devisible like 2/3
                X3 = (lambdaY ** 2 - (P1.x + P2.x)) % self.p # slide 22
                Y3 = (lambdaY * (P1.x - X3) - P1.y) % self.p

                return Dots(X3,Y3)

    def selfAddition(self, point):
        # Addition on an elliptic curve mod p
        # Exceptional case
        if point.y == 0:
            return Dots(-1, -1)
        else :

            # Doing self addition
            gradient = ((3 * (point.x ** 2) + self.a) * self.inverseModulo(2 * point.y)) % self.p # Addition on an elliptic curve mod p
            newX = (gradient ** 2 - 2 * point.x) % self.p
            newY = (gradient * (point.x - newX) - point.y) % self.p

            # Returning result
            return Dots(newX, newY)

    def multiplication(self, point, constant): # constant --> private
        """Function to do multiplication on curve."""

        # Base case
        if constant == 1:
            return Dots(point.x, point.y)

        # Recursions
        if constant % 2 == 0:
            return self.selfAddition(self.multiplication(point, math.floor(constant / 2))) # Addition on an elliptic curve mod p
        else:
            tempPoint = self.multiplication(self.multiplication(point, math.floor(constant / 2)), 2)
            return self.addition(tempPoint, point)

    def inverseModulo(self, num): # inverse modulo operation

        # Computing inverse modulo
        for i in range(1, self.p):
            if (num * i) % self.p == 1 :
                return i
        return 0

    def generatePoints(self,x): # generate E(Zp) -->  points as a list

        # Initializing variables required
        tempList = []
        remainder = self.y(x) # x --> random number between 1 and primNumber P

        # Appending required points to list
        for y in range(1, self.p) :
                if y ** 2 % self.p == remainder :
                    tempList.append(y)

        # Returning list
        return tempList

    def y(self,x):
        # Elliptic Curve equation
        # Returning computed value
        return (x ** 3 + self.a * x + self.b) % self.p


class EllipticCurve :
    def __init__(self, a, b, p): # a is ConstantA_curve , b is ConstantB_curve, p is a prime number in (x ** 3)+(a*x)+b (mod P)
        """Function to initialize elliptic curve."""

        # Initialzing variables required in --> y = (x**3)+(A*x)+ B (mod P)
        self.a = a
        self.b = b
        self.p = p

    def addition(self, P1, P2) : # First and Second point
        """Function to add points on elliptic curve."""

        # Returning if points are at infinity (reach max)
        if P1.isInfinity() :
            return Dots(P2.x,P2.y)
        if P2.isInfinity() :
            return Dots(P1.x,P1.y)

        # If points are same
        if P1.equal(P2) :
            return self.selfAddition(P1) # find other point
        # Otherwise
        else :
            if P1.x == P2.x :
                return Dots(-1, -1)
            else :
                deltaX = (P1.x - P2.x) # x2 -x1
                lambdaY = ((P1.y - P2.y) * self.inverseModulo(deltaX)) % self.p # appply inverse in case it is not devisible like 2/3
                X3 = (lambdaY ** 2 - (P1.x + P2.x)) % self.p # slide 22
                Y3 = (lambdaY * (P1.x - X3) - P1.y) % self.p

                return Dots(X3,Y3)

    def selfAddition(self, point):
        # Addition on an elliptic curve mod p
        # Exceptional case
        if point.y == 0:
            return Dots(-1, -1)
        else :

            # Doing self addition
            gradient = ((3 * (point.x ** 2) + self.a) * self.inverseModulo(2 * point.y)) % self.p # Addition on an elliptic curve mod p
            newX = (gradient ** 2 - 2 * point.x) % self.p
            newY = (gradient * (point.x - newX) - point.y) % self.p

            # Returning result
            return Dots(newX, newY)

    def multiplication(self, point, constant): # constant --> private
        """Function to do multiplication on curve."""

        # Base case
        if constant == 1:
            return Dots(point.x, point.y)

        # Recursions
        if constant % 2 == 0:
            return self.selfAddition(self.multiplication(point, math.floor(constant / 2))) # Addition on an elliptic curve mod p
        else:
            tempPoint = self.multiplication(self.multiplication(point, math.floor(constant / 2)), 2)
            return self.addition(tempPoint, point)

    def inverseModulo(self, num): # inverse modulo operation

        # Computing inverse modulo
        for i in range(1, self.p):
            if (num * i) % self.p == 1 :
                return i
        return 0

    def generatePoints(self,x): # generate E(Zp) -->  points as a list

        # Initializing variables required
        tempList = []
        remainder = self.y(x) # x --> random number between 1 and primNumber P

        # Appending required points to list
        for y in range(1, self.p) :
                if y ** 2 % self.p == remainder :
                    tempList.append(y)

        # Returning list
        return tempList

    def y(self,x):
        # Elliptic Curve equation
        # Returning computed value
        return (x ** 3 + self.a * x + self.b) % self.p


class Dots :
    def __init__(self, x, y):
        """Function to initialize point of elliptic curve."""
        # Initialzing variables required
        self.x = x
        self.y = y

    def equal(self, otherPoint) : # to choose decide weather same points or not, if yes catch another point
        """Function to return boolean of whether equal or not."""
        # Returning boolean
        return self.x == otherPoint.x and self.y == otherPoint.y

    def isInfinity(self) : # check is it infinity or not, if yes ignore it

        # Returning boolean
        return self.x == -1 and self.y == -1

    def __str__(self): # return point in string form
        # Returning string
        return "(" + str(self.x) + "," + str(self.y) + ")"


class ECC :

    def __init__(self, curveA, curveB, prime, randomK, senderRandom, privateKey, encoding = 'ascii'):
        """Function to initialize variables."""

        # Initializing variables
        self.privateKey = privateKey # k --> Q=kP
        self.primeNumber = prime # P -->  Q=kP
        self.senderRandom = senderRandom # --> random value for x in equation --> y = (x**3)+(A*x)+ B (mod P) for generating points
        self.ellipticCurve = EllipticCurve(curveA, curveB, prime)
        self.randomK = randomK # for encryption purpose
        self.encoding = encoding # ASCII
        # Generating base
        self.generateBase() # Function to generate P --> Q=kP
        # Getting public key
        self.publicKey = self.ellipticCurve.multiplication(self.basePoint, privateKey) # Q --> Q=kP



    def encrypt(self, message) :
        # Initialzing ciphertext points list
        ciphertextPoints = [] # empty list

        # Encoding plaintext message
        encodedPoints = self.encodePlaintext(message)

        # Encrypting all the points
        for point in encodedPoints :
            ciphertextPoints.append(self.encryptPoint(point))

        # Returning result
        return ciphertextPoints

    def decrypt(self, cipherpoints) :
        """Function to perform decryption algorithm."""

        # Initialzing plaintext points list
        plaintextPoints = []

        # Decrypting all the point pairs
        for pointPair in cipherpoints :
            plaintextPoints.append(self.decryptPointPair(pointPair))

        # Decoding and returning answer
        return self.decodePoints(plaintextPoints)


    def generateBase(self): # P --> Q = kP
        """Function to generate base."""

        # Boolean for breaking
        isFound = False

        # Running till base is not found
        while not isFound:
            x = random.choice(range(1, self.primeNumber))
            yList = self.ellipticCurve.generatePoints(x)
            if len(yList) > 0:
                isFound = True
                self.basePoint = Dots(x, random.choice(yList))

    def encodePlaintext(self, plaintext):
        """Function to encode the plaintext."""

        # Getting byte array of plaintext according to encoding
        byteArray = bytearray(plaintext, self.encoding)

        # Initializing chunks list
        chunksList = []

        # For each byte
        for byte in byteArray :
            # For each number from 0 till random k
            for j in range(self.randomK) :

                # Performing operations as required in algorithm
                x = byte * self.randomK + j
                yList = self.ellipticCurve.generatePoints(x)

                # Breaking early if required
                if len(yList) > 0:
                    y = random.choice(yList)
                    chunksList.append(Dots(x, y))
                    break

        # Returning chunks list
        return chunksList

    def decodePoints(self, plaintextPoints):
        """Function to decode the plaintext points."""

        # Initialzing string required
        string = ""

        # Decoding
        for point in plaintextPoints :
            string += chr(math.floor(point.x / self.randomK))

        # Returning decoded value
        return string

    def encryptPoint(self, point):
        """Function to encrypt a point."""

        # Performing multiplication and addition for encryption as required
        firstCipher = self.ellipticCurve.multiplication(self.basePoint, self.senderRandom) # (P,d)
        secondCipher = self.ellipticCurve.addition(point, self.ellipticCurve.multiplication(self.publicKey, self.senderRandom)) # (Q,d)

        # Returning answer
        return [firstCipher, secondCipher]

    def decryptPointPair(self, pointPair) :
        """Function to encrypt a point pair."""

        # Getting first block and its inverse
        firstBlock = self.ellipticCurve.multiplication(pointPair[0], self.privateKey) #first pair
        firstBlockInverse = Dots(firstBlock.x, (-firstBlock.y) % self.primeNumber) #second pair

        # Returning the addition to get answer
        return self.ellipticCurve.addition(pointPair[1], firstBlockInverse) # to get P3 pairs (x,y)

def main():
    # Initializing elliptic cryptographic curve
    ellipticCurveCrypto = ECC(ConstantA_curve, ConstantB_curve, primeNumber, randomK, randomSender, nTimes)

    inputMessage = input(U+"\nAlice: \n"+C+"Enter your message to encrypt it : "+W)

    # Encrypting input message
    cipherpoints = ellipticCurveCrypto.encrypt(inputMessage)

    # Decrypting cipherpoints obtained
    decryptMassege  = ellipticCurveCrypto.decrypt(cipherpoints)

    # progress bar
    from time import sleep
    from tqdm import tqdm
    for i in tqdm(range(10)):
        sleep(0.07)
    # Printing encrypted result
    print(C+"\nEncrypted message: \n"+W)
    for pair in cipherpoints :
        print(pair[0], pair[1])
    encrpytionHash = hashlib.sha256(inputMessage.encode("UTF-8")).hexdigest()  
    print ("Hash of encryption message: " + encrpytionHash)
    decryptionHash = hashlib.sha256(decryptMassege.encode("UTF-8")).hexdigest() 
    print ("Hash of decryption message: " + decryptionHash)
    # Printing decrypted result
    print(U+ "\nHi Bob"+C+ "\nDecypted plaintext is :"+W, decryptMassege, "\n"+W)

    if decryptionHash == decryptionHash: 
        print(C + "[*] " + W + "Verification successful")
    else:
        print(C + "[*] " + W + "Verification failed")


main()