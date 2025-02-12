# -*- coding: utf-8 -*-
"""plotting-exercises-r.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DxeJU2U45YLa6yJ_jEY0CaYerozP1W0y

# Plotting with Basic Packages
## Functions
"""

conn<-file("symbol_plotting.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
x<-seq(-2.1,2.1,len=90); y1<-exp(-x^2)
y2<--exp(-x^2); y3<-exp(-x^2)*sin(pi*x^3)
colors<-c('slategray','#3636ff','#ff3636','#ff36ff')
plot(x,y1,type='o',cex=.7,col=colors[2],
     xlim=c(-2.2,2.2),ylim=c(-1,1),xlab='x',ylab='y',
     fg=colors[1],col.axis=colors[1],col.lab=colors[1]) 
lines(x,y2,type='o',cex=.7,col=colors[3])
df<-data.frame(x=x,y=y3)
df$utf_sym<-sapply((32:121),intToUtf8)
points(df$x,df$y,pch=df$utf_sym,
       cex=.9,col=colors[4])
grid(col=colors[1])
#dev.off()",conn)

source('symbol_plotting.R')

conn<-file("parametric_polar_plotting.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
t<-seq(0,2*pi,len=360); c0<-'slategray'
f<-exp(cos(t)^2+sin(t))-3*cos(4*t)+sin(t/12)
x<-f*cos(t); y<-f*sin(t) 
for(i in 1:25) {
    plot(.04*i*x,.04*i*y,type='l',
         cex=.7,col=rgb(.04*i,0,1-.04*i),
         xlim=c(-6,6),ylim=c(-4,6),xlab='x',ylab='y',
         fg=c0,col.axis=c0,col.lab=c0)
    par(new=T)}
grid(col=c0)
#dev.off()",conn)

source('parametric_polar_plotting.R')

conn<-file("parametric_polar_plotting2.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
t<-seq(0,2*pi,len=720); c0<-'slategray'
f1<-(7+.9*cos(12*t))*(1+.05*cos(48*t))
f2<-(1+.05*cos(216*t))*(1+sin(t))
x<-f1*f2*cos(t); y<-f1*f2*sin(t)
for(i in 1:25) {
    plot(i*x,i*y,type='l',cex=.7,col=rgb(0,.04*i,0),
         xlim=c(-270,270),ylim=c(-80,460),xlab='x',ylab='y',
         fg=c0,col.axis=c0,col.lab=c0)
    par(new=T)}
grid(col=c0)
#dev.off()",conn)

source('parametric_polar_plotting2.R')

"""## Random Coefficients"""

conn<-file("random_plotting2.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-(.5+runif(1))*sample(c(-1,1),1); b<-sample(6:18,1) 
c<-.001*sample(1:99,1)*sample(c(-1,1),1)
t<-seq(0,36*pi,len=12*3600); c0<-'lightgray'
col<-rgb(runif(1),runif(1),runif(1))
x<-sin(t/6)-a*sin(b*t)*cos(t)-c*sin(16*b*t) 
y<-cos(t/6)-a*sin(b*t)*sin(t)-c*cos(16*b*t)
cat(c('a =',a,'b =',b,'c =',c,'color:',col,'\n'))
plot(x,y,type='p',cex=.01,col=col,xlab='x',ylab='y',
     fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()",conn)

source('random_plotting2.R')

conn<-file("random_plotting3.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-sample(5:11,1); b<-sample(13:19,1)
c<-2*sample(3:10,1); n<-sample(18:144,1)
cat(c('a =',a,'b =',b,'c =',c,'n =',n,'\n'))
t<-seq(1,2*n+1,1); c1=rgb(runif(1),runif(1),1,alpha=.4)
plot(0,0,type='n',xlab='',ylab='',
     xlim=c(-3,3),ylim=c(-3,3))
for (k in 1:c){
    fx<-sin(pi*t/n+k*2*pi/c)-sin(a*pi*t/n+k*2*pi/c)+
        sin(b*pi*t/n+k*2*pi/c)
    fy<-cos(pi*t/n+k*2*pi/c)+cos(a*pi*t/n+k*2*pi/c)+
        cos(b*pi*t/n+k*2*pi/c)
    polygon(fx,fy,lwd=1,border=c1,xlab='',ylab='',
            xlim=c(-3,3),ylim=c(-3,3)); par(new=T)}
#dev.off()",conn)

source('random_plotting3.R')

conn<-file("random_polygons.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-sample(5:11,1); b<-sample(13:19,1)
c<-2*sample(3:10,1); n<-sample(18:36,1)
cat(c('a =',a,'b =',b,'c =',c,'n =',n,'\n'))
t<-seq(1,2*n+1,1)
c1=rgb(runif(1),1,runif(1),alpha=.15)
plot(0,0,type='n',xlab='',ylab='',
     xlim=c(-3,3),ylim=c(-3,3))
rect(par('usr')[1],par('usr')[3],
     par('usr')[2],par('usr')[4],col='black')
for (k in 1:c) {
    fx<-sin(pi*t/n+k*2*pi/c)-sin(a*pi*t/n+k*2*pi/c)+
        sin(b*pi*t/n+k*2*pi/c)
    fy<-cos(pi*t/n+k*2*pi/c)+cos(a*pi*t/n+k*2*pi/c)+
        cos(b*pi*t/n+k*2*pi/c)
    polygon(fx,fy,lwd=.01,col=c1,xlab='',ylab='',
            xlim=c(-3,3),ylim=c(-3,3)); par(new=T);}
#dev.off()",conn)

source('random_polygons.R')

"""## Rotations"""

conn<-file("plot_rotations.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
rotate_xy<-function (k,x,y){
    i<-1; xyi<-array(c(0,0),c(2*k,2))
    while (i<=2*k) {xyi[i,1]<-cos(i*pi/k)*x-sin(i*pi/k)*y 
                    xyi[i,2]<-sin(i*pi/k)*x+cos(i*pi/k)*y
                    i<-i+1}
    return(xyi)}
k<-sample(100:900,1)/1000; n<-sample(5:15,1)
m<-sample(5:9,1); r<-sample(5:35,m)
lm<-3.5+m*k+max(scale(r,4)[3:m,1])
cat(c('r:',r,'; k =',k,'n =',n,'m =',m,'\n'))
for (i in 1:m) {
    ci<-rotate_xy(n,.5+k*i,.5+k*i)
    col1=rgb(runif(1),runif(1),1)
    col2=rgb(runif(1),runif(1),1,alpha=.07) 
    plot(ci[,1],ci[,2],type='p',cex=r[i],
         col=col1,xlab='',ylab='',
         xaxt='n',yaxt='n',frame=FALSE,
         xlim=c(-lm,lm),ylim=c(-lm,lm))
    par(new=T)
    plot(ci[,1],ci[,2],type='p',pch=16,cex=r[i],
         col=col2,xlab='',ylab='',
         xaxt='n',yaxt='n',frame=FALSE,
         xlim=c(-lm,lm),ylim=c(-lm,lm))
    par(new=T)}
#dev.off()",conn)

source('plot_rotations.R')

conn<-file("plot_rotations2.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-sample(5:9,1); b<-sample(10:14,1)
c<-sample(15:19,1); q<-2*sample(3:10,1) 
n<-sample(4:16,1); l<-5; t<-seq(1,2*n+1,1)
cat(c('a =',a,'b =',b,'c =',c,'q =',q,'n =',n,'\n'))
par(mar=c(0,0,0,0))
plot(0,0,type='n',xlim=c(-l,l),ylim=c(-l,l),
     xlab='',ylab='',xaxt='n',yaxt='n',frame=FALSE)
for (k in 1:q) {
    col1=rgb(runif(1)/2,runif(1)/2,1)
    col2=rgb(runif(1),runif(1),1,alpha=.1)
    par(mar=c(0,0,0,0))
    fy<-cos(pi*t/n+2*k*pi/q)+cos(a*pi*t/n+2*k*pi/q)+
        cos(b*pi*t/n+2*k*pi/q)+cos(c*pi*t/n+2*k*pi/q)
    fx<-sin(pi*t/n+2*k*pi/q)-sin(a*pi*t/n+2*k*pi/q)+
        sin(b*pi*t/n+2*k*pi/q)-sin(c*pi*t/n+2*k*pi/q)
    polygon(1.5*fx,1.2*fy,col=col2,border=FALSE,
            xlab='',ylab='',xlim=c(-l,l),ylim=c(-l,l),
            xaxt='n',yaxt='n'); par(new=T)
    polygon(fx,fy,lwd=1,border=col1,xlab='',ylab='',
            xlim=c(-l,l),ylim=c(-l,l),
            xaxt='n',yaxt='n'); par(new=T)}
#dev.off()",conn)

source('plot_rotations2.R')

"""## Recurrence Tables"""

conn<-file("recurrence_tables.R")
writeLines("#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
gen<-function (a,b,n) {i<-1; xyi<-array(c(0,0),c(n,2))
    while (i<=n-1) {xi<-1-(.2+.01*a)*xyi[i,1]**2+xyi[i,2]
                    yi<-(.9991+.0001*b)*xyi[i,1]; 
                    i<-i+1; xyi[i,1]<-xi; xyi[i,2]<-yi}
    return(xyi)}
xyn<-gen(0,0,7000); c0<-'slategray'
c1<-rgb(runif(1),runif(1),runif(1))
plot(xyn[,1],xyn[,2],type='p',
     cex=.1,col=c1,xlab='x',ylab='y',
     fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()",conn)

source('recurrence_tables.R')

"""# Calling External Packages
## Images
"""

source('../input/r-recipes/rpy_modules.R')
library(keras)
fpath<-'../input/image-examples-for-mixed-styles'
image_paths<-list.files(
    fpath,recursive=TRUE,full.names=TRUE)

options(repr.plot.width=5,repr.plot.height=5,
        repr.plot.bg='gray')
im<-load.image(image_paths[11])
plot(im,main='Original',axes=FALSE)
text(360,20,toString(dim(im)),col='#3636ff')
imrotate(im,45) %>% plot(main='Rotated',axes=FALSE)

options(repr.plot.width=5,repr.plot.height=5,
        repr.plot.bg='gray')
img<-image_to_array(image_load(image_paths[6]))
plot(as.raster(img/255))
text(200,20,toString(dim(img)),col='#3636ff')

"""# Calling Other Languages
## JavaScript
"""

html_str<-"
<script src='https://code.highcharts.com/highcharts.js'></script>
<div id='chart' style='height:620px; width:520px; margin:0 auto'></div>
<script>
function getinteger(min,max) {
    return Math.floor(Math.random()*(max-min+1))+min;};
function fx(a,b,c,t) {
    return Math.sin(.001*t/6)+a*Math.sin(b*.001*t)*
           Math.cos(.001*t)-c*Math.sin(16*b*.001*t)};
function fy(a,b,c,t) {
    return Math.cos(.001*t/6)+a*Math.sin(b*.001*t)*
           Math.sin(.001*t)-c*Math.cos(16*b*.001*t)};
function ar(k,a,b,c) {
    return Array(b*12800).fill(k).map((k,t)=>
          [(1+.01*k)*fx(a,b,c,t),
           (1+.01*k)*fy(a,b,c,t)]);};
function col(i) {
    var r=getinteger(i,255),g=getinteger(i,255),b=getinteger(i,255);
    return 'rgb('+r+','+g+','+b+')';}; 
var series=[]; var n=2;
var a=0.5+Math.random(),c=.001*getinteger(1,99),b=getinteger(3,12);
for (var i=1; i<n+1; i++) {
    series.push({name:i.toString(),color:col(i),
                 lineWidth:.6/i,data:ar(i,a,b,c)})};
Highcharts.chart('chart',{
    chart:{type:'line',backgroundColor:'silver'},
    xAxis:{title:{text:'x'}},yAxis:{title:{text:'y'}},
    title:{text:'Random Parameters: a,b,c = '+[a,b,c]},
    credits:{enabled:false},legend:{enabled:false},
    series:series});
</script>"
source('../input/r-recipes/embedding_html.R')
embedding_html_string(html_str,550,650)

"""## Python"""

conn<-file("rpy_random_plotting.R")
writeLines("
pi<-np$pi; n<-24
t<-np$arange(0,2*pi,.1^3*2*pi/n)
randi<-function(nmin,nmax){np$random$randint(nmin,nmax)}
a<-randi(5,11); b<-randi(12,24); c<-randi(25,81)
d<-randi(216,256); m<-randi(100,300)
fig<-pl$figure(figsize=c(10,10)); ax<-fig$gca()
ax$set_facecolor('black')
for (i in 1:n) {
    f1<-(a+.9*np$cos(b*t+2*pi*i/n))*(1+.1*np$cos(c*t+2*pi*i/n))
    f2<-(1+.01*np$cos(d*t+2*pi*i/n))*(1+np$sin(t+2*pi*i/n)) 
    x<-f1*f2*np$cos(t); y<-f1*f2*np$sin(t)
    pl$scatter(x,y,s=.1^2) }
pl$grid()
file_name<-paste0('rpy_random_plot',
                  sample(1:9999999,1),'.png')
pl$savefig(file_name)
im<-load.image(file_name)
options(repr.plot.width=10,repr.plot.height=10)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)
",conn)

source('rpy_random_plotting.R')