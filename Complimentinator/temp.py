a=[1,2,3,4,5,6,7,8]
k=4
a[0:len(a)-k],a[k:]=a[k:len(a):-1],a[0:len(a)-k]
print(a)