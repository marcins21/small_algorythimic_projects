#(1) Write a program to reverse a integer
def reverse_integer(number:int):
    reverse = ""
    while number != 0:
        temp = number % 10
        reverse = reverse + str(temp)
        number = number//10
    print(int(reverse))
    #reverse_integer(1234567)

#(2) Check if number is armstrong number
def armstrong_number(number):
    number = list(number)
    temp = 0
    for i in range(len(number)):
        temp+=pow(int(number[i]),3)

    if temp == int(''.join(number)):
        return True
    else:
        return False
    #print(armstrong_number('eg.370 eg.153'))

#(3) Check if  number is Prime number
def is_prime(number:int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
    #print(is_prime(13))

# (4) Fibonacci number Iterative method
def fibonacci_iterative(number:int):
    a = 0
    b = 1
    c = 1
    result = []
    for i in range(number):
        result.append(c)
        c = a+b
        a = b
        b = c
    return result
    #print(fibonacci_iterative(10))

# (5) Fibonacci series Recursive Method
def fibonacci_recursive(number:int):
    if number < 3:
        return 1
    return  fibonacci_recursive(number-2)+fibonacci_recursive(number-1)
    #print(fibonacci_recursive(5))

# (6) Checking if number is palindrome iterative method (Without changing to a list )
def is_palindrome(number:int):
    result = ""
    result_number = number
    while number != 0:
        result += str(number % 10 )
        number = number // 10
    if result_number == int(result):
        return True
    else:
        return False
    #print(is_palindrome(123321))


# (6.1) Checking if  expression is  palindrome using list/string
def is_palindrome_list(number):
    number = list(number)
    result = []
    for i in range(len(number)):
        if number[i] == number[-1-i]:
            result.append(number[i])
    if result == number:
        return True
    else:
        return False
    #print(is_palindrome_list('123321'))

# (7) Checking if number is palindrome recursive method
def is_palindrome_recursive(number):
    if len(number) < 3:
        return True
    if number[0] == number[-1]:
        return is_palindrome_recursive(number[1:-1])
    return False
    #print(is_palindrome_recursive('12321'))


# (8) the biggest number among 3
def biggest_among3(list_of_3numbers):
    if (list_of_3numbers[0] > list_of_3numbers[1]) and (list_of_3numbers[0] > list_of_3numbers[2]):
        return list_of_3numbers[0]
    if (list_of_3numbers[1] > list_of_3numbers[0]) and (list_of_3numbers[1] > list_of_3numbers[2]):
        return list_of_3numbers[1]
    else:
        return list_of_3numbers[2]
    #print(biggest_among3([6,6,6]))

# (9) Checking if number is binary
def is_binary(number):
    temp = ""
    while number != 0:
        if (number % 10 == 1) or (number % 10 == 0):
            temp += str(number % 10)
            number = number // 10
        else:
            return False
    return True
    #print(is_binary(1010101))

# (10) finding sum of number Recursive  #####
def sum_of_numbers(numbers:list):
    if len(numbers) == 2:
        return numbers[0]+numbers[1]
    else:
        #Dodawanie pierwszej i ostatniej
        temp = numbers[0]+numbers[-1]
        #obcinianie pierwszej i ostatniej
        numbers = numbers[1:-1]
        #dodawanie sumy tych numerow ktore obcielismy
        numbers.append(temp)
        #powtorzenie calej funkcji!
        return sum_of_numbers(numbers)
    #print(sum_of_numbers([1,2,4]))

# (11) Finding if number is Perfect number
def is_Perfect(number):
    divisiors = []
    for i in range(1,number):
        if number % i == 0:
            divisiors.append(i)
    if sum(divisiors) == number:
        return True
    else:
        return False
#   print(is_Perfect(6))

# (12) Power Function iterative
def number_power(number:float, exp:int):
    temp = 1
    for i in range(exp):
        temp *= number
    return temp
#   print(number_power(2,3))

# (13) Power Function recursive
def number_power_recursive(number:float, exp:int):
    if exp == 0:
        return 1
    return number * number_power_recursive(number,exp-1)
#   print(number_power_recursive(2,3))

# (14) Finding average of given numbers
def average_number(numbers:list):
    #leng = len(numbers)
    #return sum(numbers)/leng
    temp = 0
    lengh = len(numbers)
    for i in range(len(numbers)):
        temp += numbers[i]
    return temp/lengh
#   print(average_number([1,2,3]))

#-----------------------https://quescol.com/interview-preparation/python-coding-question---------------------------

# Q-17 Find Factorial of a number Iterative method
def factorial(number:int)-> int:
    temp = 1
    for i in range(number):
        temp *= number-i
    return temp
#   print(factorial(4))

# Q-18 Find Factorial Recursive method
def factorial_recursive(number:int):
    if number < 2:
        return 1
    return number * factorial_recursive(number-1)
#   print(factorial_recursive(4))

# Q-19 Check if number is odd or even
def odd_or_even(number:int):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Q-20 Print N first prime numbers
def n_primeNumbers(number:int):
    counter = 0
    result = []

    #meh ;( To Continue
    temp_low = 2
    temp_high = 1500
    ################

    for i in range(temp_low,temp_high):
        for j in range(temp_low,i+1):
            if i == j:
                result.append(i)
            if i % j == 0:
                break

    if len(result) >= number:
        for i in range(number):
            print(i+1,":",result[i])
# n_primeNumbers(100)

# Q-21 Print N Prime Numbers in a given range
def prime_numbers_in_range(lower_range:int,higher_range:int):
    for i in range(lower_range,higher_range):
        for j in range(2,i+1):
            if i == j:
                print(i)
            if i % j == 0:
                break
#   prime_numbers_in_range(190,200)

# Q-22 Done!
# Q-23 Done!
# Q-24 Power of a number without POW method (using FOR LOOP)
def power_of_number(number,exp:int)->float:
    temp = 1
    for i in range(exp):
        temp *= number
    return temp
#   print(power_of_number(2,3))

# Q-25 Power a number without POW method (using WHILE LOOP)
def power_of_number_while(number,exp:int):
    temp = 1
    counter = 0
    while counter != exp:
        temp *= number
        counter +=1
    return temp
#   print(power_of_number_while(2,3))




