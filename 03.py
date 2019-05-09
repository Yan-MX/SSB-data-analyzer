import urllib2
data=urllib2.urlopen("https://www.ssb.no/eksport/tabell.csv?key=383572")
a=data.read()
data.close()
a1=a.split("\r")
a1=a1[2:]
a1=a1[:-1]
#print(a1[:4])
#dic={}
l1=[]
l2=[]
for i in a1:
    m=i.split(';')
    l1.append(m[0])
    l2.append(m[1])
    #print(len(m))
    #dic[m[0]]=float(m[1])
#print(dic)
#print(l1[:5])
print(len(l2))
slope=[]

import matplotlib.pyplot as plt

l3 = [i for i in range(93)]
print(l3)
x = l3
y = l2
plt.plot(x, y)
plt.xticks(x[0::10],l1[0::10])
plt.title("CPI change of year 2018-1926 in Norway")

for i in range(len(l2)-1):
    slope.append(float(l2[i]) - float(l2[i + 1]))
print(slope.index(max(slope)))
print("In the year of "+l1[31]+" CPI increased the most")

plt.show()


