'''
Bitwise operators
1) ~ (Two's Complement)  
  To calculate Two's Complement there are two steps 1] reverse the sign 2] substract 1
  E.g.) ~125 = -125 -1 = -126
  
2) << (Left Shift)  
  To calculate Left Shift multiply a by 2 raised to n
  a << n = a * (2^n)
  
   E.g.) 20<<2 gives 80


3) >> (Right Shift)
  To calculate Right Shift floor divide a by 2 raised to n
  a >> n = a // (2^n)
  
   E.g.) 100 >> 2 gives 25
   
 4) & [AND GATE]
 
 5) | [OR GATE]
 
 6) ^ [XOR GATE]
 
'''
Interview Question
1)  Divide a num to its half without division operator?
=> Right Shift by 1 ie n>>1 

2) Swap 2 variables using bitwise operator?

=> It takes 3 steps
    a = a ^ b
    b = a ^ b
    a = a ^ b
