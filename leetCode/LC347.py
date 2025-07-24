def k_feq(num):
    hashmap ={}
    for i in num:
            hashmap[i] = hashmap.get(i,0) +1
    return hashmap.values()


print(k_feq(num=[1,1,2,2,2,3,3,3,3]))