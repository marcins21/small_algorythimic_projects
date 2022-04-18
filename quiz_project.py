import random





#CAPITALS
capitals = {'Poland':'Warsaw','Germany':'Berlin','Portugal':'Lizbona',
            'Spain':'Madryt','Italy':'Rzym','USA':'Washington',
            'Russia':'Moskwa','Finland':'Helsinki','Dania':'Kopenhaga',
            'Norwey':'Oslo','Sweden':'Sztokholm','Brazil':'Rio-De-Janeiro',
            'Argentina':'Buenos-Aires','Czech-Republic':'Prague','Japan':'Tokyo',
            'China':'Pekin','France':'Paris'}



#-----------------------------------------------------------|
#Creating 5 lists-of 5 countries
#-----------------------------------------------------------|
rand_country = []
for i in range(5):
     rand_country.append(random.sample(list(capitals.keys()),5))
  


#------------------------------------------------------------|
#Getting correct answer
#------------------------------------------------------------|
coorect_answer = []
for i in range(5):
    
    random_country = random.choice(rand_country[i])
    coorect_answer.append(capitals[random_country])
    
    #Creating 5 quiz's with random countries
    with open("quiz"+str(i+1),'w') as file:
        file.write("Choose correct Capital of the Given Country : {} \n\n".format(random_country))
        for j in range(5):

            #Capitals of randomly choosen sets of countries Guarantee Correct answer is there
            file.write("({}){}\n".format(j+1,capitals[rand_country[i][j]]))


#Files with correct answers
with open("answers",'w') as file:
    for i in range(5):
    
            file.write("Correct answer for quiz number {} is {}\n".format(i+1,coorect_answer[i]))
        
