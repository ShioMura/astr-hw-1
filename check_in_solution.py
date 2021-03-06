#include the Numpy Library
import numpy as np

#define the main() function
def main():

 i = 0 #declare i, initialize to 0
 x = 119.0 #declare a float x
 
 for i in range(120): #loop i from 0 to 119 inclusive 
  if((i%2)==0): #if i is even
   x +=3. #add 3 to x -- x = x+3
  else: #if i is odd
   x -=5. #subtract 5 from x
   
 s = "%3.2e" % x #makes a string s containing
                 #the value of x in sci notation
                 # with 2 decimal places showing
 print(s)        #print s to the screen

#now the rest of the program continues
#if the main() function exists, run it
if __name__ == "__main__":
   main()