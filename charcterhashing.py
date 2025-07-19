s = "azssihghhzzzzzzaio"
q = ["a","s","h","z"]
def charcterhash(s ,q):
    hash_list =[0]*26
    for ch in s:
        ascii_val =ord(ch)
        index = ascii_val - 97
        hash_list[index] +=1
    for ch in q:
        ascii_val_q= ord(ch)
        index_q = ascii_val_q - 97
        print(hash_list[index_q])
    return hash_list    

# 
 
print(charcterhash(s,q)) 