import matplotlib.pyplot as plt
from pylab import*
import numpy as np

#1)

x = linspace(0,5,100)
y = x*x
plt.plot(x ,  y ,'r', "--or")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^2')
plt.legend()
plt.show()

#2)

x = linspace(-5,5,100)
y = x*x*x
plt.plot(x ,  y ,'b', "--o")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^3')
plt.legend()
plt.show()


#3)

x = linspace(-1,1,100)
y = x*x
f = x*x*x
plt.plot(x ,  y ,'b', ls ='--')
plt.plot(x , f, 'g' ,ls = '-.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^2 and g(x) = x^3')
plt.legend()
plt.show()


#4)


x = linspace(-2*pi,2*pi,100)
y = np.sin(x)
plt.plot(x ,  y ,'y', ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = sin(x)')
plt.legend()
plt.show()



#5)

x = linspace(-10,10,100)
y = np.exp(x)
plt.plot(x , y , 'm')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)=e^x')
plt.legend()
plt.show()


#6)

x = linspace(-10,10,100)
y = 1+x+2*x*x+3*x*x*x+4*x*x*x*x
plt.plot(x , y , 'b' , ls = '--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Graph of f(x)=1+x+2*x^2+3*x^3+4*x^4")
plt.legend()
plt.show()

#7)

x = linspace(-2*pi,2*pi,100)
y = np.sin(x)
f = np.cos(x)
plt.plot(x , y , 'm' ,ls ='-.')
plt.plot(x , f , 'g' ,ls = '.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= sin(x) and g(x)= cos(x)')
plt.legend()
plt.show()


#8)

x = linspace(-5,5,100)
y = 1/x
plt.plot(x , y , 'b' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= 1/x')
plt.legend()
plt.show()

#9)

x = linspace(-5,5,100)
y = 1+1/x+1/x*x
plt.plot(x , y , 'g' ,ls ='-.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= 1/x+1/x*x')
plt.legend()
plt.show()




#10)

x = linspace(0,10,100)
y = x* np.sin(1/x*x)
plt.plot(x , y , 'r' ,ls ='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x*sin(1/x^2')
plt.legend()
plt.show()

#11)

x = linspace(0,10,100)
y = np.log(x)
plt.plot(x , y , 'r' ,ls ='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= log(x)')
plt.legend()
plt.show()

#12)

x = linspace(0,10,100)
y = x*x*x*x
plt.plot(x , y , 'r' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x^4')
plt.legend()
plt.show()

#13)

x = linspace(-5,5,100)
y = np.exp(-x*x)
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = e^(-x^2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-x*x)')
plt.legend()
plt.show()


#14)


x = linspace(-5*pi,5*pi,100)
y = np.exp(x)*sin(x)
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = e^(x)*sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= e^(x)*sin(x)')
plt.legend()
plt.show()




#15)

x = linspace(0,5,100)
y = x*x*x*x
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = x^4')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x^4')
plt.legend()
plt.show()

#16)

x  = np.linspace(0,5,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x)
y4 = x**2
plt.subplot(2,2,1)
plt.plot(x , y1 , 'r', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(2,2,2)
plt.plot(x , y2 , 'y',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(2,2,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.subplot(2,2,4)
plt.plot(x , y4 , 'g',  label = 'y = x^2')
plt.legend()

plt.show()


#17)

x  = np.linspace(0,5,100)
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = np.exp(1/x)
plt.subplot(3,1,1)
plt.plot(x , y1 , 'r', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(3,1,2)
plt.plot(x , y2 , 'y',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(3,1,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.show()

#18)
x  = np.linspace(0,5,100)
y1 = np.exp(-0.5*x)
y2 = np.exp(-1.0*x)
y3 = np.exp(-1.5*x)
y4 = np.exp(-2.0*x)
plt.subplot(2,2,1)
plt.plot(x , y1 , 'y', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(2,2,2)
plt.plot(x , y2 , 'g',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(2,2,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.subplot(2,2,4)
plt.plot(x , y4 , 'black',  label = 'y = x^2')
plt.legend()
plt.show()

#19)

x = np.linspace(-1,1,100)
f = x*x
g = x*x*x
plt.plot(x , f  ,'g' ,ls='--' , label = 'y1 =x^2')
plt.plot(x , g , 'r' ,'solid' , label ='y2 = x^3')
plt.title('f(x) = x^2 and g(x)= x^3')
plt.legend(loc=0)
plt.show()

#20)

x = np.linspace(-10,10,100)
f = 3*x*x*x*x + 3*x*x*x + 7*x*x + 2*x+9
g = 52*x*x*x + 2*x + 9
plt.plot(x , f  ,'g' ,ls='--' )
plt.plot(x , g , 'r' ,'solid' )
plt.title('Graph of f(x) = 3*x^4 + 3*x^3 + 7*x^2 + 2*x + 9 and ' , 'Graph of g(x) = 52*x^3 + 2*x+ 9')
plt.legend(loc=0)
plt.show()

#21)

x = linspace(0,10,100)
y = np.exp(-x)*np.sin(2*x+3)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-x)*xin(x)')
plt.legend()
plt.show()

#22)

x = np.linspace(0,1,100)
f = np.exp(-1.5*x)*sin(10*x)
g = np.exp(-2.0*x)*sin(10*x)
plt.plot(x , f  ,'g' ,ls='--' , label = 'y1 =exp(-1.5*x)')
plt.plot(x , g , 'r' ,'solid' , label ='y2 = exp(-2.0*x)')
plt.title('f(x) = exp(-1.5*x) and g(x)= exp(-2.0*x)')
plt.legend(loc=0)
plt.show()

#23)

x = linspace(-5,5,100)
y = np.exp(-pi/2)*np.sin(2*pi*x)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-pi/2)*np.sin(2*pi*x)')
plt.legend()
plt.show()

#24)

x = linspace(-10,10,100)
y = x*np.sin(x)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x*sin(x)')
plt.legend()
plt.show()












#1)

x = linspace(0,5,100)
y = x*x
plt.plot(x ,  y ,'r', "--or")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^2')
plt.legend()
plt.show()

#2)

x = linspace(-5,5,100)
y = x*x*x
plt.plot(x ,  y ,'b', "--o")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^3')
plt.legend()
plt.show()


#3)

x = linspace(-1,1,100)
y = x*x
f = x*x*x
plt.plot(x ,  y ,'b', ls ='--')
plt.plot(x , f, 'g' ,ls = '-.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = x^2 and g(x) = x^3')
plt.legend()
plt.show()


#4)


x = linspace(-2*pi,2*pi,100)
y = np.sin(x)
plt.plot(x ,  y ,'y', ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x) = sin(x)')
plt.legend()
plt.show()



#5)

x = linspace(-10,10,100)
y = np.exp(x)
plt.plot(x , y , 'm')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)=e^x')
plt.legend()
plt.show()


#6)

x = linspace(-10,10,100)
y = 1+x+2*x*x+3*x*x*x+4*x*x*x*x
plt.plot(x , y , 'b' , ls = '--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Graph of f(x)=1+x+2*x^2+3*x^3+4*x^4")
plt.legend()
plt.show()

#7)

x = linspace(-2*pi,2*pi,100)
y = np.sin(x)
f = np.cos(x)
plt.plot(x , y , 'm' ,ls ='-.')
plt.plot(x , f , 'g' ,ls = '.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= sin(x) and g(x)= cos(x)')
plt.legend()
plt.show()


#8)

x = linspace(-5,5,100)
y = 1/x
plt.plot(x , y , 'b' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= 1/x')
plt.legend()
plt.show()

#9)

x = linspace(-5,5,100)
y = 1+1/x+1/x*x
plt.plot(x , y , 'g' ,ls ='-.')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= 1/x+1/x*x')
plt.legend()
plt.show()




#10)

x = linspace(0,10,100)
y = x* np.sin(1/x*x)
plt.plot(x , y , 'r' ,ls ='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x*sin(1/x^2')
plt.legend()
plt.show()

#11)

x = linspace(0,10,100)
y = np.log(x)
plt.plot(x , y , 'r' ,ls ='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= log(x)')
plt.legend()
plt.show()

#12)

x = linspace(0,10,100)
y = x*x*x*x
plt.plot(x , y , 'r' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x^4')
plt.legend()
plt.show()

#13)

x = linspace(-5,5,100)
y = np.exp(-x*x)
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = e^(-x^2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-x*x)')
plt.legend()
plt.show()


#14)


x = linspace(-5*pi,5*pi,100)
y = np.exp(x)*sin(x)
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = e^(x)*sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= e^(x)*sin(x)')
plt.legend()
plt.show()




#15)

x = linspace(0,5,100)
y = x*x*x*x
plt.plot(x , y , 'r' ,"^" ,ls ='--' ,label = ' f(x) = x^4')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x^4')
plt.legend()
plt.show()

#16)

x  = np.linspace(0,5,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x)
y4 = x**2
plt.subplot(2,2,1)
plt.plot(x , y1 , 'r', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(2,2,2)
plt.plot(x , y2 , 'y',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(2,2,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.subplot(2,2,4)
plt.plot(x , y4 , 'g',  label = 'y = x^2')
plt.legend()

plt.show()


#17)

x  = np.linspace(0,5,100)
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = np.exp(1/x)
plt.subplot(3,1,1)
plt.plot(x , y1 , 'r', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(3,1,2)
plt.plot(x , y2 , 'y',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(3,1,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.show()

#18)
x  = np.linspace(0,5,100)
y1 = np.exp(-0.5*x)
y2 = np.exp(-1.0*x)
y3 = np.exp(-1.5*x)
y4 = np.exp(-2.0*x)
plt.subplot(2,2,1)
plt.plot(x , y1 , 'y', label ='y = sin(x)' , ls = '--')
plt.legend()
plt.subplot(2,2,2)
plt.plot(x , y2 , 'g',label = 'y = cos(x)' ,ls='-.')
plt.legend()
plt.subplot(2,2,3)
plt.plot(x , y3 , 'b',  label = 'y=exp(x)')
plt.legend()
plt.subplot(2,2,4)
plt.plot(x , y4 , 'black',  label = 'y = x^2')
plt.legend()
plt.show()

#19)

x = np.linspace(-1,1,100)
f = x*x
g = x*x*x
plt.plot(x , f  ,'g' ,ls='--' , label = 'y1 =x^2')
plt.plot(x , g , 'r' ,'solid' , label ='y2 = x^3')
plt.title('f(x) = x^2 and g(x)= x^3')
plt.legend(loc=0)
plt.show()

#20)

x = np.linspace(-10,10,100)
f = 3*x*x*x*x + 3*x*x*x + 7*x*x + 2*x+9
g = 52*x*x*x + 2*x + 9
plt.plot(x , f  ,'g' ,ls='--' )
plt.plot(x , g , 'r' ,'solid' )
plt.title('Graph of f(x) = 3*x^4 + 3*x^3 + 7*x^2 + 2*x + 9 and ' , 'Graph of g(x) = 52*x^3 + 2*x+ 9')
plt.legend(loc=0)
plt.show()

#21)

x = linspace(0,10,100)
y = np.exp(-x)*np.sin(2*x+3)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-x)*xin(x)')
plt.legend()
plt.show()

#22)

x = np.linspace(0,1,100)
f = np.exp(-1.5*x)*sin(10*x)
g = np.exp(-2.0*x)*sin(10*x)
plt.plot(x , f  ,'g' ,ls='--' , label = 'y1 =exp(-1.5*x)')
plt.plot(x , g , 'r' ,'solid' , label ='y2 = exp(-2.0*x)')
plt.title('f(x) = exp(-1.5*x) and g(x)= exp(-2.0*x)')
plt.legend(loc=0)
plt.show()

#23)

x = linspace(-5,5,100)
y = np.exp(-pi/2)*np.sin(2*pi*x)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= exp(-pi/2)*np.sin(2*pi*x)')
plt.legend()
plt.show()

#24)

x = linspace(-10,10,100)
y = x*np.sin(x)
plt.plot(x , y , 'g' ,ls ='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph of f(x)= x*sin(x)')
plt.legend()
plt.show()










