how_many_num = int(input("Enter how many Fibonacci numbers do you want: "))

fib_list = []
lines = 1
index = 1
num1 = 0
num2 = 1
fib = 0



while index <= how_many_num:
    fib_list.append(fib)
    fib =num1 + num2
    num2 = num1
    num1 = fib
    index += 1

for i in fib_list:
    print("{}: {:>30}".format(lines, i))
    lines += 1
