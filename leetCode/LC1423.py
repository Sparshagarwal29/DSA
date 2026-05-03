# Brute force approach
class Solution:
    def maxScore(self, cardPoints, k) :
        lSum = 0 
        mSum = 0 

        n = len(cardPoints)
        for i in range(k+1):
            rSum =0 
            for j in (range(k-i)):      
                rSum += cardPoints[n-(k-i)+j]
            mSum = max(mSum,  lSum + rSum )
            if i < k : 
                lSum += cardPoints[i] 
        return mSum
# better soln


        
            

