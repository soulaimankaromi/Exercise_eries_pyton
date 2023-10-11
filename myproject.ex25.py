N=int(input("type a non-zero positive number : "))
S=1
while N<0 :
 N=int(input("type a non-zero positive number : "))
for i in range(1,N+1):
 S = S * i
print("the factorial of",N,"is:",S)

