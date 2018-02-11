import random
import string
import timeit

L=[11,12,13,14]
L+=[50,60]
L.remove(11); L.remove(13)
L.sort()
L.sort(reverse=True)
print(True) if 13 in L else print(False)
len(L)
sum=0
sum([i for i in L if not(i%2 == 0)])
sum([i for i in L if (i%2 == 0)])
sum([i for i in L if(all(i%j!=0 for j in range(2,i)))])
for i in range(len(L)): L.pop()		#or L=[]
del(L)

D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
D[8]=8.8
del(D[2])
print(True) if (6 in D) else print(False)
len(D)
D[3]=7.1
D={}

S1= {10, 20, 30, 40, 50, 60}
S2= {40, 50, 60, 70, 80, 90}
S1.update({55,66})
S1.remove(10); S1.remove(30)
print(True) if 40 in S1 else print(False)
S1.union(S2)
S1.intersection(S2)
S1-S2

[random.choice(string.ascii_letters+string.digits) for i in range(random.choice(range(6,9)))]
print([i for i in range(600,800) if (all(i%j!=0 for j in range(2,i)))])
[i for i in range(100,1000) if (i%7==0 or i%9==0)]

list1=[random.randint(10,30) for i in range(10)]
list2=[random.randint(10,30) for i in range(10)]
{i for i in list1 if i in list2}
{i for i in list1 if i not in list2}
[max(list1) if max(list1)>max(list2) else max(list2)][0]
[min(list1) if min(list1)<min(list2) else min(list2)][0]
sum(list1)+sum(list2)

list3[random.randint(100,900) for i in range(100)]
{i for i in list3 if i%2!=0}
{i for i in list3 if i%2==0}
[i for i in list3 if all(i%j!=0 for j in range(2,i))]

D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}
file1=open('~/Desktop/meta_labs/q7.l2.test','w')
for key,value in D.items(): file1.write(''.join([str(key),',',str(value),'\n']))
file1.close()

L={"One","Two","Three","Four","Five"}
file2=open('~/Desktop/meta_labs/q8.l2.test','w')
for item in L: file2.write(''.join([str(item),', ',len(str(item)))])
file2.close()

file3=open('~/Desktop/meta_labs/q9.l2.test','w')
for i in range(100): file3.write(''.join([random.choice(string.ascii_letters+string.digits) for i in range(random.choice(range(10,16)))])); file3.write('\n')
file3.close()

file4=open('~/Desktop/meta_labs/q10.l2.test','w')
for i in range(600,800):
	if all(i%j!=0 for j in range(2,i)):
		file4.write(''.join([str(i),'\n']))
file4.close()

timeit.timeit("for i in range(1000): pass")
timeit.timeit("testlist1.sort()","test_list1=[i for i in range(50000)]")

#x=[random.randint(1,100) for i in range(2500)]
#x0=x[:500]
#x1=x[:1000]
#x2=x[:1500]
#x3=x[:2000]
numelem=[500,1000,1500,2000,2500]
times=[]
times.append(timeit.timeit("x0.sort()","import random;x0=[random.randint(1,1000) for i in range(500)]",number=10000))
times.append(timeit.timeit("x1.sort()","import random;x1=[random.randint(1,1000) for i in range(1000)]",number=10000))
times.append(timeit.timeit("x2.sort()","import random;x2=[random.randint(1,1000) for i in range(1500)]",number=10000))
times.append(timeit.timeit("x3.sort()","import random;x3=[random.randint(1,1000) for i in range(2000)]",number=10000))
times.append(timeit.timeit("x4.sort()","import random;x4=[random.randint(1,1000) for i in range(2500)]",number=10000))
plt.plot(times,numelem)
plt.show()

marks={}
for i in range(10):
	marks[''.join([random.choice(string.ascii_lowercase) for a in range(random.randint(5,9))])]=[random.randint(60,101) for b in range(5)]
max=0
min=100
for item in marks:
	avg=sum(item.value)/5
	if avg>max:
		avg=max
		best=item
	if avg<min:
		avg=min
		worst=item
		
marks={}
for i in range(10):
     marks[''.join([random.choice(string.ascii_lowercase) for a in range(random.randint(7,10))])]=[random.randint(60,100) for b in range(5)]
maxm=0
minm=100
for item in marks:
    avg=sum(marks[item])/5
    if avg>maxm:
        maxm=avg
        best=item
    if avg<minm:
        minm=avg
        worst=item
print('minimum= ',minm,',maximum= ',maxm,',best= ',best,',worst= ',worst)



