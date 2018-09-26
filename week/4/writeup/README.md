Writeup 3 - Pentesting I
======

Name: *Sthitadheesh Nelapatla*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Sthitadheesh Nelapatla*

## Assignment 4 Writeup

### Part 1 (45 pts)
*I began by running ```nc cornerstoneairlines.co 45``` provided in the description. This took me to a portal requesting an IP Address. I initially tried several IP addresses found in previous assignments to no avail. However, I checked to see if the IP input field itself was vulnerable to command injection. So I tried inputting ```echo; ls /```, which output the list of directories on the system. I then understood that commands could be directly injected into the system from the IP input. Therefore, I found the location of the flag by running ```nc cornerstoneairlines.co 45``` again and inputted ```echo; find . -type f -name "*.txt";``` to find all text files on the system. That command outputted the path ```./home/flag.txt``` So I went through the process of nc'ing into the system one more time and ran ```echo; cat ./home/flag.txt``` to output the flag in the text file which was ```CMSC389R-{p1ng_as_a_$erv1c3}```*

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
