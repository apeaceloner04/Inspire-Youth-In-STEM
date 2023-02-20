print(" prime numbers from 1 - 100 are ... ")
for x in range(1,100 + 1):
    if x > 0:
        for i in range ( 2,x ):
            if x%i ==0:
                break
        else:
            print(x)