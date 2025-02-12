# -*- coding: utf-8 -*-
"""pandas-practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/164bhiVt_yHLXN190exBbmil4YSLJZGEc
"""

import json,pandas as pd,pylab as pl,numpy as np

# Commented out IPython magic to ensure Python compatibility.
# %run ../input/python-recipes/dhtml.py
dhtml('Plotting Style - "a Couple of Code Rows"')

colors=['#3636ff','#ff3636','#36ff36',
        '#ff36ff','#ffff36','#36ffff']
user='https://raw.githubusercontent.com/OlgaBelitskaya/'
path='machine_learning_engineer_nd009/'+\
     'master/Machine_Learning_Engineer_ND_P3/'
data=pd.read_csv(user+path+'customers.csv')

fig=pl.figure(figsize=(10,8))
ax1=fig.add_subplot('211')
params={'frame':data,'class_column':'Channel',
        'lw':.5,'color':colors}
pd.plotting.andrews_curves(**params,ax=ax1)
ax2=fig.add_subplot('212')
pd.plotting.parallel_coordinates(**params,ax=ax2);

pl.figure(figsize=(10,8))
pd.plotting.radviz(**params,s=3)
pl.xticks([]); pl.yticks([]);

data[data<5000].drop('Region',axis=1)\
.boxplot(by='Channel',figsize=(10,10),
         boxprops={'color':colors[0]},
         flierprops={'markerfacecolor':colors[1]});

data[data<10000].plot.hexbin(
    x='Fresh',y='Milk',C='Grocery',
    reduce_C_function=np.mean,gridsize=20,
    cmap='Spectral',figsize=(10,4))
pl.show()

fig=pl.figure(figsize=(10,4))
ax=fig.add_subplot('111')
data.iloc[:,int(2):].plot.area(
    stacked=False,ax=ax,cmap='Spectral')
data_mean=pd.DataFrame(
    data.iloc[:,int(2):].mean().round()).T
data_mean.index=['mean']
pd.plotting.table(ax,data_mean,loc='top')
pl.grid();

data.drop('Region',axis=1).groupby('Channel').sum().T\
.plot.pie(subplots=True,figsize=(10,4),
          legend=False,cmap='bwr');

data_range=data.iloc[:,2:][(data<5000)&(data>1000)]
params={'bins':80,'alpha':.5,
        'figsize':(10,4),'color':colors}
data_range.iloc[:,:3].plot.hist(**params)
data_range.iloc[:,3:].plot.hist(**params);

dhtml('Data Transformation')

import json,pandas as pd,pylab as pl
url='https://www.ecb.europa.eu/stats/policy_and_exchange_rates/'+\
    'euro_reference_exchange_rates/html/index.en.html'
exchange_rates=pd.read_html(url)[0]\
.drop('Chart',axis=1)
exchange_rates.to_hdf('exchange_rates.h5',key='spot',mode='w')
pd.read_hdf('exchange_rates.h5','spot').head(7).T

exchange_rates[exchange_rates['Spot']<200]\
.set_index('Currency').plot.bar(
    figsize=(10,4),color=colors[0]);

exchange_rates_json=\
exchange_rates.to_json(orient='table')
exchange_rates_string=\
json.loads(exchange_rates_json)
n=json.dumps(exchange_rates_string).find('data')
n=json.dumps(exchange_rates_string).find('data')
for el in json.dumps(exchange_rates_string)[n+7:-1]\
.replace('[{','').replace('}]','').split('}, {'):
    print(el)

dhtml('R DataFrames in Python Notebooks')

# Commented out IPython magic to ensure Python compatibility.
# %run ../input/python-recipes/sage_call.py

# Commented out IPython magic to ensure Python compatibility.
# %sage_autorun \
# %%r \
# library('MASS'); data(Boston); n<-dim(Boston)[1] \
# svg(filename='Rplots.svg',width=8,height=6,pointsize=12, \
#     onefile=T,family='courier',bg='whitesmoke', \
#     antialias=c('default','none','gray','subpixel')) \
# plot(Boston[,'lstat'],col='#3636ff',type='o',pch=13,cex=.6) \
# grid(); dev.off()

# Commented out IPython magic to ensure Python compatibility.
# %sage_autorun \
# %%r \
# svg(filename='Rplots.svg',width=8,height=6,pointsize=12, \
#     onefile=T,family='courier',bg='ghostwhite', \
#     antialias=c('default','none','gray','subpixel')) \
# user<-'https://raw.githubusercontent.com/OlgaBelitskaya/' \
# file<-paste0(user,'machine_learning_engineer_nd009/') \
# file<-paste0(file,'master/Machine_Learning_Engineer_ND_P3/') \
# file<-paste0(file,'customers.csv') \
# customers<-read.csv(file) \
# matplot(c(1:440),customers[,c(3,4,5,6,7,8)],type='l') \
# legend('topright',colnames(customers[,c(3,4,5,6,7,8)]), \
#        col=seq_len(6),pch=13,cex=.8) \
# grid(); dev.off()

dhtml('Danfo DataFrames')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile danfo_csv.py
# from IPython.core.display import display,HTML
# 
# def danfo_table_csv(url,columns,header_font_size):
#     html_str="""<html><head><meta charset='UTF-8'>"""+\
#     """<meta name='viewport' """+\
#     """content='width=device-width,initial-scale=1.0'>"""+\
#     """<script src='https://cdn.jsdelivr.net/npm/"""+\
#     """danfojs@0.1.1/dist/index.min.js'></script></head>"""+\
#     """<div><p>&nbsp; CSV =>>> Danfo DataFrames</p>"""+\
#     """<div id='div015_1'></div><script>"""+\
#     """var url='"""+url+"""'; """+\
#     """dfd.read_csv(url)"""+\
#     """   .then(df=>{df.loc({columns:"""+str(columns)+\
#     """}).plot('div015_1').table({header_style:"""+\
#     """{font:{size:"""+str(header_font_size)+"""}}})})"""+\
#     """   .catch(err=>{console.log(err);})"""+\
#     """</script></div></html>"""
#     display(HTML(html_str))
#     
# def danfo_chart_csv(url,columns,line_width,title):
#     html_str="""<html><head><meta charset='UTF-8'>"""+\
#     """<meta name='viewport' """+\
#     """content='width=device-width,initial-scale=1.0'>"""+\
#     """<script src='https://cdn.jsdelivr.net/npm/"""+\
#     """danfojs@0.1.1/dist/index.min.js'> </script></head>"""+\
#     """<body><p>&nbsp; CSV =>>> Danfo DataFrames</p>"""+\
#     """<div id='div015_2'></div><script>"""+\
#     """var url='"""+url+"""'; """+\
#     """dfd.read_csv(url).then(df=>{var layout={"""+\
#     """  title:'"""+title+\
#     """',xaxis:{title:'columns'},"""+\
#     """  yaxis:{title:'value'}}; """+\
#     """  df.plot('div015_2').line({"""+\
#     """line:{width:"""+str(line_width)+"""},"""+\
#     """columns:"""+str(columns)+""",layout:layout})})"""+\
#     """   .catch(err=>{console.log(err);})"""+\
#     """</script></body></html>"""
#     display(HTML(html_str))

# Commented out IPython magic to ensure Python compatibility.
# %run danfo_csv.py
url='https://raw.githubusercontent.com/OlgaBelitskaya/'+\
    'machine_learning_engineer_nd009/master/'+\
    'Machine_Learning_Engineer_ND_P3/customers.csv'
columns=['Fresh','Milk','Grocery','Frozen',
         'Detergents_Paper','Delicatessen']
danfo_table_csv(url,columns,10)

danfo_chart_csv(url,columns,1,'Customers')

from IPython.display import IFrame
IFrame(src='https://olgabelitskaya.github.io/'+\
       'instagram15.html',
       width=680,height=670)