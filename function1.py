def add(a,b):
     return a+b

def sub(a,b):
    return a-b

def product(a,b):
    return a*b

def division(a,b):
    return a/b

def returnOutput():
    value1=add(10,20)
    value2=sub(60,40)
    value3=product(10,10)
    value4=division(10,5)
    return value1,value2,value3,value4

result1,result2,result3,result4=returnOutput()
print(f"The addition of two numbers  {10,20} is:",result1)
print(f"The subtraction of two numbers  {60,40} is:",result2)
print(f"The product of two numbers  {10,10} is:",result3)
print(f"The division of two numbers  {10,5} is:",result4)
   


