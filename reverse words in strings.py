#reverse a string using reversed()   
# Function to reverse a string   
def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
s = "the sky is blue"  
  
print ("The original string is : ",s)   
print ("The reversed string using reversed() is : ",reverse(s) )  
