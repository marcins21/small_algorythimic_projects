
#--------------------------------------------------------------------------------------------------------
# CODING QUESTIONS
# Python coding questions on STRINGS
#---------------------------------------------------------------------------------------------------------

#   Q-1  Python program to remove given character from a string



def remove_character(expression,char):
    
    if char in expression:
        return expression.replace(char,"")
    else:
        print("Error Occured char doesn't exist in this expression")
        return 0 
#   print(remove_character("Marcin",'a'))


#   Q-2 Python program to count occurence of a given characters in a string
def count_occurence(expression,char):
    counter = 0
    for i in range(len(expression)):
        if expression[i] == char:
            counter +=1 
    return counter
#   print(count_occurence("Marcaiaan",'a'))


#   Q-3 Python program to check if two string are Anagram
def is_anagram(expression1,expression2):
    lengh_exp1 = len(expression1)
    lengh_exp2 = len(expression2)
    expression1 = expression1.lower()
    expression2 = expression2.lower()

    if lengh_exp1 != lengh_exp2:
        return False
    else:
        counter = 0
        for i in range(0,lengh_exp1):
            if expression1[i] == expression2[-1-i]:
                counter +=1 
        if counter == lengh_exp1:
            return True
        return False
#   print(is_anagram("Marcin","nicram"))   


#   Q-4 Python program to comparing array's size
def compare_array_size(array1:list,array2:list) -> bool:
    if len(array1) == len(array2):
        return True
    return False
#   print(compare_array_size([1,2,3],[12,3]))


#   Q-5 Python Program to find largest and smallest number in a array
def max_and_min_array(array:list):
    result = []
    result.append(max(array))
    result.append(min(array))
    return result
#   print(max_and_min_array([1,2,3,31]))


#   Q-6 python program to find second highest number in a integer array
def second_highest(array:list) -> int:
    largest_index = array.index(max(array))
    array.pop(largest_index)
    return max(array)
    #PROBLEM Finding second highest number but EDITING LIST :(
#   print(second_highest([1,2,31,44]))


#   Q-7 python program to find TWO maximum numbers in a array (solving problem above)
def two_max_numbers(array:list) -> list:
    #O(1)
    result = []
    result.append(max(array))
    array.pop(array.index(max(array)))
    result.append(max(array))
    return result
#   print(two_max_numbers([1,2,3,31,1000]))


#   Q-8 Python program to replace the string space with a given character
def replace_space_with_character(expression,character):
    return expression.replace(" ",character)
#   print(replace_space_with_character("sie ma ","lol"))


#   Q-9 V

#   Q-10 python program to convert lowercache char to uppercase of String V


#   Q-11 Python program to conver lowercase VOWELS to upperacase
def lower_to_upper_vowels(expression):
    vowels = ['a','e','y','o','u','v','x','i']
    result = []
    for i in range(len(expression)):
        if expression[i] in vowels:
            if expression[i].islower():
                result.append(expression[i].upper())
            else:
                result.append(expression[i])
        else:
            result.append(expression[i])     
    return ''.join(result)
#   print(lower_to_upper_vowels("siema"))


#   Q-12






