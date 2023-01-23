#
# Sanjay R. Kharche.
# AM1201B, sections 3 and 4.
# Feb 2, 2021.
# A python program to see the solution u = ln ( t - 0.5 + 2.0 * ln(2*t-2) ), and verify the overestimation due to concave down
# property of the differential equation. Concave down is when f''(x) < 0.
# What the program does:
# 1) It takes t values from 3/2 to 9/2.
# 2) It plots u as a function of time t.
# 3) In the second part (you may have to close the figure first, or hang about for 30 seconds), it uses Euler method and provides a numerical solution.
#
################################################################## 
# New concept: We already saw for loop, this program introduces the while loop.
##################################################################
#
# Import all that you need. math, numpy (math may be accessible from numpy), and matplotlib for plotting.
import math
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure
#
#
# Get t values of your choice. These are t values from 3/2 to 9/2, in steps of h = 0.05 (I took small h to make graph look smooth).
t        			= np.arange(3.0/2.0, 9.0/2.0, 0.05);
# Calculate the solution y for all values of t you have taken.
# The spelling "log" in Python means "ln" in normal speak.
u   				= np.log(t - 0.5 + 2.0 * np.log(2*t-2) )  # double check that this is the formula given on page 9, ex 2, of chapter 3.
#
#
# Plot y vs x, and yy vs x.
figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
plot.rcParams['font.size'] = '22'
plot.plot(t, u,'black', label='y', linewidth=8)
# Give a title.
plot.title('Equation of exercise 2 in chapter 3.')
# Give x axis label.
plot.xlabel('x')
# Give y axis label.
plot.ylabel('y')
plot.grid(False, which='both')
plot.axhline(y=0, color='k')
plot.show(block=False) # plot show will draw all figures you set up using plot.plot.
#
plot.pause(45)
plot.close()
#
# Now do a bit of Euler. Do not vectorize, keep it simple and tangible (KISS approach).
# You should also do this in Excel.
t0 			= 3.0/2.0 	# initial time.
tf 			= 9.0/2.0 	# final time.
t 			= t0 		# initially time is at t0.
u0 			= 0.0		# initial condition.
uk			= u0		# initially, the u at k is u0.
timeStep 	= 1			# iterator of first time step.
maxTimeStep = 16			# Given that there are 16 intervals.
h			= (tf - t0)/maxTimeStep
#
#
print("\t\t\t%s\t%s\t%s" % ('time', 'nu.sol.', 'ext sol.'))	
while timeStep<=maxTimeStep+1:	 # do not use real numbers (e.g. t) for loop iterators.
	uexact 		= np.log(t - 0.5 + 2.0 * np.log(2*t-2) ) # work out exact solution at same time, tk, to be able to compare (print or plot) with the Euler.
	# this ukplus1 below is the solution at time t(k+1)
	ukplus1 		= uk + h * (t+1.0)/(t-1.0) * np.exp(-uk) # DE on page 9, ex 2 of chapter 3, solved for 1 time step using Euler's method.
#	print[t, uk, uexact]
	print("\t\t\t%1.3f\t%1.3f\t%1.3f " % (t, uk, uexact))	
	t 			= t + h 				# augment value of t by your time step, h, after you finish all calculations in the loop.
	timeStep 	= timeStep + 1 		# increment time step.
	uk 			= ukplus1 # do something with the ukplus1 (e.g. write to screen) and assign to uk in preparation for next iteration of loop.
	
# end of program.
