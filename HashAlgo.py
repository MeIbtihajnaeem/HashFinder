import hashlib

class HashAlgo():
    _myList = []
    _hashDictionary ={
            "MD5" : 32, 
            "SHA1" : 40,
            "SHA224" : 56,
            "SHA256" : 64,
            "SHA384" : 96,
            "SHA512" : 128,
            "BLAKE2B" : 128,
            "BLAKE2S" : 64,
            "SHA3_224" : 56,
            "SHA3_256" : 64,
            "SHA3_384" : 96,
            "SHA3_512" : 128
    }
    def __init__(self):
        _myList =[]
        for name,length in self._hashDictionary.items():
            _myList.append(HashType(name,length))
        self.myList = _myList

    def _findHashType(self,hash):
        data = [x for x in self.myList if x.length ==len(hash)]
        return data
    
    def _createHashDocument(self,hashType,fileName):
        outputFileName = hashType.name+".txt"
        hashTypeName = hashType.name+""
        if hashTypeName == "MD5":
            hashLibMethod = hashlib.md5
        elif hashTypeName == "SHA1":
            hashLibMethod = hashlib.sha1
        elif hashTypeName == "SHA224":
            hashLibMethod = hashlib.sha224
        elif hashTypeName == "SHA256":
            hashLibMethod = hashlib.sha256
        elif hashTypeName == "SHA384":
            hashLibMethod = hashlib.sha384
        elif hashTypeName == "SHA512":
            hashLibMethod = hashlib.sha512
        elif hashTypeName == "BLAKE2B":
            hashLibMethod = hashlib.blake2b
        elif hashTypeName == "BLAKE2S":
            hashLibMethod = hashlib.blake2s
        elif hashTypeName == "SHA3_224":
            hashLibMethod = hashlib.sha3_224
        elif hashTypeName == "SHA3_256":
            hashLibMethod = hashlib.sha3_256
        elif hashTypeName == "SHA3_384":
            hashLibMethod = hashlib.sha3_384
        elif hashTypeName == "SHA3_512":
            hashLibMethod = hashlib.sha3_512
        else:
            raise ValueError("Invalid hash type name")

        with open(fileName, 'r') as f_input, open(outputFileName, 'w') as f_output:
            for line in f_input:
                line = line.strip().encode('utf-8')
                hash_value = hashLibMethod(line).hexdigest()
                f_output.write(hash_value + ' ' + line.decode('utf-8') + '\n')
        return outputFileName

    def _detectHash(self,listOfGeneratedFiles,hash):
        listOfFoundValues = []
        for file_path in listOfGeneratedFiles:
            with open(file_path, "r") as file:
                for line in file:
                    splitedLine = line.split(" ")
                    if splitedLine[0].strip() == hash.strip():
                        listOfFoundValues.append(splitedLine[1])
        if(len(listOfFoundValues)>0):
            for item in listOfFoundValues:
                print("Found password is "+item)
        else:
            print("No match found")
                        

    def findValueOfHash(self,hash,fileName):
        typeOfHash = self._findHashType(hash)
        listOfGeneratedFiles =[]
        for item in typeOfHash:
            listOfGeneratedFiles.append(self._createHashDocument(item,fileName))
        self._detectHash(listOfGeneratedFiles,hash)
        

            




class HashType:
    name=""
    length=0
    def __init__(self,name,length):
        self.name=name
        self.length = length


