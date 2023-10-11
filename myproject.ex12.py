A = int(input("type the number A:"))
B = int(input("type the number B:"))
C = A * B
if C>0 :
   C=A
   A=B
   B=C
   print("the value of A is :" ,A)
   print("the value of B is :" ,B)
else:
    D=A+B
    print("the sum solution is : ", D)
    print("the product solution is : " ,C)