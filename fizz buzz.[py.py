class Solution:
    def fizzBuzz(self, n: int) -> Li[str]:
        
        final_li = []
        for i in range(1, n+1):
            
            if i%15 == 0:
                final_li.append("FizzBuzz")
            elif i%5 == 0:
                final_li.append("Buzz")   
            elif i%3 == 0:
                final_li.append("Fizz")
            else:
                final_li.append(str(i))
                
        return final_li
