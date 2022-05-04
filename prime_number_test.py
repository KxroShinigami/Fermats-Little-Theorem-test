#--> Fermats-Little-Theorem-Test
#-> Fermats little Theorem test for a number to be a prime number or a Carmichael-number with the calculation help of the Montgomery-Ladder.

# Input
try: # a
        num = int(input("Please enter your number to be tested: "))
except Exception as e:
        print("\nError: ", e)

# Loop
def fermats_little_theorem_test(num):
    # Initializing
    base = 2
    
    for base in range(1, num):
        print("base: ", base)
        if (MontLadder(base, (num-1), num) == 1):
            #print(base, " ...is 1") # optional
            if (base == (num-1)):
                print(num, " is a prime number or a Carmichael-number.")
        else:
            print(num, " is no prime number")
            break


def MontLadder(a, k, mod):
    # Formatting exponent k into a binary number
    k_bin = format(k, 'b')


    # Initializing x and y
    x = 1
    y = a % mod


    # Loop 
    for i in range(len(k_bin)):
        if k_bin[i] == "0":
            y = (x * y) % mod
            x = pow(x, 2, mod)

        elif k_bin[i] == "1":
            x = (x * y) % mod
            y = pow(y, 2, mod)

        #print(str(len(k_bin) - i - 1), ": x = ", str(x) + "; y = ", str(y))   # optional

# Output: x
    print("x = a^k =  " + str(x))
    return x

# Calling the function
fermats_little_theorem_test(num)