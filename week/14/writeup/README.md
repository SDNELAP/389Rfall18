Writeup 10 - Crypto II
=====

Name: Sthitadheesh Nelapatla
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 10 Writeup

### Part 1 (70 Pts)

I saw the s q l bold hint which led me to think that I had to use SQL injection for this problem. I walked through the page and saw the item= field and thought that this is the attack vector that I have to use. From here, I tried ```http://cornerstoneairlines.co:8080/item?id=';--``` but that gave me an Internal Server Error. Going back through the slides, I found that we can try to use or 1=1 within to make it return everything so I tried ```http://cornerstoneairlines.co:8080/item?id='or 1='1;--``` which gave me the flag CMSC38R-{y0U-are_the_5ql_n1nja}. 
### Part 2 (30 Pts)

The first level I beat simply by injecting ```<script>alert("PWNED")</script>```

I initially started off the second level by trying to inject an alert into the text but that did not work. I was absolutely clueless and used up the all the hints. Finally, after seeing the final hint, I realized that I needed to enter a dummy image and give it an onerror attribute and entered ```<img src="abc.png" onerror="alert("PWNED)"/>``` and that did the trick. 

For level 3, I spent a really long time digging through the Javascript code trying to find where it processes URL changes and eventually used the first hint which told me to do just that. After I dug through the javascript, I found that I had to manipulate the window.location and tried ```https://xss-game.appspot.com/level3/frame#67' onerror ="alert("PWNED)"``` as the url and it worked. 

For level 4, I was absolutely clueless with this one. I looked at the first few hints and found the startTimer function after crawling through the code. I realized that it was directly putting the code in as it is in between apostrophes so I escaped the apostrophe and reopened it with ```');alert("PWNED");console.log('```

For level 5, I tried the same thing as level 4 to no avail. I opened all the hints and opened the link they gave me which then showed that you could append javascript:doSomething() to a particular function in the url. So I entered the url ````https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("PWNED")``` and entered my email and pressed Next and I beat the level. 

For the final level, I began this level by looking through the web for a solution to no avail. I once again opened all the hints and went to the google link they gave and found that it returned the callback function given. I tried to do ```https://www.google.com/jsapi?callback=alert()``` and got a message saying http not allowed so I modified it to ```httpS://www.google.com/jsapi?callback=alert()``` but it still did not work. I quickly realized that I did not need the parentheses after the alert and submitted ```httpS://www.google.com/jsapi?callback=alert``` and it finally worked.  This was incredibly difficult overall. 