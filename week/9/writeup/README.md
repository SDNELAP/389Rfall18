Writeup 9 - Crypto I
=====

Name: Sthitadheesh Nelapatla
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 9 Writeup

### Part 1 (60 Pts)
The first part of the project was intuitively quite simple. I understood that I had to iterate through the text files and try to crosscheck the sha512 hash of the salt characters appended to the passwords given in the wordlist against the list of hashes given. I had problems with the file opening and reading process when using the ```wordlist.readlines()``` function but eventually found that a better way to interact with files in python was ```with open('probable-v2-top1575.txt','r') as f1``` Doing this solved my file problems and gave me the following output
```Hash:9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458
Salt: k  Password: neptune
Hash: c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8  Salt: m  Password: jordan
Hash: 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f  Salt: p  Password: pizza
Hash: d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267  Salt: u  Password: loveyou```


### Part 2 (40 Pts)

I tried nc'ing into the server where I was faced with various hashes. I wrote an algorithm to split the questions and find the hash algorithm and text based on the position of the word "Find" and sent the appropriate hash based on the algorithm requested. This worked until I found the flag but ran into an error in the parsing process. I then created a condition to check if "Find" was contained in the data and if it wasn't it meant we found the flag which was the last word of the output so I output the last word of the data to print the flag. 
