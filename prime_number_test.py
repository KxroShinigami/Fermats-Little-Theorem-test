#--> Fermats-Little-Theorem-Test
#-> Fermats little Theorem test for a number to be a prime number or a Carmichael-number.

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
        #print(base)
        if ((base**(num-1))%num == 1):
            #print(base, " ...is 1")
            if (base == (num-1)):
                print(num, " is a prime number or a Carmichael-number.")
        else:
            print(num, " is no prime number")
            break

fermats_little_theorem_test(num)