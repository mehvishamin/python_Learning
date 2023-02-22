num=4
i=2
isPrime=True

while i<=num/2:
    if(num%i==0):
        isPrime=False    
        break
    i=i+1   
if(isPrime==True):
    print("number is Prime")          
else:
    print("number is not prime")            
