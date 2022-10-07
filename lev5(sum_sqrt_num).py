#The average of n integer numbers from n1 to n2
import math
n1= 1
n2=100
sum=0
N=0
for i in range(n1,n2+1):
    
    sum=sum+math.sqrt(i)
    print(sum)
#print('sum=',sum)
average=sum/(n2-n1+1)
print(average)
