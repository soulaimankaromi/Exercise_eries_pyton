age=int(input("type the age :"))
sex=input("type the sex male or female :")
if (age>20 and sex=="male"):
    print("You are obligated to pay the tax")
else:
 if (35>=age>=18 and sex=="female"):
     print("You are obligated to pay the tax")
 else:
    print("You are not obligated to pay the tax")  