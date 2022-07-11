import random
print("|| we welcome you in the guess game ||")
name = input("enter your name : ")
words=['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
guess=''
d=0

while (d<=5):
    
    response=input("enter the word : ")
    if (len(response)>1):
        print("error")
    elif (response in word):
        guess+=response
        print(guess)
        print("uhooooo! you choose the right word")
    elif (word==guess):
        print("you won !\n ")
        f=input ("would you like to play again if yes please type yes if no please type no : ")
        if (f=="yes"):
            word=random.choice(words)
            guess=''
            d=0
            continue
        else:
            print("thank you for playing guess game ")
            break
    
    else:
        print("soory wrong choice.....try again \n")
        print("___")
        d +=1
        print("life left : ", 5-d)
    if(d==5):
        print('word is : ',word)
        f=input ("would you like to play again if yes please type yes if no please type no : ")
        if (f=="yes"):
            word=random.choice(words)
            guess=''
            d=0
            continue
        else:
            print("thank you for playing guess game ")
            break

    
    


    