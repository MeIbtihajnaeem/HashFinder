from hash_algo import HashAlgo

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

hashedText = input("Please enter the hash: ")
customFile = input('''
Please enter the file path and name of the dictionary file to use for the brute force 
approach. If you want to use the default file 'rockyou.txt', simply press enter without 
typing anything.
''') or "rockyou.txt"
HashAlgo().findValueOfHash(hashedText,customFile)
