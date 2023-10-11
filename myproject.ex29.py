P_M=1000000   #P_M=Population_of_Marrakech
P_A=500000    #P_A=Population_of_Agadir
Y=0   #Y=years
while P_A<= P_M :
    P_M=P_M+500000
    P_A=P_A*(1+0.08)
    Y=Y+1
print('The population of Agadir will exceed that of Marrakech in',Y,'years')