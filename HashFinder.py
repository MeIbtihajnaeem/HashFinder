from hash_algo import HashAlgo

def start():
    print("""\
        This script is designed to accept a hash and utilize a dictionary brute force approach
        to attempt to find the original text. By leveraging this approach, the script is able
        to systematically iterate through a dictionary file and test each entry to determine
        if it matches the provided hash.

        Supported hash methods:
        - MD5 : 32
        - SHA1 : 40
        - SHA224 : 56
        - SHA256 : 64
        - SHA384 : 96
        - SHA512 : 128
        - BLAKE2B : 128
        - BLAKE2S : 64
        - SHA3_224 : 56
        - SHA3_256 : 64
        - SHA3_384 : 96
        - SHA3_512 : 128
        """)
def runProgram():
    hashedText = input("Please enter the hash: ")
    while not hashedText:
        print("Hashed text cannot be empty.")
        hashedText = input("Please enter the hash: ")
    customFile = ""

    while not customFile:
        customFile = input('''
        Please enter the file path and name of the dictionary file to use for the brute force 
        approach.
        ''')
    HashAlgo().findValueOfHash(hashedText,customFile)
def main():
    while True:
        start()
        runProgram()
        anotherHash = input("Do you want to run the program for another hash? (y/n)")
        if anotherHash.lower() != 'y':
            print("Exiting program...")
            break

main()    