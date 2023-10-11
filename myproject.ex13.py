N= int(input("type the number N of photocopies:"))
if N<=10:
    print("the price to pay :",N * 0.30, "DH")
if 10<N<=30 :
    print("the price to pay :",10*0.30+(N-10)*0.25 , "DH")
if 30<N:
    print("the price to pay :",10*0.30+20*0.25+(N-30)*0.2 , "DH")