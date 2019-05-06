f= open('C:\\Users\\caiyuanle\\Downloads\\tabell.csv','r+')
a = f.readlines()
t=a[0].split("\r")
q=[]
for i in t:
	o=i.split(";")
	try:
		k=int(o[1])
		q.append(k)
	except:
		continue
a=q[1:]
t1=t[2:]
del t1[1]
b=[]
for i in t1:
	o=i.split(";")
	b.append(o[0])
del b[-1]
print(a)
print(b)