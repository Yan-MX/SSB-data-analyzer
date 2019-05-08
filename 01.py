import urllib2
data=urllib2.urlopen("https://www.ssb.no/eksport/tabell.csv?key=372475")
print data.read()



