n=int(input("type the value of n: "))
while n<2:
  N=int(input("Enter the value of n:"))
U1=1
U2=0
print(U1)
for i in range (2,n+1):
  Un=U1+U2
  print(Un)
  U2=U1
  U1=Un