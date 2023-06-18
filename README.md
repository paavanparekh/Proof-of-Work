IT486:     Blockchains and Cryptocurrencies

Title:     Generation and Verification of Proof-of-Work

Author:    Paavan Parekh

Date:      30/9/2022

* Steps to run the code: 

  1. Open any Python compiler
  2. Run files from terminal using command: python -u "file_address" args
  3. See results on console or output files

* Proof-of-Work Create (pow_create):

      Two arguments:
    
      1.number of difficulty bits
      2.input file address
      
      for eaxmple,
      python -u "d:\Users\paava\OneDrive\Desktop\sem 7\Blockchain & Cryptocurrencies\HW1\pow_create.py" 20 ./testfiles/walrus.txt
      (python -u <file address> arg1 arg2)

* Proof-of-Work check (pow_check)

       Two arguments:
 
        1.address of pow header file(file in which result of pow create function are stored)
        2.address of original file
  
      for example,
      python -u "d:\Users\paava\OneDrive\Desktop\sem 7\Blockchain & Cryptocurrencies\HW1\pow_check.py"  output.txt ./testfiles/abc 
