# -*- coding: utf-8 -*-
"""styling-recipes-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mQ4qDJPlhFjo6OeHC-0FFnP5OQxVWDeo

[📑 My Observable Exercises](https://observablehq.com/@olgabelitskaya?tab=notebooks)
"""

# Commented out IPython magic to ensure Python compatibility.
# %run ../input/python-recipes/dhtml.py
dhtml('Code Modules & Element Classes','#ff36ff',f2,fs8)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile cidhtml.py
# from IPython.display import display,HTML
# import random
# 
# f1,f2,f3,f4,f5,f6,f7,f8,f9=\
# 'Smokum','Akronim','Wallpoet','Orbitron','Ewert',\
# 'Lobster','Roboto','Miss Fajardose','Monoton'
# fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11=\
# 10,12,14,16,18,20,22,24,26,28,30
# 
# def chtml(string,font_family=f2,font_size=fs9,font_color='#ff36ff'):
#     css_str="""<style>@import """+\
#     """'https://fonts.googleapis.com/css?family="""+font_family+"""'; 
#     .ch1 {color:"""+font_color+"""; font-family:"""+font_family+"""; 
#     font-size:"""+str(font_size)+"""px;}</style>"""
#     h1_str="""<h1 class='ch1'>"""+string+"""</h1>"""
#     display(HTML(css_str+h1_str))
#     
# def idhtml(string,font_family=f5,
#            font_size=fs5,font_color='darkslategray'):
#     randi=random.randint(1,999999999)
#     css_str="""<style>@import """+\
#     """'https://fonts.googleapis.com/css?family="""+font_family+"""'; 
#     #ch1_"""+str(randi)+""" {font-family:"""+font_family+"""; 
#     color:"""+font_color+"""; font-size:"""+str(font_size)+"""px;}</style>"""
#     h1_str="""<h1 id='ch1_"""+str(randi)+"""'>"""+string+"""</h1>"""
#     scr_str="""<script>
#     var idc=setInterval(function() {
#         var iddoc=document.getElementById('ch1_"""+str(randi)+"""'), 
#             sec=Math.floor(new Date().getTime()%60000/1000); 
#         var col='rgb('+(5+Math.abs(245-8*sec))+',0,'+
#                 (250-Math.abs(245-8*sec))+')';  
#         iddoc.style.color=col;}, 1000);</script>"""
#     display(HTML(css_str+h1_str+scr_str))
#     
# def whtml(string,background_color='black',padding=2,
#           font_family='Akronim',font_size_px=int(28),
#           deg=int(120),percent=[0,33,67,100],
#           colors=['magenta','orange','cyan','purple']):
#     randi=str(random.randint(1,999999999))
#     css_str="""<style>@import 'https://fonts.googleapis.com/"""+\
#     """css?family="""+font_family+"""';</style>"""
#     html_str="""<div id='col_div"""+str(randi)+"""' 
#     style='background:"""+background_color+"""; width:100%; 
#     padding:"""+str(padding)+"""vw;'>
#     <div style='background:linear-gradient("""+str(deg)+"""deg, 
#     """+colors[0]+""" """+str(percent[0])+"""%,
#     """+colors[1]+""" """+str(percent[1])+"""%,
#     """+colors[2]+""" """+str(percent[2])+"""%,
#     """+colors[3]+""" """+str(percent[3])+"""%); 
#     font-family:"""+font_family+"""; font-size:"""+str(font_size_px)+"""px; 
#     -webkit-background-clip:text; color:transparent;'>"""+string+"""
#     </div></div>"""
#     display(HTML(css_str+html_str))

dhtml('Colorized Code Outputs','#ff36ff',f2,fs8)

# Commented out IPython magic to ensure Python compatibility.
# %run cidhtml.py
#looks fine in the working space
chtml('Style Applying to Classes of Elements')
#looks fine in the working space and after the notebook execution
idhtml('Style Applying to Id of Elements')

corpus=['Have you already set your goals for the New Year?', 
        'Do you want to lose ten kilos, '+\
        'run a marathon or speak fluent English?', 
        'Some experts believe that you need systems, not goals.', 
        'A system is something you do on a regular basis. ',
        'This means focusing on what you can control '+\
        '(your actions) rather than what you can’t.',
        'For example, do not focus on losing ten kilos.',
        'Focus on shopping for healthy food and '+\
        'cooking something light every day.',
        'Do not focus on the marathon.',
        'Focus on the training schedule.',
        'Invent a system to improve your English, one step at a time.',
        'Good luck!']
corpus_str=' '.join(corpus)

#cool, isn't it?
whtml(corpus_str)

dhtml('Animated Markdown Cells','#ff36ff',f2,fs8)

# Commented out IPython magic to ensure Python compatibility.
# %%javascript
# var t=setInterval(function() {
#   var doc=document.getElementById('simple_timer');
#   var now=new Date().getTime();
#   var sec=Math.floor(now%60000/1000);
#   doc.innerHTML='🕒 '+sec;
#   doc.style.color='rgb('+4*(sec+1)+',0,'+4*(sec+1)+')'},1000);
# var tc=setInterval(function() {
#   var doc=document.getElementById('color_timer');
#   var now=new Date().getTime();
#   var sec=Math.floor(now%60000/1000);
#   var col='rgb(0,'+(5+Math.abs(245-8*sec))+','+
#           (250-Math.abs(245-8*sec))+')';
#   doc.style.color=col},1);
# var countDownDate=new Date('Jan 1, 2022 00:00:00').getTime();
# var cdd=setInterval(function() {
#   var doc=document.getElementById('new_year_countdown');
#   var now=new Date().getTime();
#   var distance=countDownDate-now;
#   var days=Math.floor(distance/(1000*60*60*24)),
#       hours=Math.floor(distance%(1000*60*60*24)/(1000*60*60)),
#       minutes=Math.floor(distance%(1000*60*60)/(1000*60)),
#       seconds=Math.floor(distance%(1000*60)/1000);
#   doc.innerHTML=days+' days '+hours+' hours '+minutes+
#                 ' minutes '+seconds+' seconds';
#   if (distance<0) {
#     clearInterval(x); doc.innerHTML='Happy New Year!';}},3000);

"""<p id='color_timer'>This Markdown element has id='color_timer'.</p>

🕒 <<<<< Simple Timer >>>>> 🕒 <p id='simple_timer'></p>

🕒 <<<<< New Year Countdown >>>>> 🕒 <p id='new_year_countdown'></p>
"""

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <style>
# @import url('https://fonts.googleapis.com/css?family=Ewert');
# .animated {
#     background-color:silver; font-family:'Ewert'; 
#     color:#ff36ff; text-align:center; font-size:20px; 
#     border-radius:15px; padding:10px; width:350px; 
#     transition:all 0.8s; cursor:pointer; margin:2px;}
# .animated span {
#     cursor:pointer; display:inline-block; 
#     position: relative; transition:0.8s;}
# .animated span:after {
#     content:'\22d9'; position:absolute; 
#     opacity:0; top:0; right:-10px; transition:0.8s;}
# .animated:hover span {padding-right:15px;}
# .animated:hover span:after {opacity:1; mright:0;}
# </style>

"""<button class='animated'><span>Animated Button</span></button>"""

dhtml('Animated Code Outputs','#ff36ff',f2,fs8)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile example000.html
# <script src='https://d3js.org/d3.v6.min.js'></script>
# <style>
# @import 'https://fonts.googleapis.com/css?family=Ewert';
# .gewert {font-family:Ewert; color:white; text-align:center; width:99%;}
# </style>
# <h3 id='colorized1' class='gewert'>Color Interpolation in Text Displaying</h3>
# <h3 id='colorized2' class='gewert'>Background Interpolation in Text Displaying</h3>
# <script>
# var tc=setInterval(function() {
#     var now=new Date().getTime();
#     var iddoc1=document.getElementById('colorized1');
#     var iddoc2=document.getElementById('colorized2');
#     iddoc1.style.color=d3.interpolateSinebow(now/1000);
#     iddoc2.style.background=d3.interpolateRainbow(now/60000);},1)
# </script>

from IPython.display import IFrame
IFrame(src='example000.html',width=650,height=100)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile example001.html
# <script src='https://d3js.org/d3.v6.min.js'></script>
# run <button style='background:silver; width:200px; height:25px'
# onclick='draw_circles();' id='interpolate_button'>
# =>>></button><br/><br/>
# <svg id='svg016'></svg>
# <script>
# function draw_circles() {
# var cols={1:'silver',2:'#ff36ff'};
# var svg=d3.select('#svg016')
#           .attr('width',300).attr('height',300);
# svg.selectAll('circle').remove();
# svg.selectAll('text').remove();
# for (var i=1; i<7; i++) {
#     svg.append('circle').attr('id','c'+i)
#       .attr('transform','translate(150,150)')
#       .attr('cx',0).attr('cy',0).attr('r',140-i*20)
#       .attr('stroke','silver').attr('stroke-width',3)
#       .attr('fill-opacity',.1*i)
#       .transition().duration(10000)
#       .styleTween('fill',function() {
#           return d3.interpolateHsl(cols[1],cols[2]);});
#     svg.append('text').text('COLOR INTERPOLATION')
#        .attr('transform','translate(30,20)')
#        .attr('x',0).attr('y',0).attr('fill','siver')
#        .transition().duration(10000)
#        .styleTween('fill',function() {
#           return d3.interpolateHsl(cols[2],cols[1]);});
# };};</script>

from IPython.display import IFrame
IFrame(src='example001.html',width=350,height=370)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile example002.html
# <script src='https://d3js.org/d3.v6.min.js'></script>
# number <select id='num_points' 
# style='text-align:center; text-align-last:center; 
#   background:silver; width:200px; height:25px'>
#     <option value='100'>100</option><option value='150'>150</option>
#     <option value='200'>200</option><option value='250'>250</option>
#     <option value='300'>300</option><option value='350'>350</option>
# </select><br/><br/>run &nbsp; &nbsp; &nbsp; &nbsp;
# <button style='background:silver; width:200px; height:25px'
# onclick='draw_chart();' id='run_button'>=>>></button><br/><br/>
# <svg id='svg015' style='background-color:silver;'></svg><script>
# margin={top:20,right:20,bottom:20,left:60},width=600,height=250;
# reveal=path=>
# path.transition().duration(10000).ease(d3.easeLinear)
#     .attrTween('stroke-dasharray',function() {
#       const length=this.getTotalLength();
#       return d3.interpolate(`0,${length}`,`${length},${length}`);});
# function draw_chart() {
#   var n=parseInt(document.getElementById('num_points').value);
#   var x=d3.scaleLinear().domain([0,n-1])
#           .range([margin.left,width-margin.right]),
#       y=d3.scaleLinear().domain([0,n])
#           .range([height-margin.bottom,margin.top]); 
#   var line=d3.line().curve(d3.curveMonotoneX)
#            .x(function(d,i) {return x(i);})
#            .y(function(d) {return y(d.y);});
#   var data=d3.range(n).map(function(d) {
#       return {'y':d3.randomUniform(n)()}; })
#   var xAxis=(g,scale=x)=>g
#       .attr('transform',`translate(0,${height-margin.bottom})`)
#       .call(d3.axisBottom(scale)
#               .ticks(width/60).tickSizeOuter(0)),
#       yAxis=(g,scale=y)=>g
#       .attr('transform',`translate(${margin.left},0)`)
#       .call(d3.axisLeft(scale).ticks(height/40));
#   var svg=d3.select('#svg015')
#             .attr('width',width).attr('height',height);
#   svg.selectAll('g').remove(); svg.selectAll('path').remove();
#   svg.append('g').call(xAxis); svg.append('g').call(yAxis);
#   svg.append('path').datum(data).attr('d',line)
#      .attr('stroke','#ff36ff').attr('stroke-width',1)
#      .attr('stroke-miterlimit',1).attr('stroke-dasharray','0,1')
#      .attr('fill','none').call(reveal);};
# </script>

from IPython.display import IFrame
IFrame(src='example002.html',width=650,height=370)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile example003.html
# <script src='https://d3js.org/d3.v6.min.js'></script>
# n <input type='number' id='n_frames' value=1
# style='width:120px; font-size:120%; color:#363636;
# background-color:silver; text-align:center;'/> 
# m <input type='number' id='m_frames' value=15
# style='width:120px; font-size:120%; color:#363636;
# background-color:silver; text-align:center;'/>
# run =>>> <input type='button' onclick='draw_curves();' value='update'
# style='width:120px; font-size:120%; color:#363636;
# background-color:silver; text-align:center;'/><br/><br/>
# <svg id='svg014' style='background-color:silver;'></svg>
# <script>s=600;
# colors=['#3636ff','#ff3636','#ff36ff',
#         '#ffff36','#36ff36','#36ffff'];
# function subpoint(a,b,m) {
#   return [Math.floor(m/2)*(a[0]+b[0])/m,
#           Math.floor(m/2)*(a[1]+b[1])/m]};
# function subdivpoly(poly,m,iterations=1) {
#   var [p1,p2,p3]=poly,points=[];
#   var centroid=d3.polygonCentroid(poly);
#   if (iterations===0) {points.push(centroid);} 
#   else {var subset1=[p1,subpoint(p1,p3,m),p2],
#             subset2=[p2,subpoint(p1,p3,m),p3];
#         points.push(...subdivpoly(subset1,m,iterations-1));
#         points.push(...subdivpoly(subset2,m,iterations-1));}
#   return points};
# function recursive_curve(len,m,iterations) {
#   var contour1=[[0,len],[0,0],[len,0]],
#       contour2=[[len,0],[len,len],[0,len]];
#   var half1=subdivpoly(contour1,m,iterations),
#       half2=subdivpoly(contour2,m,iterations);
#   return [...half1,...half2];};
# function draw_curves() {
#   var m=parseInt(document.getElementById('m_frames').value);
#   var n=parseInt(document.getElementById('n_frames').value);
#   var line=d3.line();
#   var svg=d3.select('#svg014').attr('width',s).attr('height',s);
#   svg.selectAll('path').remove();
#   svg.selectAll('.curve').data(colors).join('path')
#      .attr('d',(_,i)=>line(recursive_curve(s,m,i+n))+'z')
#      .style('stroke',d=>d).style('stroke-width',3)
#      .style('fill',d=>d).style('fill-opacity',.9)
#      .transition().duration(10000)
#      .style('fill',d=>d).style('fill-opacity',.02); };
# </script>

from IPython.display import IFrame
IFrame(src='example003.html',width=650,height=670)