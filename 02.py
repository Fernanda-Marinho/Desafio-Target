def pertence_fibonacci(n):
    a = 0
    b = 1 

    if (n == 0 or n == 1):
        return True

    while (b < n):
        a = b
        b = a + b
    
    return (b == n)


numero = int(input("informe o numero: "))

if (pertence_fibonacci(numero)):
    print("pertence")
else:
    print("nao pertence")

