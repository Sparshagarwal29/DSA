def mergeAlternately(word1: str, word2: str):
        x = len(word1) -1
        y = len(word2) -1
        while x !=0 or y !=0:
            for i in word1:
                for j in word2:
                    print(i+j)
            x -=1
            y -=1                    

print(mergeAlternately(word1="ab",word2="pqrs"))