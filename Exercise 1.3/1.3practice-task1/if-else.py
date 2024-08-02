a = int(input("Choose a number: "))
b = int(input("Choose another number: "))
op = input("Choose an operator, either + or - : ")

if op == "+":
    print("Add ", str(a), "and ", str(b), "to get ", a + b )
elif op == "-":
    print("Subtract ", str(a), "and ", str(b), "to get ", a - b)
else: 
    print("Unknown operator")