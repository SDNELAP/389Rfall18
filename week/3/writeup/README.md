Writeup 3 - OSINT II, OpSec and RE
======

Name: *Sthitadheesh Nelapatla*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Sthitadheesh Nelapatla*

## Assignment 3 Writeup

### Part 1 (100 pts)
*Fred Krueger's company servers have several underlying security flaws which made them quite vulnerable to OSINT attacks. I will attempt to describe a few of those flaws and some potential fixes to fix these flaws and make the system more secure than it currently is right now.  

1. **Exposed IP Address**: The first major issue that made the brute-force attack on the server possible was the fact that the IP Address of the admin page was simply displayed in the address bar. Instead of this, I would advise the use of a VPN software on the server machine to conceal the original ip address. Another solution the admin can employ is the use of a dynamic DNS service such as http://DynDNS.com to create a custom subdomain in the Cornerstone website pointing to the admin server to hide the ip address. 

2. **Unprotected Secret Directories**: The secret directories such as the directory called "secret" found in the robots.txt file of the website, were not secure and were accessible by applying the extensions to the website domain. To fix this on the Apache server, the admin should setup a .htaccess file and build rules to hide and/or redirect the page away from those secret directories. More information on how to do this can be found at http://corz.org/server/tricks/htaccess.php 

3. **Weak Password**: The server security had a poor password that was clearly derived from the user's interests in Pokemon on his Twitter account. Hence, my recommendation would be to use a randomly generated password using a website like passwordgenerator.net or lastpass.com/password-generator that is absolutely independent from one's personal interests. Furthermore, the administrator should also create a system where the IP address of a system with several login failures is flagged and locked out from logging from that IP to protect against brute force attacks. This feature is already a part of several intrusion detection and prevention systems such as which can be installed on the web server like Jupiter Networks. I would strongly suggest that the system administrator consider investing some money into the installation of an effective IDS/IPS service on the webserver to prevent anamolous network activity. See https://www.juniper.net/us/en/products-services/what-is/ids-ips/ for more details.
*
