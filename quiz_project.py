import random

#AMOUNT OF QUIZ's
AMOUNT_OF_QUIZ = 8

#AMOUNT OF QUESTIONS IN EACH QUIZ max 15
AMOUNT_OF_QUESTIONS = 19


#CAPITALS
capitals = {'Poland':'Warsaw','Germany':'Berlin','Portugal':'Lizbona',
            'Spain':'Madryt','Italy':'Rzym','USA':'Washington',
            'Russia':'Moskwa','Finland':'Helsinki','Dania':'Kopenhaga',
            'Norwey':'Oslo','Sweden':'Sztokholm','Brazil':'Rio-De-Janeiro',
            'Argentina':'Buenos-Aires','Czech-Republic':'Prague','Japan':'Tokyo',
            'China':'Pekin','France':'Paris'}

if AMOUNT_OF_QUESTIONS < 16 and AMOUNT_OF_QUESTIONS > 0:
    pass

else:
    print("\n\n\nWRONG AMOUNT_OF_QUESTION\n\n\n")
    exit()

#-----------------------------------------------------------|
#Creating 5 lists-of 5 countries
#-----------------------------------------------------------|
rand_country = []
for i in range(AMOUNT_OF_QUIZ):
     rand_country.append(random.sample(list(capitals.keys()),AMOUNT_OF_QUESTIONS))
  


#------------------------------------------------------------|
#Getting correct answer
#------------------------------------------------------------|
coorect_answer = []
for i in range(AMOUNT_OF_QUIZ):
    
    random_country = random.choice(rand_country[i])
    coorect_answer.append(capitals[random_country])
    
    #Creating 5 quiz's with random countries
    with open("quiz"+str(i+1),'w') as file:
        file.write("Choose correct Capital of the Given Country : {} \n\n".format(random_country))
        for j in range(AMOUNT_OF_QUESTIONS):

            #Capitals of randomly choosen sets of countries Guarantee Correct answer is there
            file.write("({}){}\n".format(j+1,capitals[rand_country[i][j]]))


#Files with correct answers
with open("answers",'w') as file:
    for i in range(AMOUNT_OF_QUIZ):
    
            file.write("Correct answer for quiz number {} is {}\n".format(i+1,coorect_answer[i]))
        
