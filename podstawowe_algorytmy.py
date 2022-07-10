#Exponential Normally
def number_exp(number:float, exp:int ) -> float:
    temp = 1
    for i in range(exp):
        temp *= number
    print(temp)
    return temp


#Exponential recursive
def number_exp_rek(number: float, exp:int) -> float:
    if exp == 0:
        return 1
    return number * number_exp_rek(number,exp-1)


#Plaindrome Normally
def is_palindrome(expression):
    expression = list(expression)
    counter = 0
    for i in range(len(expression)):
        if expression[i] == expression[-1-i]:
            counter += 1

    if counter == len(expression):
        print("Palindrome!")
    else:
        print("Not a palindrome!")


# Palindrome Recursive
def is_palindrome_rek(expression):
    if len(expression) < 2:
        return True
    if expression[0] != expression[-1]:
        return False
    return is_palindrome_rek(expression[1:-1])

#Fibonacci Normally
def fibonaci_numbers(amount:int,exact:int):
    a = 0
    b = 1
    c = 1
    result = []
    for i in range(amount):
        result.append(c)
        c = a+b
        a = b
        b = c

    print("Liczba Ktorej Szukales:{} ".format(exact) ,result[exact-1])
    print("Cala lista Wypisanych liczb :",result)


#Fibonacci Recursive
def fibonacci_number_rek(exact:int):
    if exact < 3:
        return 1
    return fibonacci_number_rek(exact-2) + fibonacci_number_rek(exact-1)


#Checking if number is prime
def is_number_prime(number:int):
    for i in range(2,number):
        if number % i == 0:
            return False

    return True

#Showing specific amount of PRIME numbers
def show_prime_numbers(amount:int):
    for i in range(2,amount):

        for j in range(2,i+1):
            if i == j:
                print(i)
            if i % j == 0:
                break










