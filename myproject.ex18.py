price = int(input("Type the price of the product :"))
type= input("Enter the product type A OR B OR C :")
if type =="A":
  print("product type A")
  print("Price including tax",price+(price*0.07))
  print("Price without tax",price)
else:
 if type =="B" :
   print("product type B")
   print("Price including tax",price+(price*0.2))
   print("Price without tax",price)
 else:
  if type =="C":
    print("product type C")
    print("Price including tax",price+(price*0.25))
    print("Price without tax",price)