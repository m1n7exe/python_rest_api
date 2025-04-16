def ope():
    if operator <= 5 and operator >= 1:
        n1=float(input("\nEnter first number: "))
        n2=float(input("Enter first number: "))
        if operator == 1:
            result=n1+n2
            print(f"{n1} + {n2} = {result}")
        elif operator == 2:
            result=n1-n2
            print(f"{n1} - {n2} = {result}")
        elif operator == 3:
            result=n1*n2
            print(f"{n1} * {n2} = {result}")
        elif operator == 4:
            result=n1/n2
            print(f"{n1} / {n2} = {result}")
        elif operator == 5:
            result=n1%n2
            print(f"{n1} % {n2} = {result}")
    else:
        print("Invalid input, only enter the number shown")

again='y'

while again =='Y'or again =='y':
    print("\nSelect an operator:")
    print("1. + (Addition)")
    print("2. - (Subtraction)")
    print("3. * (Multiplication)")
    print("4. / (Division)")
    print("5. % (Modulus)\n")
    operator = int(input("Enter the operator number (1-5): "))

    ope()

    print("Try again? (Y/N): ")
    again = input()

print("Goodbye!")