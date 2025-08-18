n_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
a, b = 0, 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 1
