from matplotlib.pyplot import *
from numpy import linspace

maxy = 16

def y_x(x,r1,r2):
  y = []
  for i in x:
    y0 = abs(i)**r1 + abs(i)**r2
    if y0 < maxy:
      y.append( y0 )
    else: y.append( y[-1] ) #plateau when above max
  return y

#
# (i)
#

xi = linspace(-3,3,1000)
yi = y_x(xi,0.5,-0.5)
subplot('221')
plot(xi,yi,label='(i)')
# asymptote
x_asm = [-0.0000001,0.0000001]
y_asm = [1,12]
plot(x_asm,y_asm,color='r',linestyle='dashed',linewidth=3)
grid(True)
title( '(i)' )

#
# (ii)
#

xii = linspace(-1.5,1.5,1000)
yii = y_x(xii,complex(-0.25,5),complex(-0.25,-5))
subplot('222')
plot(xii,yii,label='(ii)')
grid(True)
title( '(ii)' )

#
# (iii)
#

xiii = linspace(-5,5,1000)
yiii = y_x(xiii,complex(0.5,5),complex(0.5,-5))
subplot('223')
plot(xiii,yiii,label='(iii)')
grid(True)
title( '(iii)' )

#
# Other stuff
#

suptitle('AM351 Assignment 2 Question 3c')
subplots_adjust(hspace=0.4  )
#show()
savefig('AM351_A03_Q3c.pdf')
