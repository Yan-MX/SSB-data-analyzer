import urllib2
data=urllib2.urlopen("https://www.ssb.no/eksport/tabell.csv?key=372475")
q=data.read()
data.close()
print(len(q))
print(type(q))
m=q.split(";")
print(m)
l=m[1:7]
print(l)
k=m[23:27]
print(k)
c=m[7:11]
print(c)
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(9,9))
names=[c[0],k[0]]
value=[int(c[1]),int(k[1])]
position=[1,2]


plt.bar(position, value, width=0.3, color="g")
plt.title(l[0])
plt.xticks(position,names)
plt.show()