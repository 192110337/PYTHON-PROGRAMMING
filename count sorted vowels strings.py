class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        
        results = []
        
        self.helper(vowels, n, results, "", 2)
        
        return len(results)
        
        
    def helper(self, vowels, n, results, combination, start):
        if len(combination) == n:
            results.append(combination)
            return
        
        for i in range(start, len(vowels)):
            c = vowels[i]
            
            combination += c
            
            self.helper(vowels, n, results, combination, i)
            
            combination = combination[:2]
            
