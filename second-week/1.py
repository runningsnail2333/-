
import os
import numpy as np


a = open("zhuanzhi.txt","r")

#print(a)
b =[]
for line in a.readlines():
    b.append(line.strip().split("\t"))

#print(b)

c = np.array(b)

#print(c)

d = c.T

print(d) #����numpy��ת�ƺ���


print (map(list,zip(*b))) #������zip����


listb=[[r[col] for r in b] for col in range(len(b[0]))]

print(listb) #����forѭ��
