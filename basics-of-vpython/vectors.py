from vpython import *

A = vector(0, 0, 1) #Defines a vector using the "vector()" method
B = vector(-1, 1, -2)
print("Sum of x and y-components of A: ", A.x + A.y) #vector.component allows you to access a specific component of a given vector
print("Magnitude of A as sum of squares of components: ", sqrt(A.x**2 + A.y**2 + A.z**2))
print("Scalar multiplication: ",2*A)

C = A + B
print("Sum of A and B: ", C)

D = mag(A) #Defining magnitude of a vector (|A|) using the "mag()" method
print("|A| =", D)

E = mag2(B) #Defining magnitude square of a vector (|A|*|A|) using the "mag2()" method
print("|A|*|A| =", E)

F = hat(B) #Defines the unit vector for a given vector [Can also be defined with "norm()"]
print("B_hat =", F)

G = dot(A, B) #Calculates dot product between two vectors
print("A.B =", G)

H = cross(A, B) #Calculates cross product between two vectors
print("AxB =", H)

I = diff_angle(A, B) #Calculates the angle between two vectors
print("Angle between A and B =", I)

J = proj(A, B) #Calculates the vector projection of A on B
print("Projection of A along B =", J)

K = comp(A, B) #Calculates the scalar projection of A on B
print("Scalar projection of A along B =", K)

L = rotate(A, pi/2, vector(1, 0, 0))
print("Rotation of A about x-axis by 90 degrees: ", L)

print("Random vector: ", vector.random()) #Generates a random vector with magnitude of components between -1 and 1