# class Soln:
#     def fact(self,n):
#         res =1 
#         for i in range(1,n+1):
#             res = i*res
#         return res    

#     def vow(self,s):
#         freq={}
#         vowels ="aeiou"
#         for ch in s:
#             if ch in vowels:
#                 freq[ch] = freq.get(ch,0)+1
#         if not freq:
#             return 0                    
#         choices =1

#         for count in freq.values():
#             choices *= count
#         dis = len(freq)    

#         res = choices * self.fact(dis)
#         return res
        

class Solution:
    
    def vowelCount(self, s):
        #code here
        def factorial(n):
            res = 1
            for i in range (1,n+1):
                res = i * res
            return res 
            
        frequency = {}
        vowel = "aeiou"
        for ch in s:
            if ch in vowel:
                frequency[ch] = frequency.get(ch,0)+1
        if not frequency:
             return 0
        choice = 1
        for count in frequency.values():
            choice *= count
        dis = int(len(frequency))
        
        res = choice * factorial(dis)
        
        return res 
            
            
Solution = Solution()
s  = input("enter the string: ")
result = Solution.vowelCount(s)
print(result)