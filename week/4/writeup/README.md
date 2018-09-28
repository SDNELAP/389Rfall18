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

Going off of the solution for part one, I realized that the only way to construct an interactive shell would be to enter each command one by one, keep track of the current directory and change into that directory before each command and display that directory in the prompt. This simply involved keeping track of command inputs involving ```cd``` with the special case of ``` cd ..``` . For all other commands, all I did was use ```echo;cd <current_directory>; command`` to escape the IP input and then change into the current directory even though it seems as though we are already in that directory based on the prompt and run the command and print the output. We then update the new_directory as needed and return it so it can be used by future commands. The outer shell was a matter of using an infinite loop with four if statements to check each of the possible commands. 

The only other command other than the shell command which was intellectually stimulating was the ```pull``` command. For this command, the only viable solution that I could think of was to receive the output of using ```cat <remote_path>``` and write that decoded output to the <local_path> as provided. Implementing it was not as difficult as it appeared to be as it was simply running ```echo; cat <remote_path>``` once connected to the server. The shell was a bit confusing given that we had to go through several string manipulations to keep track of the current directory. However, conceptually it was rather straightforward. This assignment is a prime example of how assignments can appear to be quite overwhelming initially but end up being clear once you begin working on it. 