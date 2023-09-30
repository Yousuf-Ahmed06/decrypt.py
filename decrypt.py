import sys

public_key = int(input("Please enter the public key: "))
g = int(input("Please enter a number: "))

r = 0
remainder = 2
while remainder != 1:
    for exponent in range(1,65535):
        remainder = g**exponent % public_key
        r += 1
        print(remainder)
        
        if remainder == 1:
            print("-"*11)
            print("Remainder has reached: ", remainder)
            print("period = ", r)
            print("-"*11)
            print("\n Performing further calculations \n")
            p = (g**(r/2))+1
            p_r = p % public_key
            while p_r != 0:
                
            q = (g**(r/2)-1)
            print(p, "-", q)
            sys.exit()
        else:
            pass
