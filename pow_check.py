#IT486:     Blockchains and Cryptocurrencies
# Homework1: Proof of Work
# Author:    Paavan Parekh
#Date:      30/9/22

# importing useful libraries
import hashlib
import sys
import math
from math import log

# returns sha-256 hash value of whole file


def hash_file(filename):
    h = hashlib.sha256()  # hash object
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()  # hash in hex format

#verifier: pow-check

# The command is provided a file wih the headers (generated by the pow-create command and
# a file with the original message. It validates the headers against the file.
# These are the tests it performs:
# • It checks the value of the Initial-hash in the header.
#  This is the SHA-256 hash of the message.
# • It computes the hash of the Proof-of-work string in the header concatenated with that
#  initial hash string. This value should match the Hash header.
# • Finally, it checks that the number in the Leading-bits header exactly matches the number
#  of leading 0 bits in that Hash header.
# The result of pow-check will be a pass or a fail. If passed, simply print a ‘pass’ message.
# If any tests failed, specify which of these tests failed.


def pow_check(pow_header, file_name):

    file1 = open(pow_header, 'r')
    Lines = file1.readlines()
    Headers = []  # contains information about what we have computed using pow-create function
    for line in Lines:
        Headers.append(line.strip().split(": ")[1])

    init_hash = hash_file(file_name)
    res_hash = hashlib.sha256((Headers[2]+str(init_hash)).encode('utf-8')).hexdigest()

    cond1 = str(init_hash) == Headers[1]  # check initial hash values
    cond2 = str(res_hash) == Headers[3]  # check final hash values
    cond3 = str((256-math.floor(log(int(res_hash, 16), 2))-1)) == Headers[4]  # check difficulty bits

    if cond1 and cond2 and cond3:  # if all conditions are true
        return "pass"
    elif not cond1:
        return "initial hash not matches"
    elif not cond2:
        return "final hash not matches"
    else:
        return "leading bits not matches"


def main():
    file_name1 = sys.argv[1]
    f1 = open(file_name1, 'rb')
    if not f1:
        print('File cannot open')

    file_name2 = sys.argv[2]
    f2 = open(file_name2, 'rb')
    if not f2:
        print('File cannot open')
    # verify your proof of work
    print(pow_check(file_name1, file_name2))


# driver programme
if __name__ == "__main__":
    main()
