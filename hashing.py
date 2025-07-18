# def hashing(n , m ):
#     hash_list = [0] *11
#     for num in n: 
#         hash_list[num] +=1
#     for num in m:
#         if num < 1 or num > 10:
#             print("does not exit")    
#         else:
#             print( hash_list[num])
#     return hash_list        
def hashing(n,m):
    hash_map ={}
    for num in n:
        hash_map[num] = hash_map.get(num,0) +1
    for num in m:
         if num < 1 or num > 10:
            print(f"{num}--does not exit in the Dictionary") 
         else:
              print(f"count of {num} : {hash_map.get(num,0)}")
    return hash_map


num =[5,3,2,2,1,5,5,7,10,6,1,1,1,1,1]
n = sorted(num)
m =[10,111,9,1,9,5,67,2,]
print(hashing(n,m))


