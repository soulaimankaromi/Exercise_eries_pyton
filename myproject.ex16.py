import cmath
A=float(input("type THE VALUES OF A :"))
B=float(input("type THE VALUES OF B :"))
C=float(input("type THE VALUES OF C :"))
D = (B*B)-A*C*4
if D < 0 :
    print("no solution")
elif D == 0 :
    X = (-B)/(2*A)
    print("the solution is:", X)
else :
    X1 = (-B + cmath.sqrt(D))/(2*A)
    X2 = (-B - cmath.sqrt(D))/(2*A)
    print("the solution is :", X1 ,"and" , X2)