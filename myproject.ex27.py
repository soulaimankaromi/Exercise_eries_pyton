n=int(input('Enterc a number : '))
if n>0:
    print("Divisors of number ",n," is")
for i in range(1,n+1):
     if n%i==0:
         print(i)
else:
    if n<0:
     print("Please type a positive number!")