Writeup 3 - Pentesting I
======

Name: *Sthitadheesh Nelapatla*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Sthitadheesh Nelapatla*

## Assignment 4 Writeup

### Part 1 (45 pts)
I began by running ```nc cornerstoneairlines.co 45``` provided in the description. This took me to a portal requesting an IP Address. I initially tried several IP addresses found in previous assignments to no avail. However, I checked to see if the IP input field itself was vulnerable to command injection. So I tried inputting ```echo; ls /```, which output the list of directories on the system. I then understood that commands could be directly injected into the system from the IP input. Therefore, I found the location of the flag by running ```nc cornerstoneairlines.co 45``` again and inputted ```echo; find . -type f -name "*.txt";``` to find all text files on the system. That command outputted the path ```./home/flag.txt``` So I went through the process of nc'ing into the system one more time and ran ```echo; cat ./home/flag.txt``` to output the flag in the text file which was ```CMSC389R-{p1ng_as_a_$erv1c3}```.

To better understand how to fix the vulnerability, I went back into the system and ran ```echo; find . -type f -name "*.sh";``` to find which shell script was processing the IP Address input. After looking through each file, I found in /opt/container_startup.sh that the script was simply taking the input and running ```ping -w 5 -c 2 $input``` where ```$input``` is the variable that stores the input. This makes it possible for attackers to simply inject commands by adding any input followed by ';' and whatever code they would like to execute. To prevent this, the first thing he should do is some variation of sanitizing his inputs and ensuring that the input is in fact an IP address and not some random arbitrary input. Perhaps Fred can check if the input matches a certain IP address format and also ensure that no special characters (like ';' or '&&' or '|' etc. ) are used using conditional statements before sending the input into the ping command. 

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
