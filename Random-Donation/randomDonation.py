import random 
random.seed()

people = []

for i in range(0,50):
    people.append(100)


for term in range(1,10000):
    for donor in range(1,50):
        if ( people[donor] != 0): 
            reciever = random.randrange(1,50)
            while (people[reciever] == 0 ):
                reciever = random.randrange(1,50)  

            people[donor]-=1
            people[reciever]+= 1     


for i in range (0,50):
    print ("person ", i , "value ",people[i] )