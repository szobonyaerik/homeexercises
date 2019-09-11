
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


number = input("Enter a number: ")
op = input("Enter an operator: ")
number2 = input("Enter a number: ")

if number not in abc and number2 not in abc:

        number = int(number)
        number2 = int(number2)

        if op == "+":
            print(number + number2)
        elif op == "*":
            print(number * number2)
        elif op == "-":
            print(number-number2)
        elif op == "/":
            print(number / number2)
        else:
            print("Invalid operator!")

else:
    print("Thank you :)")
