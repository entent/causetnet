##time

#d=2
x1=seq(-1,0,length=51)
x2=seq(0,1,length=51)
y=1-abs(x)
y1=(1/2)*x1^2+x1+(1/2)#(1/2)*(x1+1)^2
y2=-(1/2)*x2^2+x2+(1/2)#1-(1/2)*(1-x2)^2
x3=c(x1,x2)
y3=c(y1,y2)
x4=seq(-1,1,length=101)
y4=(-sign(x4)*(1/2)*(x4^2))+x4+1/2
#f=outer(x,y,function(x,y)cos(y)/(1+x^2))
#contour(x,y,f)
y3
plot(x1, y1, type="l") 
plot(x2, y2, type="l") 
plot(x3, y3, type="l") 
plot(x4, y4, type="l") 
#lines(x, y, type="l")
sign(x4)



x5=seq(0,0.5,length=101)
y5=-1+sqrt(2*x5)
x6=seq(0.5,1,length=101)
y6=1-sqrt(2-2*x6)
x7=c(x5,x6)
y7=c(y5,y6)
plot(x7, y7, type="l") 
sqrt(2*x5)
x5

#d=3
#distribution
x1=seq(-1,1,length=101)
y1=x1^2-2*abs(x1)+1
plot(x1, y1, type="l") 
#area under curve
x21 = seq(-1,0,length=51)
x22 = seq(0,1,length=51)
y21 = 1/2*(x21+1)^3
y22 = -1/2*(1-x22)^3 + 1
x2=c(x21,x22)
y2=c(y21,y22)
plot(x2, y2, type="l") 
#inverse area function
x31=seq(0,0.5,length=101)
x32=seq(0.5,1,length=101)
y31=(2*x31)^(1/3)-1
y32=-(2-2*x32)^(1/3)+1
x3=c(x31,x32)
y3=c(y31,y32)
plot(x3, y3, type="l") 














