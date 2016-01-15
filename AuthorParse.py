import urllib
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import plotly.plotly as py
import plotly.graph_objs as go

no = raw_input('Enter no of authors')
no = int(no)
count =0
data = list()

while count < no: 
    url = raw_input('Enter the URL:')
    html = urllib.urlopen(url).read()
    #soup = BeautifulSoup(html)
    stuff = ET.fromstring(html)
    lst = stuff.findall('r') 
    count1 = dict()
    lst1 = list()
    x = list()
    y = list()
    lst4 = list()
    for item in lst:
        
        lst1 = item[0].findall('author')
        yr = item[0].find('year')
        if float(yr.text) > 2005:
            for author in lst1:
                if author.text == "Amit Kumar 0001" or author.text == "Amit Kumar 0002" or author.text == "Amit Kumar 0003" or author.text == 'Amit Kumar 0004':
                    authorname = author.text
                    lst3 = list()
                    lst3 =  (author.text).split()
                    authorno = int(lst3[2])
                    count1[yr.text] = count1.get(yr.text,0) + 1

    for v, k in count1.items():
        lst4.append( (v,k) )
    
    lst4.sort()
    print lst4
    for item in lst4:
        x.append(item[0])
        y.append(item[1])

    trace = go.Bar(
            x=x,
            y=y,
            name = authorname
        )
    
    data.append(trace)
    count = count + 1
  
layout = go.Layout(
     barmode = 'group'     
 )
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')     