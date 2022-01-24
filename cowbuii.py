import random
# from secrets import choice
number=[]
attempts=0

def makenumber():
    for i in range(4):
        x=random.randrange(0,9)
        number.append(x)
    if len(number)> len(set(number)):
        number.clear()
        makenumber()

def playGame():
    global attempts
    attempts+=1
    cows=0
    bulls=0
    print(number)
    choice=input("please enter a 4 digt nbr")
    guess=[]
    for i in range(4):
        guess.append(int(choice[i]))
    for i in range(4):
        for j in range(4):
            if (guess[i]== number[j]):
                cows+=1
    for x in range(4):
        if (guess[x]==number[x]):
            bulls+=1
    print("bulls:",bulls)
    print("cows:",cows)
    if (bulls==4):
        print("you won after",attempts,"attempts!")
    if (bulls !=4):
        playGame()
makenumber() 
playGame()            



