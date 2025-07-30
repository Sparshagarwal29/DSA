# divisiblisty by 13
# using digit by digit method 
# rem = (rem*10 +digit)%13
def divisible_by_13(s):
   rem = 0 
   for ch in s :
        rem =(rem *10 + int(ch)) % 13
  
   return rem == 0 
     


if __name__ == "__main__":
    s = "2911285"
    
    if divisible_by_13(s):
        print("true")
    else:
        print("false")

