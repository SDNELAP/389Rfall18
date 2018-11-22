Writeup 10 - Crypto II
=====

Name: Sthitadheesh Nelapatla
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 10 Writeup

### Part 1 (70 Pts)

I began this assignment by using the provided notary port to connect manually and understand how the Digital Notary works. I realized that the first argument required by the program is the function that you want to run. Either signing data or testing a signature's validity. Given that part 1 needs us to calculate the forged hash as it says in the stub code, I finished the first step of part 1 by simply communicating with the server and parsing the hash output and saving that to the provided legit value in the stub code. 

With step 2 of part 1, the process of constructing the padding was initially very confusing for me. I realized that the first byte had to be 1 and the remaining padding had to be zeroes. I initially tried using a for loop to append \x00 based on my calculations but that wasn't working for me (most probably because I don't understand the inclusivity of Python's range function). I found a way to generate a string of repeated substrings using the integer multiplication operator on Stack Overflow and used it. I had initial issues because I placed the inital ```padding = '\x80'``` outside the for-loop which caused all of the padding to be appended across multiple iterations. After I found that bug,I finally found the following flag: CMSC389R-{i_still_put_the_M_between_the_DV} 

### Part 2 (30 Pts)

Referring to the slides, I noticed that gpg command line tool is useful in generating public key private key pairs. By using the command ```gpg --gen-key``` in the slide, I was able to enter my information and generate a new key. From there, I ran ``` gpg --import pgpassignment.key ``` which imported the key and showed me that the owner of this key was UMD Cybersecurity Club. I then used the ```gpg -e -u "Sthitadheesh Nelapatla" -r "UMD Cybersecurity Club" message.txt``` and created a file called message.txt which had the following text: Om Namo Narayanaya. This created a messages.txt.gpg file and I renamed that file as messages.private and moved it to the writeup folder. 


