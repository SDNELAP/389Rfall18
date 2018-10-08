Writeup 5 - Binaries I
======

Name: *Sthitadheesh Nelapatla*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Sthitadheesh Nelapatla

## Assignment 5 Writeup

Initially, I found the assignment to be a bit confusing but as I read through the slides, the process of implementing the methods provided became more clear. For both parts of assignment I began with a few common operations. The stub code provided took care of saving the stack pointer and adjusting the stack pointer to the new function location. From there, I began by moving the string length parameter in to the rcx register by using the following command: 

```mov rcx, rdx ``` 


Given that parameters passed into a function in x86 are stored in the rdi, rsi and rdx registers in that order. With that said, I moved the third parameter based on the provided method signatures 

```c
void memset(char *str, char val, int strl)
```

and 

```c
void strncpy(char *dst, char *src, int len)
```

which is the length of the string in both parts into the counter parameter. I then followed by moving the first parameter into permanent registers in the line 

```
mov rbx, rdi  
```

to ensure that it is stored after function execution because the purpose of the function is for the parameter passed in passed in to be used after function execution is over. This assumption based on my experience with the C language. The next command moves the number 0 into the impermanent r8 register to use as an for the address of the string pointer that needs to be modified. 

From that point, the next few lines are the only lines that differ between part 1 and part 2. For the first part, the logic is that we need to move the provided character parameter into each character of the string so beginning at the pointer address provided at a parameter, we loop an instruction to increment the r8 register from 0 and dereference the address beginning at the initial pointer and incrementing r8 addresses to it and assigning to the character value provided through the following command: 

```str_loop: mov byte [rbx + r8], sil ``` which is equivalent to the C command is 

```*(str + i) = val)``` 
where i is the increment value added onto the address str. Initially, I copied the second parameter into permanent register also but then realized that it would be efficent to use the 1 byte resgister representing rsi which is sil. The second part of the assignment which requires us to copy one string to another is achieved by moving the contents of the src pointer incremented by a certain quantity less than the length of the string by to the dest pointer incremented by the same increment through the following commands: 

```str_cpy_loop: mov bl, byte [r12 + r8];copy value at source pointer into temp variable
    mov byte [rbx + r8], bl;copy temp variable into destination pointers address``` 
which is equivalent to the C command 
```*(dst + i) = *(src + i)``` 
where i is the increment value added onto the addresses dst and src. I had to use a single byte register bl as the temporary register to transfer each character from one string to another. After this point the only commands that remain are 

```
add r8, 1     ; increment counter
loop str_loop ; loop this process
```
which are common across both parts and are used to increment r8 and loop the code beginning from the str_loop name until rcx or the counter register containing the value of the string length parameter decrements to zero which ensures that we will not corrupt an invalid address space. The remaining stub code took care of moving down the stack pointer and restoring the previous base pointer and returning from the function. Overall, this assignment was insightful and took me back to the days of 216 where careful consideration about registers and pointer increments was incredibly important and once I got into that mindset, the problem appeared to be relatively straight forward. 


