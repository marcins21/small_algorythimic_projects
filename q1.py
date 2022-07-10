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


# (6.1) Checking if  number is  palindrome using list/string
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

