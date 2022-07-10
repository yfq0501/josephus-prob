m=int(input("input the amount:"))
n=int(input("input the number:"))


list1=[]

for i in range(0,m,1):
    list1.append(i)

print("大家的编号为：%s"%list1)

i=0
flag=1
while len(list1)>=n:
    if i==len(list1):
        i=0
    if flag==n :
        list1.pop(i)
        flag=1
        print("目前存活的数为：%s"%list1)
        continue  
    
        
    else:
        flag+=1
         
    i+=1