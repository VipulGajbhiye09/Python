# Dynanmic casting - Python automatically assigns data type to variable

a=10       #integer 

b=3.14     #float 

c="abc"    #string 

d=True     #boolean 

'''
Q] Primitive data types in python?

1)int 2)float 3)str 4)bool 5)complex

'''
num = input("Enter a number")  #prompt message will be displayed on terminal
'''
default mode of input is string
'''
type(num) #string

#type casting
count = int( input("Enter a number") )

type(count) #int

'''
Logical operators
1) and   2) or  3) not
'''

if ____ and ____ and ____ :
  #logic here
  
''' in "and" will stop and EXIT on 1st FALSE '''

if ____ or ____ or ____ :
  #logic here
  
''' in "or" will stop on 1st TRUE and ENTER '''  

Loops : n instructions to be repeated in a fixed sequence till a condition is true
-for loop 
 for i in range (start, end, step)
  
 eg) for i in range (1,5,1)
        print(i)
   => 1,2,3,4
    
 eg) for i in range (1,5,1)
        print(i)   
     print("out of loop i" , i)
    
   => 1,2,3,4
      out of loop 4
