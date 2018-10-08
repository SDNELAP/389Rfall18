section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, rdx  ;moves string length parameter into counter register
        mov rbx, rdi  ;moves string pointer into permanent register
        mov r8, 0     ;set pointer offset increment to 0 

str_loop: 
        mov byte [rbx + r8], sil; copy char val into relevant pointer addresses(pointer + increment)
        add r8, 1     ; increment counter
        loop str_loop ; loop this process

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;
        mov rcx, rdx  ;moves string length parameter into counter register
        mov rbx, rdi  ;moves destination pointer into permanent register
        mov r12, rsi  ;moves source pointer into permanent register
        mov r8, 0     ;set pointer offset increment to 0 

str_cpy_loop:
        mov bl, byte [r12 + r8];copy value at source pointer into temp variable
        mov byte [rbx + r8], bl;copy temp variable into destination pointers address
        add r8, 1     ; increment counter
        loop str_cpy_loop ; loop this process


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
