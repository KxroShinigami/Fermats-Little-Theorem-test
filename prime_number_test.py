basis = 2;

input = input("Geben Sie ihre zu testende Zahl ein:");

input = int(input);

for basis in range(1, input):
    #print(basis)
    if ((basis**(input-1))%input == 1):
        #print(basis, " ...ergibt 1")
        if (basis == (input-1)):
            print(input, " ist eine Primzahl oder Carmichael-Zahl")
    else:
        print(input, " ist keine Primzahl")
        break