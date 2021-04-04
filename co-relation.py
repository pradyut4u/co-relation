import plotly.express as pe
import csv
import numpy as np

def getdata(path):
    icecremsales=[]
    colddrinksales=[]
    temperature=[]
    with open(path)as f:
        reader=csv.DictReader(f)
        for row in reader:
            print(row)
            temperature.append(float(row["ï»¿Temp"]))
            icecremsales.append(float(row["Ice-cream"]))
            colddrinksales.append(float(row["Cold drink"]))
#    return {"x":temperature,"y":icecremsales,"z":colddrinksales}
    return {"x":colddrinksales,"y":icecremsales}

def findcorelation(data):
    corelation=np.corrcoef(data["x"],data["y"])
#    corelation1=np.corrcoef(data["x"],data["z"])
 #   corelation2=np.corrcoef(data["y"],data["z"])
    print(corelation[0,1])
  #  print(corelation1)
   # print(corelation2)

def setup():
    path="co-relation.csv"
    data=getdata(path)
    findcorelation(data)

setup()