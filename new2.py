
#Q2 assume a list which has negative values .create an absolute list

# num=[-1,-2,-3,-4,-5]
# for i in num:
#     i=abs(i)
#     print([i])


#Q3 consider a list[apple,banana,orange,pear].return me the word from the list which has largest length


fruits=['apple','banana','pear']
max=0
longestWord=""
for i in fruits:
    if(len(i)>max):
        max=len(i)
        longestWord=i
print(max,longestWord)    

        

    


