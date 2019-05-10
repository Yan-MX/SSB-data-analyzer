import urllib2
import json
import pyjstat
import pandas as pd
import matplotlib.pyplot as plt

from pyjstat import pyjstat
import requests

POST_URL = 'https://data.ssb.no/api/v0/en/table/06313'

#API query
payload = {
  "query": [
    {
      "code": "Innvandringsgrunn",
      "selection": {
        "filter": "item",
        "values": [
          "00",
          "01",
          "02",
          "05",
          "06"
        ]
      }
    },
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": [
          "0",
          "1",
          "2"
        ]
      }
    },
    {
      "code": "Alder",
      "selection": {
        "filter": "item",
        "values": [
          "00-17",
          "18-29",
          "30-59",
          "80+",
          "UOPP"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Personer"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "1990-2011",
          "1990-2012",
          "1990-2013",
          "1990-2016",
          "1990-2017"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

resultat = requests.post(POST_URL, json = payload)
#print(resultat)

dataset = pyjstat.Dataset.read(resultat.text)
df = dataset.write('dataframe')
df.columns = [c.replace(' ', '_') for c in df.columns]
#df.head()
#df.info()
#print(df[10:12])
#print(len(df))
#print(type(df.value))
#print(df[100:120])

a1=df[(df.reason_for_immigration  =="Education")& (df.sex=="Males" )]
a2=a1[a1.age=="18-29 years"]
a2.head()
a2.info()


#a2['value'] = a2['value'].astype(float)
#print(type(a2["value"]))
w=[i for i in range(5)]
print(a2)
#a2.plot.bar(x="interval_(year)",y="value",rot=0)
#plt.show()