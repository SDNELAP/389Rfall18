Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Sthitadheesh Nelapatla*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Sthitadheesh Nelapatla*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. Twitter, Reddit, Videobam - Discovered by using OSINT Framework to search username. 
    Email address: kruegster@tutanota.com

3. 142.93.118.186 - I got this IP address by nmapping the domain of his website

4. There is a hidden directory called secret. Inside of it the following flag was found: 'CMSC389R-{fly_th3_sk1es_w1th_u5}'

5. 142.93.117.193 - His admin page is currently underconstruction and the domain address provides the IP of the server hosting the admin page

6. The associated admin server is located at 101 Ave of the Americas 10th floor New York, NY 10013

7. Apache/2.4.18 (Ubuntu) determined by entering a false directory after ip address of the site i.e. http://142.93.118.186 /asvji

8. 'CMSC389R-{h1dden_fl4g_in_s0urce}'

### Part 2 (55 pts)

*I ran nmap 142.93.117.193 -p- and found a list of open ports. I then found the port of interest to be 1337 after trying to nc into each of the ports outputted by the nmap. Using OSINT, I determined his username to be kruegster and used his interest in Pokemon Go reflected on his Twitter account to guess pokemon as the password and unexpectedly got in on the first try. *

