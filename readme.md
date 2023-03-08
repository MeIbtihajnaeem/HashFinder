# HashFinder
HashFinder is a Python script that allows users to input a hash and then utilizes a dictionary-based brute force approach to attempt to find the original text. By leveraging this approach, the script systematically iterates through a dictionary file and tests each entry to determine if it matches the provided hash. HashFinder automatically detects the hash type based on its length and supports a variety of popular hash types, such as MD5, SHA-256, SHA-512, and more.

## Dependencies

- HashFinder requires Python 3 and the hashlib library, which is included with Python by default.

## Usage
To use HashFinder, run the following command:
```sh
python3 HashFinder.py
```

## Credits
HashFinder was inspired by the Naive Hashcat project by Brannon Dorsey: https://github.com/brannondorsey/naive-hashcat. The rockyou.txt dictionary file was also sourced from that project.