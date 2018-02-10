import numpy as np
arr1=np.fromstring(input("enter numbers"),dtype=float,sep=' ')
print(arr1[::-1])

arr2=np.fromstring(input("enter numbers"),dtype=float,sep=' ')
arr3=np.reshape(arr2,(3,3))

arr4=arr3.astype(int)
print(np.ndarray.transpose(arr4))
print(np.ndarray.flatten(arr4))

counts=[int(x) for x in input().split(' ')]
arr5=np.empty(((counts[0]+counts[1]),counts[2]),int)
for y in range(counts[0]+counts[1]):
	arr5[y]=np.fromstring(input('enter numbers'),dtype=int,sep=' ')
	
dim1=[int(x) for x in input().split(' ')]
print(np.zeros(dim))
print(np.ones(dim))

dim2=[int(x) for x in input().split(' ')]
np.eye(dim2[0],dim2[1])

arr6_1=np.random.random_sample((4,4))
arr6_2=np.random.random_sample((4,4))
print(np.add(arr6_1,arr6_2))
print(np.subtract(arr6_1,arr6_2))
print(np.dot(arr6_1,arr6_2))
print(np.divide(arr6_1,arr6_2))
print(np.mod(arr6_1,arr6_2))
print(np.power(arr6_1,arr6_2))

arr7=np.random.random_sample((7))
print(np.floor(arr7))
print(np.ceil(arr7))
print(np.rint(arr7))

print(np.mean(arr6_1,axis=1))
print(np.var(arr7,axis=0))
print(np.std(arr7,axis=0))
