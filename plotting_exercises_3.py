# -*- coding: utf-8 -*-
"""plotting-exercises-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nxnQ-HfzQ1XsvYJpSULsJIxidiSd8iYX

# 📑 [Visualization Notes](https://visualization-notes.blogspot.com)
"""

# Commented out IPython magic to ensure Python compatibility.
# %run ../input/python-recipes/dhtml.py
# %run ../input/python-recipes/embedding_html_svg.py
# %run ../input/python-recipes/embedding_html_string.py
# %run ../input/python-recipes/embedding_html_page.py
dhtml('Additional Packages: Pygal')

!python3 -m pip install pygal --user --quiet
import os; os.listdir('../working/')

import warnings; warnings.filterwarnings('ignore')
from IPython.display import display,HTML
import pygal,pandas as pd
from pygal.style import BlueStyle
columns=['Fresh','Milk','Grocery','Frozen',
         'Detergents_Paper','Delicatessen']
colors=['#1b2c45','#5a8bbd','#008b8b','#ff5a8b']
index= ['C1','C2','C3']
data=[[26373,36423,22019,5154,4337,16523],
      [16165,4230,7595,201,4003,57],
      [14276,803,3045,485,100,518]]
samples=pd.DataFrame(data,columns=columns,index=index) 
line=pygal.Line(
    fill=False,height=330,
    style=BlueStyle(opacity='.3',colors=colors,
                    background='transparent'))
line.title='Samples of the Dataset "Wholesale Customers"'
line.x_labels=columns
line.add('C1',data[0]); line.add('C2',data[1])
line.add('C3',data[2]); line.add('MEAN',samples.mean())
file_name='samples.svg'
line.render_to_file(file_name)
width=650; height=350
embedding_html_svg(file_name,width,height)

dhtml('Interactive Outputs: D3, Highcharts, Plotly')

html_str='''
<script src='//d3js.org/d3.v3.min.js'></script>
<svg id='poly' style='background-color:silver;'></svg>
<script>
var mouse=[250,250],count=0;
var svg=d3.select('#poly')
          .attr('width',600).attr('height',600);
var g=svg.selectAll('g').data(d3.range(25)).enter()
         .append('g').attr('transform','translate('+mouse+')');
g.append('rect').attr('rx',5).attr('ry',5)
 .attr('x',-5).attr('y',-5)
 .attr('width',15).attr('height',15)
 .attr('transform',function(d,i){return 'scale('+(1-d/25)*15+')';})
 .style('fill',d3.scale.category20b());
g.datum(function(d){return {center:mouse.slice(),angle:0};});
svg.on('mousemove',function(){mouse=d3.mouse(this);});
d3.timer(function(){count++; 
g.attr('transform',
       function(d,i){d.center[0]+=(mouse[0]-d.center[0])/(i+1); 
d.center[1]+=(mouse[1]-d.center[1])/(i+1); 
d.angle+=Math.sin((count+i)/30)*7; 
return 'translate('+d.center+')rotate('+d.angle+')'});});
</script>'''
width=650; height=650
embedding_html_string(html_str,width,height,1)

html_str="""<script src='https://cdn.plot.ly/plotly-latest.min.js'>
</script>
<div id='test_plotly' style='width:600px;height:600px;'/>
<script>TEST=document.getElementById('test_plotly');
function f(t) {return Math.exp(Math.pow(Math.cos(0.001*t),2)+
                      Math.sin(0.001*t))-3*Math.cos(0.004*t);};
function arx(a) {return Array(6400).fill(1+0.1*a).map((r,t)=>
                        r*f(t)*Math.cos(0.001*t));};
function ary(a) {return Array(6400).fill(1+0.1*a).map((r,t)=>
                        r*f(t)*Math.sin(0.001*t));};
function col(a) {return 'rgb('+(1-0.05*a).toString()+',0,'+
                        (0.05*a).toString()+')';};
function plt(a) {return Plotly.plot(TEST,[{x:arx(a),y:ary(a),
                                           line:{color:col(a)},
                                           name:a.toString()}]);};
for (i=1; i<20; i++) {plt(i);}
</script>"""
width=650; height=650
embedding_html_string(html_str,width,height,2)

html_str='''<script src='https://code.highcharts.com/highcharts.js'></script>
<div id='highcharts' style='height:600px; width:600px; margin:0 auto'></div><script>
function getinteger(min,max) {return Math.floor(Math.random()*(max-min+1))+min;};
function fx(a,b,c,q,n,t,k) {
    var x1=Math.cos(Math.PI*t/n+k*Math.PI/q)+Math.cos(a*Math.PI*t/n+k*Math.PI/q);
    var x2=Math.cos(b*Math.PI*t/n+k*Math.PI/q)+Math.cos(c*Math.PI*t/n+k*Math.PI/q);
    return x1+x2};
function fy(a,b,c,q,n,t,k) {
    var y1=Math.sin(Math.PI*t/n+k*Math.PI/q)+Math.sin(a*Math.PI*t/n+k*Math.PI/q);
    var y2=Math.sin(b*Math.PI*t/n+k*Math.PI/q)+Math.sin(c*Math.PI*t/n+k*Math.PI/q);
    return y1+y2};
function ar(a,b,c,q,n,k) {return Array(2*n+1).fill(k).map((k,t)=>
                                 [fx(a,b,c,q,n,t,k),fy(a,b,c,q,n,t,k)]);};
function colrb(i) {var r=getinteger(i,255); var g=0; var b=getinteger(i,255);
    return 'rgb('+r.toString()+','+g.toString()+','+b.toString()+')';};   
var a=getinteger(5,9),b=getinteger(10,14),c=getinteger(15,19);
var q=getinteger(3,6),n=getinteger(4,24); var series=[];
for (var k=1; k<2*q+2; k++) {
    series.push({name:[k,a,b,c,n].toString(),marker:{symbol:"circle",radius:1},
                 color:colrb(k),lineWidth:0.5,data:ar(a,b,c,q,n,k)})};
Highcharts.chart('highcharts', {
    chart:{type:'line',backgroundColor:'ghostwhite'},
    xAxis:{title:{text:'x'}},yAxis:{title:{text:'y'}},
    title:{text:'Random Parametric Polygons'},credits:{enabled:false},
    legend:{enabled:false},series:series});
 </script>'''
width=650; height=650
embedding_html_string(html_str,width,height,3)

dhtml('Interactive Code Cells')

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <div id='smcell' style='border:10px double white; 
#      width:650px; height:1000px; overflow:auto; 
#      padding:10px; background-color:ghostwhite'>
# <iframe id='if1' 
# src='https://olgabelitskaya.gitlab.io/kaggle/kaggle_smc02.html' 
# width='600' height='950'/></div>