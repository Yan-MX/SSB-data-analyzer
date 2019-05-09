import urllib2
data=urllib2.urlopen("https://www.ssb.no/eksport/tabell.csv?key=383572")
a=data.read()
data.close()
a1=a.split("\r")
a1=a1[2:]
a1=a1[:-1]
print(a1[:4])
#dic={}
l1=[]
l2=[]
for i in a1:
    m=i.split(';')
    m=m[2:-1]
    m=m[::-1]
    #print(m)

    for i in m:
        l1.append(i)

    #l1.append(m[0])
    #l2.append(m[1])

#print(l1)
for i in range(0,len(l1)-1):
    c=float(l1[i])-float(l1[i+1])
    c1=c/float(l1[i+1])
    l2.append(c1)
w=l2.index(max(l2))
print(max(l2))
print(sum(l2)/len(l2))

print(w)
w1=w//12
w2=w%12
year=2018-w1
print(year)
month=12-w2
print("in the year of "+str(year)+ " and in the "+str(month)+"th month")
