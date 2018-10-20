Writeup 7 - Forensics I
======

Name: Sthitadheesh Nelapatla
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 7 writeup

### Part 1 (40 pts)

1. The given image file is a JPEG file. 

2. The photo was taken at the John Hancock Center in Chicago, Illinois

3. The photo was taken on August 22nd 2018 at 11:33 (timestamp: 2018:08:22 11:33:24)

4. An Apple IPhone 8 rear 12.2 megapixel camera was used to take this photo

5. 539.5 m

6. CMSC389R-{look_I_f0und_a_str1ng} and CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

*Flag: CMSC389R-{dropping_files_is_fun}*

I began by installing cutter and opening the binary file in cutter. This allowed me to look at the assembly code. In the comments for the assembly code, I found the characters ```/tmp/.stego``` being written to the filename variable and then I went to the imports tab and saw fopen, fclose, fwrite and puts. I realized that this assembly code was writing a file called .stego. I ran the binary by simply running ```./binary``` and navigated to /tmp and found a file called stego. I initially used strings and grep to hope to find the file like the first part. However, that did not output anything I then ran ```binwalk --dd=".*" .stego``` which is similar to the procedure used for the second flag in the first part. I found a file called 1 and tried the same strings and grep formula to no avail. At this point, I determined the type of 1 by running ```file 1``` which told me that the file was a JPEG. I installed ImageMagick onto my machine and ran ```display 1``` to open the file. I was hoping to find a flag but I found a giant stegosaurus. Given that the file was called stego and there was a picture of a stegosaurus, I guessed that some kind of steganography was going on and ran ```steghide extract -sf 1 -xf out.txt``` which prompted me for a password. Using the photo as a hint, I guessed stegosaurus and then found that the output was written to out.txt. I then simply ran ```cat out.txt``` to discover the flag. 
