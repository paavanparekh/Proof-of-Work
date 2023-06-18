#IT486:     Blockchains and Cryptocurrencies
# Homework1: Proof of Work
# Author:    Paavan Parekh
#Date:      30/9/22

# importing useful libraries
from cmath import nan
import hashlib
import sys
import time
import math
from math import log
from itertools import product
from string import ascii_letters, digits, punctuation, ascii_lowercase, ascii_uppercase
# maximum length of prefix that we are going to have otherwise my computer
# have to check infinite possibilities
max_len_prefix = 10
# number of leading zeros in hexadecimal digits
hex_dict = {'0': 4, '1': 3, '2': 2, '3': 2, '4': 1, '5': 1, '6': 1,
            '7': 1, '8': 0, '9': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}

# counting leading zeros in hash


def count_leading_zeros(hash):
    cnt = 0
    for ch in hash:
        if ch != '0':
            return cnt + hex_dict[ch]
        else:
            cnt = cnt + 4


# to h=generate all possible combinations of prefixes we only have to
# use ascii printable characters which are from 33-126
ascii_printable_chars = ''
for i in range(33, 127):
    ascii_printable_chars += chr(i)

# to get pow string try all possible combination of string of each
# length (<= max_len), the one string which have at least d leading
# zeros is our pow string.(d = difficulty bits)


def proof_of_work(header, difficulty_bits):
    itr = 0  # no of iterations to reach pow string
    for len in range(max_len_prefix):
        for W in product(ascii_printable_chars, repeat=len+1):
            itr = itr+1
            prefix = ''.join(W)
            prefix_hash_msg = prefix+str(header)
            prefix_hash_msg = prefix_hash_msg.encode('utf-8')
            Hash = hashlib.sha256(prefix_hash_msg).hexdigest()
            if count_leading_zeros(Hash) >= difficulty_bits:
                return (Hash, prefix, itr)

    return (nan, nan, nan)

# returns sha-256 hash value of whole file


def hash_file(filename):
    hs = hashlib.sha256()  # hash object
    with open(filename, 'rb') as file:
        buff = 0
        while buff != b'':
            buff = file.read(1024)
            hs.update(buff)
    return hs.hexdigest()  # hash in hex format

# function pow-create which creates pow string for given file.
# this pow string when prefixed to a hash of the given file (file), will
# result in a SHA-256 hash that contains nbits of leading 0s.


def pow_create(nbits, file_name):

    header = hash_file(file_name)  # initial hash of file
    start_time = time.time()  # start time
    Hash, prefix, iter = proof_of_work(header, nbits)  # get pow string for header
    end_time = time.time()  # end time
    elapsed_time = end_time-start_time  # total time to get pow string
    leading_bits = count_leading_zeros(Hash)  # leading bits in resultant hash
    # Writing outputs into file 
    output_filename=file_name.strip().split("/")[2]+".pow"
    with open(output_filename, "w") as f:
        print('File:', file_name, file=f)
        print('Initial-hash:', header, file=f)
        print('Proof-of-work:', prefix, file=f)
        print('Hash:', Hash, file=f)
        print('Leading-bits:', leading_bits, file=f)
        print('Iterations:', iter, file=f)
        print('Compute-time:', elapsed_time, file=f)
    return file_name, header, prefix, Hash, leading_bits, iter, elapsed_time

# main function


def main():

    try:
        nbits = int(sys.argv[1])
        if nbits < 0:
            print('Difficulty bits must be positive number')
    except:
        print('Difficulty bits must be positive number')

    file_name = sys.argv[2]
    f = open(file_name, 'rb')
    if not f:
        print('File cannot open')
    # get pow string for file and see results in output.txt
    pow_create(nbits, file_name)


# driver programme
if __name__ == "__main__":
    main()
