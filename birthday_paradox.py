import random
#DECLARING MONTHS AND DAYS
MONTHS = ['sty','lut','mar','kwi','maj','cze','lip','sie','wrz','paz','lis','gru']
DAYS = [i for i in range(1,32)]


#FUNCTION TO FIND IF BIRTHDAY REPEAT IN A RANDOM CHOICED LIST
def find_same_birthdays(birthdays:list):
    same_birthday = []
    result_list = []
    for i in range(len(birthdays)):
        
        #checking if birthday repeats
        tmp = birthdays.pop(0)
        if tmp in birthdays:
            same_birthday.append(tmp)
            #if birthday repeats then add '100' to another list
            result_list.append(100)
            
        else:
            result_list.append(0)

    return result_list

#FUNCTION TO CALCULATE AVERAGE VALUE OF THE LIST THAT CONTAINS '0' and '100'
def find_percentage(same_birthdays:list):
    return sum(same_birthdays)/len(same_birthdays)


print("-------WELCOME TO MY SIMULATION-------")
#VARIABLES
how_many_simulations = int(input("HOW MANY SIMULATIONS: "))
how_many_people = int(input("Size of the Group of People:"))
complete_result = []

#'FOR LOOP'  SIMULATIONS
for i in range(how_many_simulations):
    number_of_people = [[] for i in range(how_many_people)]
    
    # 'FOR LOOP' GROUP OF PEOPLE
    for j in range(how_many_people):
        
        #adding random days and month [[month,day] ... ]
        random_day = random.choice(DAYS)
        random_month = random.choice(MONTHS)
        number_of_people[j].append(random_month)
        number_of_people[j].append(random_day)

    #information that the program is not stuck
    if i % 1000 == 0:
        print(i,"/",how_many_simulations,"Simulations Completed")

    #getting value of the list 
    same_birthday_result = find_same_birthdays(number_of_people)

    ################################################################################################################
    #cheking if '100' is in the list then adding '100' to another list else adding '0'
    #
    #because if 100 EXIST  This means that we hit same birthday in the group of people
    #
    # if 100 DO NOT EXIST this mean that we didn't hit same birthday in a group of people
    ###############################################################################################################
    
    if 100 in same_birthday_result:
        complete_result.append(100)
    else:
        complete_result.append(0)

# getting average value of list filled above
# We're calculating ratio of HITTING or NOT HITTING the same birthday in the group of people 
# We can HIT or DO NOT HIT <--> 100% or 0%
# [100,0,100,0,0....] sa average of this list is our result
print("In the group of {} You have".format(how_many_people)
      ,find_percentage(complete_result),"% Chance to hit have same birthday with someone else")


