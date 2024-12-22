
l = [14,78,90,21,2,3]
print("The original list is", l)

count=0
for i in l:
    count += i 

avg = count/len(l)

print("sum = ", count)
print("average = ", avg)

l.sort()

print("smallest element is:", l[0])
print("Largest element is:",[-1])
