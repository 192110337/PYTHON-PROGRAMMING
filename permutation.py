i = 0 1 2 3
    A B A C
index = 0, s[0] = A
Start swapping s[index] with s[i] following it:
i = index + 1 = 1 

Since s[index] != s[i], swap and recur.

i = 2, s[index] == s[i], dont swap

i = 3,  s[index] != s[i], swap and recur. 
