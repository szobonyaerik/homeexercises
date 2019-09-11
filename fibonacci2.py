how_many_num = int(input("Enter how many Fibonacci numbers do you want: "))

index = 1
num1 = 0
num2 = 1
fib = 0



while index <= how_many_num:
    print(fib)
    fib =num1 + num2
    num2 = num1
    num1 = fib
    index += 1
