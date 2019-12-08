from math import*
import numpy as np
#User input 3 coordinates
D1= float(input('Enter first coordinate x1: '));
E1=float(input('Enter first coordinate y1: '));
D2=float(input('Enter second coordinate x2: '));
E2=float(input('Enter second coordinate y2: '));
D3=float(input('Enter third coordinate x3: '));
E3=float(input('Enter third coordinate y3: '));

#Creating matrix for solving 3 eq 3 unknowns
F=1;
G1=-((D1*D1)+(E1*E1));
G2=-((D2*D2)+(E2*E2));
G3=-((D3*D3)+(E3*E3));

A=np.array([[2*D1,2*E1,F],[2*D2,2*E2,F],[2*D3,2*E3,F]])
B=np.array([[G1],[G2],[G3]])
z=np.linalg.solve(A,B) #using np.linalg.solve() to multiply inverse of matrix A and mstrix B to store to z

D=z[0]; #to call out values from Z
E=z[1];
F=z[2];

print('Center: (%.2f,%.2f)'%(float(-D),float(-E))) #printing values
print('The radius is %.2f'%sqrt((D)*(D)+(E)*(E)-F))
print('Vector [D,E,F]:[%.2f, %.2f, %.2f]'%(float(D),float(E),float(F)))



