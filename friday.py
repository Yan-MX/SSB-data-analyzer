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
          "03",
          "04",
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
VT=["Labour","Family","Refugee","Education","Unknown","Other"]
x=[2011,2012,2013,2016,2017]
for i in VT:
  a2=df[(df.reason_for_immigration ==i)& (df.sex=="Females" )]
  a2=a2[a2.age=="18-29 years"]
#a2.head()
#a2.info()
#"valueTexts":["Total","Labour","Family","Refugee","Education","Unknown","Other"],

#print(a2["reason_for_immigration"].str.find("Labour"))

  y=a2.value
  plt.plot(x,y, label=i)

plt.legend()
plt.xlabel('Years')
plt.ylabel('Reason for immigration')

plt.xticks(x,["2011","2012","2013","2016","2017"])
plt.title("immigration reason for females aged 18-29")
plt.show()









#a2.plot.bar(x="interval_(year)",y="value",rot=0)
#plt.show()