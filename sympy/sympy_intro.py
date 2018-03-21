#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : sympy_intro.py
Purpose : learn the basics of sympy
Creation Date : 21-02-2018
Last Modified : Wed 21 Feb 2018 12:25:59 PM EST
Created By : Samuel M. Haugland

==============================================================================


 .d8888b. Y88b   d88P 888b     d888 8888888b. Y88b   d88P
d88P  Y88b Y88b d88P  8888b   d8888 888   Y88b Y88b d88P
Y88b.       Y88o88P   88888b.d88888 888    888  Y88o88P
 "Y888b.     Y888P    888Y88888P888 888   d88P   Y888P
    "Y88b.    888     888 Y888P 888 8888888P"     888
      "888    888     888  Y8P  888 888           888
Y88b  d88P    888     888   "   888 888           888
 "Y8888P"     888     888       888 888           888

'''

import numpy as np
#from sympy import symbols,simplify,expand_trig,sin,cos,sqrt,pi,lambdify
#also can import everything from sympy
#I'm putting this comment on github
from sympy import *

#Create symbol objects to be used in symbolic computations.
#Two ways of doing this.
x,y,z = symbols('x y z')
x,y,z = symbols('x,y,z')

#Now make expression using these symbols

expr = x**2+2*y**2+z**2

#Substitute variables for numbers by passing dictionary object
expr.subs({x:2,y:3,z:0})

#Substitute variables for other expressions
expr.subs({x:2*y+1})

#Make two equivalent mathematical statements
expr = (2*x+3)**2
fact = 4*x**2+12*x+9

#Factor a polynomial
expr = factor(fact)

#expand into polynomial
fact = expand(expr)

#This statement will return False
expr == fact

#if expr = factor, then expr-factor = 0
#Use sympy.simplify 
simplify(expr-fact) == 0

#Using the equals method of an expression will test equivalence at discrete 
#points.

expr.equals(fact)

#Expand trig functions (must have sympy trig functions imported)
cos_expand = expand_trig(cos(2*x))
sin_expand = expand_trig(sin(2*x))

#Evaluate irrational numbers to arbitrary decimal points
sqrt_2_10 = sqrt(2).evalf(10)
pi_100 = pi.evalf(100)

#Evaluate expression for many points using lambdify
a = np.linspace(0,10)
expr = sin(2*x)+cos(3*x)
f = lambdify(x,expr,'numpy')
evaluate = f(a)

#Enable pretty printing
#Either use init_session()
#or use pprint

'''
  ______  ______  __      ______  __  __  __      __  __  ______
 /\  ___\/\  __ \/\ \    /\  ___\/\ \/\ \/\ \    /\ \/\ \/\  ___\
 \ \ \___\ \  __ \ \ \___\ \ \___\ \ \_\ \ \ \___\ \ \_\ \ \___  \
  \ \_____\ \_\ \_\ \_____\ \_____\ \_____\ \_____\ \_____\/\_____\
   \/_____/\/_/\/_/\/_____/\/_____/\/_____/\/_____/\/_____/\/_____/

'''

#Differentate simple function.
diff(exp(x**2),x)

#Take a fifth order partial derivative with respect to many variables
messy_diff = diff(exp(x**2+y**3+2*z),x,y,y,z,z)

#return latex formula
print latex(messy_diff)

#Make derivative object for use in differential equation
d = Derivative(exp(x**2+y**3+2*z),x,y,y,z,z)

#Integrate a function symbolically
integrate(exp(x**2+y**3),x)

#Compute a definite integral, even improper integral
#From x = 0 to inf
integrate(exp(x**2+y**3),(x,0,oo))

#Make Integral object 
Integral(exp(x**2+y**3),x)

#Integral of multiple variables
integral_func = Integral(exp(-x**2-y**2),(x,-oo,oo),(y,-oo,oo))

#Use .doit() method on unevaluated integral function
integral_func.doit()

#Limits
limit_function = Limit(sin(x)/x, x, 0)
limit_function.doit()

#Series expansion
expr = exp(sin(x))
expr.series(x,0,4)

#Solving algebraic equations
solve(3*x**2+2*x+1,x)

#Make a differentail equation













