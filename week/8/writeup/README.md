Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Sthitadheesh Nelapatla
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. The hackers used traceroute on two particular IP addresses. The first IP address was ```128.8.120.43``` which belongs to the UMD Cybersecurity club. The second IP address was ``` 216.58.219.238``` which is the Google website. 

2. laz0rh4x and c0uchpot4doz are the hackers communicating in the network. 

3. Their IP addresses are 142.93.118.186 and 104.248.224.85. They are both located on the 10th floor of 101 Ave of the Americas, New York, NY 10013

4. laz0rh4x was operating on port 2749 and c0uchpot4doz was operating on port 33794. 

5. They mentioned their plans in the chatroom that they are planning on meeting tomorrow at 3:00 p.m. and shared the updated plans in the form of a file called update.fpff

6. They shared the updated plans in the form of a file called update.fpff using the following google drive link: https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. They are planning to meet on October 25th 2018 at 3:00 p.m. based on the the fact that they say tomorrow at 1500 and the message timestamp for the arrival of the packet says that it was recieved on October 24th at 10:42:48 EDT

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. The update.fpff file was generated at the following time: ```2018-10-24 20:40:07```

2. laz0rh4x authored the document

3. It says that there are 9 but there are 11 in actuality

4.

Section 1
ASCII
b'Call this number to get your flag: (422) 537 - 7946'

Section 2
WORDS
[b'\xef\xbe\xad\xde', b'\x01\x00\x00\x00', b'\xe7\x10\xd1[', b'laz0', b'rh4x', b'\t\x00\x00\x00', b'\t\x00\x00\x00', b'3\x00\x00\x00', b'Call', b' thi', b's nu', b'mber', b' to ', b'get ', b'your']

Section 3
COORD
lat: 38.99161 long: -77.02754

Section 4
REFERENCE
1

Section 5
ASCII
b'The imfamous security pr0s at CMSC389R will never find this!'


Section 6
ASCII
b'The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}'


Section 7
COORD
lat: 38.9910941 long: -76.9328019


Section 8
PNG

Section 9
ASCII
b'AF(saSAdf1AD)Snz**asd1'


Section 10
ASCII
b'Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9\n'


Section 11
DWORDS
[b'\xef\xbe\xad\xde\x01\x00\x00\x00', b'\xe7\x10\xd1[laz0', b'rh4x\t\x00\x00\x00', b'\t\x00\x00\x003\x00\x00\x00', b'Call thi', b's number']


5. ```CMSC389-{c0rn3rst0ne_airlin3s_to_the_m00n};CMS389R-{PlaIN_dIfF_FLAG};CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}```
