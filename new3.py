num=[1,2,3,4,5,6,-1,-2,-3]
sum=0
product=1
n=[]

for i in num:
    
    if(i>0):
        if(i%2==0):
            sum=sum+i
        else:
            product=product*i
    else:
        n.append(i)
print("The sum of even no's is:",[sum])
print("The product of odd no's is:",[product])
print("The negative no's are:",n)