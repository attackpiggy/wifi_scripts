import math

def r_square():
    SSE=input("Enter the value here: ")
    k=input("Enter the value of K here : ")
    ssto=1052.10
    r_squared=(1-(SSE/ssto))

    print("The values for R_Squared: " ,r_squared)

    r_adjusted=(1-((1-r_squared)*31)/(32-k-1))
    print ("The adjusted values are :", r_adjusted)







    
r_square()

