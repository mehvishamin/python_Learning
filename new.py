
# Q1 given two lists num1[1,2,3,4,5] and num2[5,6,7,8] create a new list called result which vll have similar elements present in these two

num1=[1,2,3,4,5]
num2=[4,4,5,6,7,8]
num1.extend(num2)
num1.sort()
max=num1[0]
count=0
for i in range(1,len(num1)):
    if(num1[i]>max):
        max=num1[i]
        count=0
    elif(num1[i]==max):
       if(count==0):   
          count=count+1
          print(num1[i])

# for i in range(1,len(num1)):
#     if(num1[i-1]==num1[i]):
#         print(num1[i])



# for i in num1:
#     for j in num2:    
#       if(i==j):
#          print("result:",[i])


